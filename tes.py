import telebot
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
import time

# Inisialisasi bot
bot = telebot.TeleBot("7180943695:AAHdjI562H8aMRwhcbco9VJ5hzYRARcbzdM")

# Inisialisasi bot
bot = telebot.TeleBot("TOKEN_BOT_TELEGRAM")

@bot.message_handler(commands=['get_ip_info'])
def get_ip_info(message):
    user_id = message.from_user.id
    CHAT_ID = [1234567890]  # Ganti dengan daftar ID yang diizinkan

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

            message_text = f"══════════•●•══════════\n"
            message_text += f"◈ *Alamat IP :* `{ip_address}`\n"
            message_text += f"◈ *Kota :* `{city}`\n"
            message_text += f"◈ *Wilayah :* `{region}`\n"
            message_text += f"◈ *Negara :* `{location_response.country}`\n"
            message_text += f"◈ *Zona Waktu :* `{timezone}`\n"
            message_text += f"◈ *ISP :* `{isp}`\n"
            message_text += f"══════════•●•══════════"
            bot.reply_to(message, message_text, parse_mode="Markdown")
        else:
            bot.reply_to(message, "Gagal mendapatkan informasi IP")
    except IndexError:
        bot.reply_to(message, "Gunakan perintah /get_ip_info domain/ip")
    except socket.gaierror:
        bot.reply_to(message, "Domain atau IP tidak ditemukan")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Jalankan bot
bot.polling()
