import sys                    # Uses sys to print Exception reasons
import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # Uses MQTT protocol to communicate with Node-Red dashboard
import micropython            # Needed to run any MicroPython code
from machine import Pin       # Uses to define pin
import config                 # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 
import ujson                  # Creates JSON object for MQTT & Telegraf
import wifiConnection         # Uses for WiFi connection
import customChars            # Creates custom chars combined with text to show on LCD

# Initialize LCD
lcd = customChars.initializeLcd()
customChars.createCustomChars(lcd)
customChars.displayMainScreen(lcd)

# Initialize LED pin, PIR sensor pin, and buzzer pin
LED = Pin("LED", Pin.OUT)
PIR_sensor = Pin(28, Pin.IN, Pin.PULL_UP)
buzzer = Pin(0, Pin.OUT)
 
# Set default status
LED.off()
time.sleep(2)
security_flag = False
alarm_triggered = False
buzzer.off()

# Create a map between keypad buttons and characters
matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

# PINs according to schematic - Change the pins to match with your connections
keypad_rows = [9,8,7,6]
keypad_columns = [5,4,3,2]

# Create two empty lists to set up pins ( Rows output and columns input )
col_pins = []
row_pins = []
input_no = []
initial_pw = ['0','0','0','0']

# Loop to assign GPIO pins and setup input and outputs
for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    
# Build jason format for MQTT 
def build_json(variable_1, value_1):
    try:
        data = {variable_1: value_1}
        retValue = ujson.dumps(data)
        return retValue
    except:
        return None

# Send message to MQTT server
def send_topic(topicObject, topicName):
    print(f"{topicName}: {topicObject}")
    try:
        client.publish(topicName, topicObject)
        print("DONE")
    except Exception as e:
        print("FAILED")
        print(f"exception: {e}")
        # We must add error hadling here if WiFi being unavailable here

# Receive mqtt messages
def receive_topic(topicName, topicObject):
    # print(f"{topicName}: {topicObject}")
    print(f"Received topic: {topicName}, message: {topicObject}")
    global security_flag, initial_pw
    try:
        msg_str = topicObject.decode('utf-8')
        message = ujson.loads(msg_str)
        if topicName == b'dashboard/security':
            if message.get('security') == 'on':
                security_flag = True
            elif message.get('security') == 'off':
                security_flag = False
        elif topicName == b'dashboard/verify_passcode':
            # print(list(msg_str))
            if list(msg_str) == initial_pw:
                send_topic("true", "devices/verify_passcode")
            else:
                send_topic("false", "devices/verify_passcode")
        elif topicName == b'dashboard/update_passcode':
            initial_pw = list(msg_str)
            print(f"Passcode updated: {initial_pw}")
            send_topic("true", "devices/update_passcode")
    except Exception as e:
        print(f"Failed to process message: {e}")

# Send security mode status 
def sendSecurityState(state):
    topic = "devices/security"
    message = build_json("state", state)
    send_topic(message, topic)

# WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Connect to MQTT server
try:
    client = MQTTClient(client_id=config.MQTT_CLIENT_ID, server=config.MQTT_SERVER, port=config.MQTT_PORT, user=config.MQTT_USER, password=config.MQTT_KEY)
    # client = MQTTClient(config.MQTT_CLIENT_ID, config.MQTT_SERVER, config.MQTT_PORT)
    time.sleep(0.1)
    client.connect()
    print("Connected to %s" % (config.MQTT_SERVER))
    sendSecurityState("off")  # Initial state is off
except Exception as error:
    sys.print_exception(error, sys.stderr)
    print("Could not establish MQTT connection")
    wifiConnection.disconnect()
    print("Disconnected from WiFi.")

# Keyboard interrupt handler
def exceptionHandler(e):
    if e is KeyboardInterrupt:
        print("Keyboard interrupt")
    else:
        print("MQTT Brocker does not work or WiFi issues")

# Subscribe to topics
try:
    client.set_callback(receive_topic)
    client.subscribe('dashboard/security')
    client.subscribe('dashboard/verify_passcode')
    client.subscribe('dashboard/update_passcode')
except Exception as e:
    print(f"Subscription failed: {e}")

# Check entered passcode
def checkInput(input_no):
    global alarm_triggered
    global security_flag
    if input_no == initial_pw:
        buzzer.off()
        lcd.clear()  # Clear the LCD before printing
        lcd.print("Passcode correct!")  
        alarm_triggered = False
        security_flag = False
        sendSecurityState("off") # Update state
        time.sleep(0.1)
    else:
        lcd.clear()  # Clear the LCD before printing
        lcd.print("Wrong passcode!")

# Scan pressed keys
def scankeys():
    global security_flag
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            # key = None
            if col_pins[col].value() == 1:
                lcd.set_cursor(0,1)
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                lcd.clear()  # Clear the LCD before printing the new key
                lcd.set_cursor(0, 1)
                lcd.print(f'Key: {key_press}')  # Print the pressed key on the LCD
                if alarm_triggered:        
                    input_no.append(key_press)
                    lcd.clear()
                    lcd.print("Enter passcode:")
                    lcd.set_cursor(0, 1)
                    lcd.print('*' * len(input_no))
                    if len(input_no) == 4:
                        checkInput(input_no)
                        input_no.clear()
                else:
                    if key_press == 'A':
                        print("Activate security")
                        security_flag = True
                        sendSecurityState("on") # Update state
                        break
                    if key_press == 'D':
                        security_flag = False
                        sendSecurityState("off") # Update state
                        break               
                time.sleep(0.3)
            if len(input_no) == 4:
                checkInput(input_no)
                for i in range(0,4):
                    input_no.pop()
        row_pins[row].low()

# Loop
while True:
    try:
        client.check_msg()  # Check for incoming messages
    except Exception as e:
        print(f"Error checking messages: {e}")

    if security_flag:
        customChars.displaySecurityOn(lcd)
        if PIR_sensor.value() == 1:
            tempObj = build_json("motion", "Motion Detected!")
            lcd.clear()
            lcd.print("Motion Detected!")
            print(f"MQTT_MOTION_FEED: {config.MQTT_MOTION_FEED}, {tempObj}")
            send_topic(tempObj, config.MQTT_MOTION_FEED)
            LED.on()
            alarm_triggered = True
            while alarm_triggered:
                print(f"alarm_triggered: {alarm_triggered}")
                for i in range(30):
                    if not alarm_triggered:
                        break
                    buzzer.on()
                    time.sleep(0.1)
                    buzzer.off()
                    time.sleep(0.1)
                    scankeys()
        else:
            tempObj = build_json("motion", "No motion detected")
            LED.off()
            buzzer.off()
            time.sleep(0.5)
    else:
        customChars.displayMainScreen(lcd)
    scankeys()
