import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('токен')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе съесть яблоко!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list =["Разнообразие сортов: Существует более 7500 сортов яблок, что делает их одними из самых разнообразных фруктов по вкусу и использованию.",
           "Польза для здоровья: Яблоки богаты витамином C, антиоксидантами и пищевыми волокнами, помогающими поддерживать хорошее здоровье и укреплять иммунитет.",
           "Долговечность хранения: При правильном хранении в прохладе яблоки могут оставаться свежими в течение нескольких месяцев, обеспечивая доступ к питательным фруктам круглый год."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Вот факт о яблоке {random_fact}')

def send_reminders(chat_id):
    first_rem = "10:00"
    second_rem = "15:09"
    end_rem = "18:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - съешь яблоко")
            time.sleep(60)
        else:
            time.sleep(1)

bot.polling(none_stop=True)