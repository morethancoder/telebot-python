#main commands and bot creation

import telebot
from decouple import config
from weather import getCurrentWeather
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

weather = ["weather","temp","temprature"]
greetings = ["hello","hi","hey"]
whoAreYou = ["who" , "what" ]
botName = "billy"

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_message(message.chat.id,"welcome to billy bot just a bot to have fun building it")

#answering every message not just commands 
def isMSg(message):
    return True


@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    if words[0].lower() in weather :
        report = getCurrentWeather()
        return bot.send_message(message.chat.id,report or "failed to get weather !!")
    if words[0].lower() in whoAreYou :
        return bot.reply_to(message,f"i am {botName}")
    if words[0].lower() in greetings :
        return bot.reply_to(message,"hey how is going!")
    else:
        return bot.reply_to(message,"that's not a command of mine!")

bot.polling()
