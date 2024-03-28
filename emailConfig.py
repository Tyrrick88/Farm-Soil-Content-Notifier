import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


smtp_port  = 465
sender_email = input('Please Enter the senders e-mail address: ')
password = input('Please input the senders email address pass word: ')
reciever_email = input('Please enter the recivers email address: ')
smtp_server = 'smtp.gmail.com'
message = """\
Subject : FARM SOIL CONTENT.

Your Soil Analysis is as follows:
Body : your soil farm content is {}


"""

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
    server.sendmail(sender_email, reciever_email, msg.as_string())

    # Disconnect from server
    server.quit()