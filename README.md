# Smart Home Security System Project ![Door Sensor Alarmed](https://hackmd.io/_uploads/SkaHizjU0.gif)


Author: Victoria(Shiyao) Xin / sx222ak

This project is a smart home security system that improves residential security through integrated hardware and software solutions. The system utilizes a Raspberry Pi Pico W, a motion sensor, a buzzer, a LCD screen and a keypad coded in MicroPython with a Node-RED dashboard for user interaction. The security system can be activated or deactivated via the physical keypad and dashboard switches. When activated, a motion sensor monitors the area and once movement is detected, a buzzer is triggered and a notification is displayed on the dashboard. The alarm can be deactivated by entering the correct password on the keypad, which can also be changed by the user via the dashboard, thus ensuring a convenient and secure real-time control and alarm environment for the user.

Approximate time: 10 hours

## Objective ![Book](https://hackmd.io/_uploads/ByjFVMiIR.gif)

I chose this project to explore the intersection of IoT and home security by creating a practical solution to improve residential security. This project allowed me to learn in-depth about using a variety of hardware components, thus providing a hands-on learning experience for building an integrated system.

#### Project Purpose
The main objective of this project was to develop a smart home security system that provides real-time monitoring and alerts for unauthorized access. By integrating motion detection, an alarm system, and a user-friendly control interface, it provides homeowners with a reliable and convenient way to increase the security of their residence.

#### Project Insights
This project will provide an in-depth understanding of how to integrate different hardware components and manage two-way communication using protocols such as MQTT. Additionally, it will provide some valuable insights into creating user interfaces using Node-RED.

## Materials  ![List](https://hackmd.io/_uploads/HyG7tMoIR.gif)

