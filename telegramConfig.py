import telegram
from telegram import Bot

chat_id = input("Please input the Farm owners Telegram chat id: ")
bot_token = input("Please enter the telegram bot Token: ")
message ="""\

Subject : KAJIADO FARM SOIL CONTENT 
Body : Your farm soil content at youe Elangata bean farm is {}. Please check and maintain it. If any issue



"""

def telegram_message(message):
    # Initializing the telegram bot.
    telegram.bot = (bot_token)
    try:
        bot.send_message = (chat_id, message)

    except:
        print("Error sending Telegram message")