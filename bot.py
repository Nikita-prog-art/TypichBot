import telebot
import openai
from subprocess import Popen

Popen(["sh", "-c", "./llama-start.sh"])

API_TOKEN = open(".env").readline()

bot = telebot.TeleBot(API_TOKEN)

ai = openai.OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="123"
    )

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Я Тупич. Маленькая языковая модель.
""")

lst = []

@bot.message_handler(commands=['reset'])
def reset(message):
    global lst
    lst = []
    bot.reply_to(message, "reseted")


@bot.message_handler(func=lambda message: True)
def echo_message(message: telebot.types.Message):
    global lst
    lst.append({
        #"role": message.from_user.first_name,
        "role": "user",
        "content" : message.text
        })
    print(message.text)
    ans = ai.chat.completions.create(
        messages=lst,
        model="1"
        ).choices[0].message.content
    print(ans)
    lst.append({
        "role" : "assistant",
        "content" : ans
    })
    bot.reply_to(message, ans, parse_mode="markdown")


bot.infinity_polling()
