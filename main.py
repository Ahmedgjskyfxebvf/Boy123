import telebot
from flask import Flask, request

API_TOKEN = '8122329927:AAHRKHfIB1JsZLGYKGjczYZwO-P55XYxY3c'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(name)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا بك يا " + message.from_user.first_name)

@app.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'ok', 200

@app.route('/')
def index():
    return "البوت شغال ✅"

if name == 'main':
    bot.remove_webhook()
    bot.set_webhook(url='https://رابط_مشروعك.onrender.com/')
    app.run(host="0.0.0.0", port=10000)