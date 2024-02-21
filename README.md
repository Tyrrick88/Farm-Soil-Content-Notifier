Soil Sensor Data Notifier
This Python script interacts with an Arduino connected to FC28 Hygrometer and DHT11 sensor, sending soil moisture, temperature, and humidity data via email or SMS every 6 hours. It is designed for monitoring soil conditions on a farm.

Table of Contents
Prerequisites
Installation
Configuration
Usage
Testing
Contributing
License
Prerequisites
Arduino board with FC28 Hygrometer and DHT11 sensor.
Serial communication between Arduino and Python.
SMTP server (for email functionality).
Access to an email account for sending emails.
(Optional) Information on the SMS gateway domain for sending SMS(Safaricom).
Installation
Clone or download the repository to your local machine.

Install required Python packages using the following command:

bash

pip install pyserial
Upload the Arduino code to read sensor data to your Arduino board.

Configuration
Open the Python script (FarmSoilNotifierscript.py) in a text editor.
Update the following variables with your information:
sender_email: Your email address for sending notifications.
receiver_email: Either your phone number's SMS gateway or another email address for email notifications.
password: Your email password or App Password (for Gmail, if applicable).
smtp_server and smtp_port: SMTP server details for sending emails.
(Optional) Adjust the COM port in the ser = serial.Serial('COM3', 9600) line to match your Arduino's connection.
Usage
Run the Python script:

bash

FarmSoilNotifier.py
Monitor the console for real-time sensor data.

Receive email or SMS notifications every 6 hours with the latest soil conditions.

Testing
Run unit tests to verify certain functions:

bash

python -m unittest FarmSoilNotifierscript_test.py
Note: Comprehensive testing involving external interactions (Arduino, email, SMS) may require manual testing in a controlled environment.

Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

