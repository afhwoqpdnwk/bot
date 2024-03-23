import telebot
import socket
import requests
from dbip import DbIpCity
import time

# Inisialisasi bot
bot = telebot.TeleBot("7180943695:AAHdjI562H8aMRwhcbco9VJ5hzYRARcbzdM")

@bot.message_handler(commands=['get_ip_info'])
def get_ip_info(message):
    user_id = message.from_user.id
    CHAT_ID = [5066246825]  # Ganti dengan daftar ID yang diizinkan

    if user_id not in CHAT_ID:
        bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return

    try:
        address = message.text.split()[1]
        ip_address = socket.gethostbyname(address)
        timestamp = int(time.time())
        url = f"https://ipinfo.io/{ip_address}/json?timestamp={timestamp}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            org_parts = data.get('org', 'Unknown').split(" ")
            isp = " ".join(org_parts[1:]) if len(org_parts) > 1 else org_parts[0]

            timezone = data.get('timezone')
            region = data.get('region')
            city = data.get('city')

            location_response = DbIpCity.get(ip_address, api_key='free')

            message = f"══════════•●•══════════\n"
            message += f"◈ *Alamat IP :* `{ip_address}`\n"
            message += f"◈ *Kota :* `{city}`\n"
            message += f"◈ *Wilayah :* `{region}`\n"
            message += f"◈ *Negara :* `{location_response.country}`\n"
            message += f"◈ *Zona Waktu :* `{timezone}`\n"
            message += f"◈ *ISP :* `{isp}`\n"
            message += f"══════════•●•══════════"
            bot.send_message(chat_id=message.chat.id, text=message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id=message.chat.id, text="Gagal mendapatkan informasi IP")
    except IndexError:
        bot.reply_to(message, "Gunakan perintah /get_ip_info domain/ip")
    except socket.gaierror:
        bot.reply_to(message, "Domain atau IP tidak ditemukan")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Jalankan bot
bot.polling()
