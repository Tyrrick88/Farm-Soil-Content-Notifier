import serial
import time
import smtplib
import emailConfig

# Serial communication setup
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to


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
            emailConfig(sensor_data)
            print("Email sent!")

        time.sleep(10)  # Adjust the delay as needed

if __name__ == "__main__":
    main()