| Image | Item | Description | Cost |
| --- | --- | --- | --- |
| <img src="https://www.electrokit.com/cache/ba/700x700-product_41019_41019114_PICO-WH-HERO.jpg" alt="Raspberry Pi Pico W" width="100"> | [Raspberry Pi Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh) | The core microcontroller for managing system operations. | 109 SEK |
| <img src="https://www.electrokit.com/upload/product/41015/41015509/41015509.jpg" alt="PIR motion sensor HC-SR501" width="100"> | [PIR motion sensor HC-SR501](https://www.electrokit.com/en/pir-rorelsedetektor-hc-sr501) | Detects any movement within the monitored area. | 49 SEK |
| <img src="https://www.electrokit.com/upload/product/41003/41003596/41003596.jpg" alt="Buzzer 3.8 kHz" width="100"> | [Buzzer 3.8 kHz](https://www.electrokit.com/en/summer-3.8-khz) | Acts as an alarm to alert users of unauthorized access. | 37.50 SEK (Or you can get it from the kit below) |
| <img src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR0_I-tHyzbsIqZ-9WtNx_NhYKRByM63UTC9RiKUePIjZ7z-mUhzLh8u2Slnx_GieO7VKYGRgk" alt="LCD Screen" width="100"> | [LCD 1602](https://www.amazon.se/dp/B01M30ZWQR/ref=pe_24982401_503747021_TE_SCE_dp_1) | Displays system status and prompts for user interaction. | 281.69 SEK (price is for an entire kit) |
| <img src="https://www.electrokit.com/upload/product/41004/41004259/41004259-3.jpg" alt="Wires" width="100"> | [Keypad](https://www.amazon.se/dp/B01M30ZWQR/ref=pe_24982401_503747021_TE_SCE_dp_1) | Allows users to input commands and passcodes. | 281.69 SEK (price is for an entire kit)/ [Alternative purchase link](https://www.electrokit.com/en/tangentbord-membran-4x4-x-y) for 39 SEK |
| <img src="https://www.electrokit.com/cache/b9/700x700-product_41012_41012686_41012686.jpg" alt="Jumper wires" width="100"> | [Jumper wires](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hona/hane) | They are used to connect components on the breadboard and microcontroller. | 49 SEK |
| <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg" alt="Breadboard" width="100"> | [Breadboard](https://www.electrokit.com/en/kopplingsdack-840-anslutningar) | A board for making solderfree experiment circuits for prototyping. | 69 SEK |
| <img src="https://www.electrokit.com/cache/4c/700x700-product_40810_40810310_40810310.png" alt="Resistor carbon film 0.25W 1kohm (1k)" width="100"> | [Resistor carbon film 0.25W 1kohm (1k)](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k) | Resistors to limit current and divide voltages. | 1 SEK |


## Computer setup <img src="https://hackmd.io/_uploads/HJJ97MoIA.png" alt="Arrow" width="50"/>

### Chosen IDE

In this project, I am using Visual Studio Code (VSCode) as the Integrated Development Environment (IDE).

### How the code is uploaded

Code is uploaded to the Raspberry Pi Pico W using the Pymakr extension in VSCode, which allows seamless communication and code transfer between the computer and the microcontroller.

### Steps for Setting Up (Mac OS)

#### Step 1 - Install Node.js:

- Download and install [Node.js LTS](https://nodejs.org/en/download/package-manager).

#### Step 2 - Install VSCode:

- Download and install VSCode from [the official website](https://code.visualstudio.com/Download).

#### Step 3 - Install Pymakr Extension:

- Open VSCode and click on the Extensions icon in the sidebar. Alternatively, use the hotkey Cmd + Shift + X in VSCode.
- Search for "Pymakr" and click "Install".

![Screenshot 2024-06-24 at 22.01.55](https://hackmd.io/_uploads/H1HUZUDIR.png)

> :information_source: See more detailed information [here](https://hackmd.io/@lnu-iot/rkiTJj8O9).

#### Step 4 - Install MicroPython Firmware:

- Download the MicroPython firmware for the Raspberry Pi Pico W from [the MicroPython website](https://micropython.org/download/RPI_PICO_W/). Download the __latest__ uf2 file from the Releases category.
- Connect the Raspberry Pi Pico W to your computer while holding down the BOOTSEL button. This will make the Pico appear as a mass storage device.
- Drag and drop the downloaded .uf2 firmware file onto the Pico's storage. The device will reboot with MicroPython installed.

![Pico connection](https://www.raspberrypi.com/documentation/microcontrollers/images/MicroPython-640x360-v2.gif)

> :information_source: See more detailed information [here](https://hackmd.io/@lnu-iot/rkFw7gao_).

## Putting everything together <img src="https://hackmd.io/_uploads/HkdgLGiLA.png" alt="circuit" width="50"/>
This project involves connecting a Raspberry Pi Pico W, a motion sensor, a buzzer, an LCD screen, a keyboard, and two resistors. The details of how each component is connected are described below.
#### Circuit diagram
![Screenshot 2024-06-28 at 18.37.23](https://hackmd.io/_uploads/ry6mDv2IA.png)

> :bulb: **Tip:** The motion sensor needs 5V, not 3.3V.
#### Wiring Instructions

##### Raspberry Pi Pico W:
- Acts as the central microcontroller and manages all operations.
##### Keypad:
- The keypad has 8 pins. Connect the row pins of the keypad to the Pico's GPIO pins (e.g. GP5 to GP2). Connect the column pins of the keypad to another set of GPIO pins (e.g. GP9 to GP6).
##### Motion Sensor:
- Power: Connect the VCC pin of the PIR sensor to the VBUS pin on the Pico for 5V.
- Ground: Connect the GND pin to the ground rail.
- Output: Connect the OUT pin to a GPIO pin on the Pico (e.g. GP10).
##### Buzzer:
- Connect the positive side of the buzzer to a GPIO pin (e.g. GP11).
- Connect the negative side of the buzzer to the ground rail.
##### LCD Screen:
- Connect the VSS pin to the ground rail.
- Connect the VDD pin to VSYS pin.
- Connect the RS, RW, and E pins to the GPIO pins, GP12, the ground rail, and GP11).
- Connect the V0 pin to the ground rail via a 2kΩ resistor
- Connect the data pins (D4 to D7) to GPIO pins (e.g., GP10 to GP7).
- Connect the A (anode) pin to the 5V power rail.
- Connect the K (cathode) pin to the ground rail.
##### __Resistor__:
- Use two 1kΩ resistors in series where needed to create an equivalent 2kΩ resistance.


DEVELOPMENT SETUP: The current breadboard setup is perfect for prototyping. Modifications, troubleshooting and testing can be easily performed without soldering. For production setups, the breadboard should be replaced with a customized printed circuit board to ensure reliability, durability, and a more compact design.

## Platform  ![Control Panel](https://hackmd.io/_uploads/BkFjUMs80.png)
I chose [Node-RED](https://nodered.org/docs/getting-started/local) as the platform for this smart home security system project, using MQTT to build dashboards and manage communication between hardware components. Node-RED provides a visual interface that simplifies the creation of complex workflows by dragging and dropping nodes. It is highly extensible with a large library of pre-built nodes that can be used for a variety of functions such as HTTP requests, WebSockets and data processing.

Node-RED was used as the platform because it has powerful process-based visual programming development tools that are widely used in IoT applications. In addition, it natively supports MQTT, a lightweight messaging protocol ideal for IoT applications, allowing seamless two-way communication between the Raspberry Pi Pico W and the dashboard. Since the platform allows real-time interaction with connected devices, it is critical for controlling and monitoring security systems.

## The code ![Code](https://hackmd.io/_uploads/Hy7xwzo8A.png)
### Core functions

#### WiFi Connection
The wifiConnection.py script manages the connection to the WiFi network.
```python
# Contains functions to connect/disconnect from WiFi
import wifiConnection

# WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")
```
>The above code snippet is from main.py. It imports wifiConnection.py in main.py and calls the connect() function in wifiConnection.py to connect to the wifi.
- Function: connect()
    - Purpose: Connects the Pico W to the specified WiFi network using credentials from config.py.
    - Process: The function scans for networks and attempts to connect using the provided SSID and password in the config.py.

#### MQTT
The mqtt.py script handles MQTT communication, allowing interaction between hardware and Node-RED dashboards.
```python
from mqtt import MQTTClient 

# Connecting to MQTT server
try:
    client = MQTTClient(client_id=config.MQTT_CLIENT_ID, server=config.MQTT_SERVER, port=config.MQTT_PORT, user=config.MQTT_USER, password=config.MQTT_KEY)
    time.sleep(0.1)
    client.connect()
    print("Connected to %s" % (config.MQTT_SERVER))
    sendSecurityState("off")  # Initial state is off
except Exception as error:
    sys.print_exception(error, sys.stderr)
    print("Could not establish MQTT connection")
    wifiConnection.disconnect()
    print("Disconnected from WiFi.")
```
```python
# Subscribe to topics
try:
    client.set_callback(receive_topic)
    client.subscribe('dashboard/security')
    client.subscribe('dashboard/verify_passcode')
    client.subscribe('dashboard/update_passcode')
except Exception as e:
    print(f"Subscription failed: {e}")
```
```python
# Sending messages to MQTT server
def send_topic(topicObject, topicName):
    print(f"{topicName}: {topicObject}")
    try:
        client.publish(topicName, topicObject)
        print("DONE")
    except Exception as e:
        print("FAILED")
        print(f"exception: {e}")
```
> The above code snippets are from main.py. It imports MQTTClient class from mqtt.py in main.py to handle all MQTT-related operations, including broker connections, subscribing to topics, and publishing topics.
- Functions:
    - connect(): Establishes connection to the MQTT broker using credentials from config.py.
    - publish(topic, message): Publishes messages to specific MQTT topics.
    - subscribe(topic): Subscribes to topics and sets up callbacks for incoming messages.

Example code snippets for sending and receiving data:
##### Activate/Deactivate Security Mode
```python
# Send security mode status 
def sendSecurityState(state):
    topic = "devices/security"
    message = build_json("state", state)
    send_topic(message, topic)
```

##### Receiving topics and messages
```python
# Receive mqtt messages
def receive_topic(topicName, topicObject):
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
```

#### LCD Display
The lcd1602.py script controls the LCD, displaying messages and system status.
```python
def write(self, value):
    if isinstance(value, int):
        self.send(value, 1)
    elif isinstance(value, str):
        self.send(ord(value), 1)
    else:
        raise TypeError("Value must be an integer or a single character string")
```
```python
def print(self, message):
    for char in message:
        self.write(char)
```
```python
def create_char(self, location, charmap):
    location &= 0x7
    self.command(0x40 | (location << 3))
    for i in range(8):
        self.write(charmap[i])
```
> The above code snippets shows the three main used functions in lcd1602.py.
- Functions:
    - write(self, value): sends a value to the LCD display. The value can either be an integer or a single character string. If the value is a string, it converts the character to its ASCII integer value before sending it.
    - print(self, message): prints a string message to the LCD display.
    - create_char(self, location, charmap): creates a custom character that can be displayed on the LCD.

#### Deactivate Triggered Alarm
This function deactivates the alarm when the correct passcode is entered via the keypad.
```python
# Check entered passcode
def checkInput(input_no):
    global alarm_triggered
    global security_flag
    if input_no == initial_pw:
        buzzer.off()
        # Clear the LCD before printing
        lcd.clear()  
        lcd.print("Passcode correct!")  
        alarm_triggered = False
        security_flag = False
        # Update state
        sendSecurityState("off") 
        time.sleep(0.1)
    else:
        # Clear the LCD before printing
        lcd.clear()  
        lcd.print("Wrong passcode!")
```
> The above code snippet is from main.py. It checks the input passcode from the keypad. The triggered alarm will be deactivated and security mode will be set to off if the passcode is correct. 
- Function:
    - checkInput(input_no): compares the input with the passcode, and deactivates the triggered alarm if correct, otherwise shows "Wrong passcode" on LCD screen.

### Network and Communication Setup
1. Create config.py in the lib folder:

    - Add all credentials in this file:
    ```python
    WIFI_SSID = "your_wifi_ssid"
    WIFI_PASS = "your_wifi_password"
    MQTT_SERVER = "your_mqtt_broker_address"
    MQTT_PORT = "port_number"
    MQTT_USER = "your_mqtt_username"
    MQTT_KEY = "your_mqtt_user_password"
    # Can be anything start with id-
    MQTT_CLIENT_ID = "id-1223" 
    ```

2. Set up a WiFi connection:

Make sure the wifiConnection.py script uses these credentials to connect the Pico to the local network.

3. Set up MQTT:

Ensure that mqtt.py connects to the MQTT broker using these credentials.

## Transmitting the data / connectivity ![Centralized Network](https://hackmd.io/_uploads/BkxgIwzsUR.png)

__The data transmission is mainly event-driven.__
- Motion Detection Events:
    - When motion sensors detect movement, data is sent immediately, ensuring timely alerts.
- Alarm Deactivation:
    - Data is sent when the user deactivates the alarm by entering the correct code on the keypad.
- Passcode Change:
    - Data is transmitted when the user changes passcode via the dashboard.
        - The current passcode entered on the dashboard is sent to the device to check for correctness and the result is sent to the dashboard to continue to the next step.
        - A new passcode is entered and sent to the device to update the device passcode.
- Security Status Updates:
    - Status updates are mainly sent immediately when the user activates/deactivates safe mode. However, they can also be sent periodically to ensure that the system is functioning properly. These updates can be sent every few minutes or at customized intervals to check connectivity and system response.

### Design Choices and their Impact

#### Chosen Wireless Protocol: WIFI

WiFi was used for this project because it is widely available and easy to integrate with the Raspberry Pi Pico W. WiFi can provide a stable and robust connection for real-time data transfer and has sufficient coverage for typical home areas. It is suitable for the real-time data transfer required by smart home devices. 
- Device range: WiFi coverage is usually sufficient to cover all areas within a residential space. Using WIFI ensures that the security system stays connected to the local network and the Internet throughout the apartment/house. Therefore, by using WiFi, the security system can reliably communicate with the Node-RED dashboard and other devices within the home. This ensures that alarms, status updates, and other such control commands are transmitted without noticeable signal loss or interruption.
- Battery consumption: WIFI tends to consume more battery, especially for applications that require real-time communication given their need for a stable WIFI connection. However, since this security system is primarily event-driven in terms of data transfer, power can be saved by configuring the system to use power-saving modes even when it's not transferring data, and only activating WIFI when it's needed.

#### Chosen Transport Protocol: MQTT
This project uses MQTT as the transport protocol because it reliably delivers information with minimal overhead, supports various Quality of Service (QoS) levels, and is well suited for publish-subscribe real-time communication used in this project.
- Device range: Given that the MQTT protocol runs over the TCP/IP protocol, its range is determined by the WiFi network.
- Battery consumption: In general, MQTT has relatively low processing power and therefore low energy consumption per message. Since MQTT has multiple Quality of Service (QoS) levels, if lower power consumption is strongly desired, you can choose Qos 0 to achieve this, but only at the risk of unreliable data transmission.

## Presenting the data ![Database](https://hackmd.io/_uploads/H1NtDGsIR.gif)

![dashboard1](https://hackmd.io/_uploads/B1jW0X28R.png)

The dashboard was built using Node-RED, a free and open source process-based visual programming development tool. It integrates with various hardware components via MQTT for real-time control and monitoring. The dashboard contains Node-RED dashboard nodes, e.g., ui switch button nodes, ui text nodes, ui gauge nodes, mqtt related nodes, function nodes, change nodes, and so on. In addition, database-related influxdb nodes from the node-red-contrib-influxdb palette were used. The Node-RED interface allows users to easily monitor security status, view logs and adjust settings.

![nodes](https://hackmd.io/_uploads/rJcowuaIA.png)


Each time a new MQTT message is received from the smart home security system regarding motion detection, the data is saved to the database. The frequency with which data is saved is directly related to the events reported by the motion detection system, i.e. each motion event triggers an immediate write to InfluxDB.

#### Choice of Database: [InfluxDB](https://www.influxdata.com)
Given that InfluxDB specializes in working with time-series data, it's perfect for recording timestamped motion detection events. It's easy to use because users simply install the InfluxDB palette to Node-RED and then use the InfluxDB node. In addition, InfluxDB supports data retention and since the free InfluxDB Cloud Serverless Account has a 30-day data retention limit, it's easy to automatically get rid of old data that has expired.

![db](https://hackmd.io/_uploads/HkIFW42LC.png)

#### Automation/Triggers of the Data
###### Motion detection and data storage:
Whenever the motion sensor detects motion, it sends an MQTT message <img src="https://hackmd.io/_uploads/BJ6QlfsIC.png" alt="Arrow" width="20"/> Node-RED processes the message and saves the event details to InfluxDB.The event is also added to the dashboard's motion log.
###### Real-time dashboard updates:
Each new motion detection event <img src="https://hackmd.io/_uploads/BJ6QlfsIC.png" alt="Arrow" width="20"/> A new event is added to the Motion Log list on the dashboard and ensure that the most recent events are displayed first.
###### Node-RED Server Restart Processing (Consider Server Downtime):
The Node-RED server is restarted <img src="https://hackmd.io/_uploads/BJ6QlfsIC.png" alt="Arrow" width="20"/> Node-RED queries InfluxDB for all motion detection events from the last two days and uses this data to update the motion logs on the dashboard.


## Finalizing the design
This is my first IoT project and it is both new and exciting for me. Although I have done some similar projects, we have used WIO terminal instead of directly using microcontrollers. Therefore, I enjoyed the experience of working on such a project. Although I encountered some problems, especially in the beginning, such as uploading files to the Rasbberry pi pico using extensions in the VS Code and the MQTT setup, overall the project went well and I am happy with the results. If I had more time, I would like to make this system more robust and add more features.

![prototype](https://hackmd.io/_uploads/SJ8yo7nIR.jpg)


> :mega: [Click here to See the Video Presentation ](https://www.youtube.com/watch?v=kD_n2ydlhK4)
