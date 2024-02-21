import serial
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Serial communication setup
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to

# Email configuration
sender_email = "tyrrickndungu@gmail.com"  # Replace with your email address
receiver_email = "+254723005901@your_carrier_sms_gateway.com"  # Replace with your phone number's SMS gateway
password = "your_email_password"  # Replace with your email password
smtp_server = "smtp.gmail.com"  # Adjust for your email provider
smtp_port = 600  # Adjust for your email provider

def send_email(message):
    # Create message
    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to email account
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Disconnect from server
    server.quit()

def read_sensor_data():
    # Read data from Arduino
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("Soil Moisture:"):
            return line

def main():
    while True:
        # Read sensor data
        sensor_data = read_sensor_data()

        # Print data to console
        print(sensor_data)

        # Send email every 6 hours
        if time.localtime().tm_hour % 6 == 0:
            send_email(sensor_data)
            print("Email sent!")

        time.sleep(10)  # Adjust the delay as needed

if __name__ == "__main__":
    main()
