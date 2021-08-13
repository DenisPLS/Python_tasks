import telebot
import time
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


bot = telebot.TeleBot("1776101982:AAHuZruet8_m4GcaLLLd4TdFle6oZD-GOTk")
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('8ce2c2e97a1fb9a880f0c920062771b2', config_dict)
owm.supported_languages
mgr = owm.weather_manager()

@bot.message_handler(content_types = ['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    wind = w.wind()["speed"]
    humidity = w.humidity
    pressure = w.pressure['press']

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"  # Получаем облачность
    answer += "Температура: " + str(temp) + "\n"                                 # Получаем температуру
    answer += "Ветер: " + str(wind) + " м/с" + "\n"                              # Получаем скорость ветра    
    answer += "Влажность: " + str(humidity) + " %" + "\n"                        # Получаем влажность
    answer += "Давление: " + str((int(pressure/1.333))) + " мм.рт.ст"+ "\n\n"    # Получаем давление

    bot.send_message(message.chat.id, answer)

# bot.polling(none_stop = True)
# bot.infinity_polling()

while True:
    try:
        bot.polling(none_stop = True, interval = 0, timeout = 20)
    except Exception as E:
        time.sleep(1)