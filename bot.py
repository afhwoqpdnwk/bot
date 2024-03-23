import tempfile
import os
import datetime
import time
import subprocess
import telegram
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from CloudFlare import CloudFlare
import random
import string
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
import json
import base64
import urllib.parse

# Ganti dengan token bot Telegram dan Chat id Anda
TELEGRAM_TOKEN = '7180943695:AAHdjI562H8aMRwhcbco9VJ5hzYRARcbzdM'
#Tambahkan koma jika ingin menambahkan chat id lain,contoh [CHAT_ID, CHAT_ID2]
CHAT_ID = [5066246825, 5973850814, 5821080403, 5920844499]


# Ganti dengan API Key Cloudflare Anda
CLOUDFLARE_API_KEY = 'd0328b30f47965ece4e692b1c0c3dc55ac224'
CLOUDFLARE_EMAIL = 'dakross81@gmail.com'
DOMAIN1 = 'efwangstore.my.id'
DOMAIN2 = 'premiumserver.me'
DOMAIN3 = 'fonestores.my.id'
DOMAIN4 = 'ryanvpn.my.id'
ZONEID1 = '674bd9c87f757f2ab1f5254c0146fc56'
ZONEID2 = '24900651852c5783074d7a2bfecd7a29'
ZONEID3 = 'd39d6d776279cea12773883d5a7e0362'
ZONEID4 = 'ae8a1a1cb57908185f90fb307fa5503d'
UUID = '1d1c1d94-6987-4658-a4dc-8821a30fe7e0'
BUGILPED = '104.26.7.171'
BUGVIDIO = 'quiz.int.vidio.com'
BUGVISION = '104.18.225.52'
BUGISATEDU = '141.193.213.10'
ISATEDU2 = 'beta.zoom.us'
TUTORHI = 'telegra.ph/CARA-IMPORT-KONFIG-HTTP-INJECTOR-03-07'
TUTORHC = 'telegra.ph/CARA-IMPORT-KONFIG-HTTP-CUSTOM-03-07'
TUTORVNG = 'telegra.ph/CARA-IMPORT-KONFIG-V2rayNG-03-07'
WAKTU = '1 Jam'
PEMBATAS = '☉————————————————————————☉'
SGTRIAL = 'sgtrial'
IDTRIAL = 'idtrial'



BASE64_STATE = 1
user_ips = {}

def cancel(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    message = "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += "/add_subdomain 𝙙𝙖𝙛𝙩𝙖𝙧 𝙞𝙥 𝙨𝙪𝙗𝙙𝙤𝙢𝙖𝙞𝙣\n"
    message += "/add_cname_pribadi 𝙥𝙧𝙞𝙗𝙖𝙙𝙞 𝙩𝙤 𝙥𝙧𝙞𝙗𝙖𝙙𝙞\n"
    message += "/add_cname_public 𝙥𝙪𝙗𝙡𝙞𝙘 𝙩𝙤 𝙥𝙧𝙞𝙗𝙖𝙙𝙞\n"
    message += "/add_cname_pelanggan 𝙘𝙣𝙖𝙢𝙚 𝙥𝙚𝙡𝙖𝙣𝙜𝙜𝙖𝙣\n"
    message += "/renew 𝙧𝙚𝙣𝙚𝙬 𝙥𝙚𝙡𝙖𝙣𝙜𝙜𝙖𝙣\n"
    message += "/delete_subdomain 𝙝𝙖𝙥𝙪𝙨 𝙨𝙪𝙗𝙙𝙤𝙢𝙖𝙞𝙣\n"
    message += "/delete_idtrial 𝙝𝙖𝙥𝙪𝙨 𝙞𝙙𝙩𝙧𝙞𝙖𝙡\n"
    message += "/delete_sgtrial 𝙝𝙖𝙥𝙪𝙨 𝙨𝙜𝙩𝙧𝙞𝙖𝙡\n"
    message += "/list_subdomain 𝙡𝙞𝙨𝙩 𝙨𝙪𝙗𝙙𝙤𝙢𝙖𝙞𝙣\n"
    message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += "/ip_info 𝙘𝙝𝙚𝙘𝙠 𝙙𝙤𝙢𝙖𝙞𝙣/𝙞𝙥 𝙞𝙣𝙛𝙤\n"
    message += "/scan 𝙨𝙘𝙖𝙣 𝙞𝙥\n"
    message += "/ping 𝙥𝙞𝙣𝙜 𝙙𝙤𝙢𝙖𝙞𝙣/𝙞𝙥\n"
    message += "/create_vmess 𝙘𝙤𝙣𝙛𝙞𝙜 𝙫𝙢𝙚𝙨𝙨\n"
    message += "/create_vless 𝙘𝙤𝙣𝙛𝙞𝙜 𝙫𝙡𝙚𝙨𝙨\n"
    message += "/create_trojan 𝙘𝙤𝙣𝙛𝙞𝙜 𝙩𝙧𝙤𝙟𝙖𝙣\n"
    message += "/create_vmess_trial 𝙘𝙤𝙣𝙛𝙞𝙜 𝙫𝙢𝙚𝙨𝙨 𝙩𝙧𝙞𝙖𝙡\n"
    message += "/create_vless_trial 𝙘𝙤𝙣𝙛𝙞𝙜 𝙫𝙡𝙚𝙨𝙨 𝙩𝙧𝙞𝙖𝙡\n"
    message += "/create_trojan_trial 𝙘𝙤𝙣𝙛𝙞𝙜 𝙩𝙧𝙤𝙟𝙖𝙣 𝙩𝙧𝙞𝙖𝙡\n" 
    message += "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    context.bot.send_message(chat_id=user_id, text=message, reply_markup=ReplyKeyboardRemove())
    if user_id in user_ips:
        del user_ips[user_id]
    return ConversationHandler.END
  
def add_subdomain(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END  
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return 'wait_domain'

def wait_domain(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain :", reply_markup=markup)
    return 'wait_subdomain'

def wait_subdomain(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['subdomain'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input IP:", reply_markup=markup)
    return 'wait_ip'

def wait_ip(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['ip'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'A',
        'name': f"{user_data['subdomain']}.{user_data['domain']}",
        'content': user_data['ip'],
    }
    try:
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['subdomain']}.{user_data['domain']}"})
        if records:
            cf.zones.dns_records.delete(zone_id, records[0]['id'])
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"          *Hapus Domain Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`Name   : ``{user_data['subdomain']}`\n"
            message += f"`Sub    : ``{user_data['subdomain']}.{user_data['domain']}`\n"
            message += f"`Domain : ``{user_data['domain']}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['subdomain']}`", parse_mode=telegram.ParseMode.MARKDOWN)
        cf.zones.dns_records.post(zone_id, data=record)
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"              *Add IP Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['subdomain']}`\n"
        message += f"`Sub    : ``{user_data['subdomain']}.{user_data['domain']}`\n"
        message += f"`IP     : ``{user_data['ip']}`\n"        
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"        
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error creating DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menciptakan rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)
   
def delete_subdomain(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Pilih domain untuk menghapus subdomain:", reply_markup=markup)
    return 'wait_delete_domain'

def wait_delete_domain(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_delete_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain :", reply_markup=markup)
    return 'wait_delete_subdomain'

def wait_delete_subdomain(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    subdomain_to_delete = update.message.text.lower()
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    try:
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{subdomain_to_delete}.{user_data['domain']}"})
        if records:
            cf.zones.dns_records.delete(zone_id, records[0]['id'])
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"          *Hapus Domain Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`Name   : ``{subdomain_to_delete}`\n"
            message += f"`Sub    : ``{subdomain_to_delete}.{user_data['domain']}`\n"
            message += f"`Domain : ``{user_data['domain']}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{subdomain_to_delete}`", parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error deleting DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menghapus rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)
    
def delete_sgtrial(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    try:
        records = cf.zones.dns_records.get(ZONEID1, params={'name': f"{SGTRIAL}.{DOMAIN1}"})
        if records:
            cf.zones.dns_records.delete(ZONEID1, records[0]['id'])
            context.bot.send_message(chat_id=user_id, text=f"Subdomain : `{SGTRIAL}`\nDomain : `{DOMAIN1}`\nberhasil dihapus", parse_mode=telegram.ParseMode.MARKDOWN)
            return cancel(update, context)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{SGTRIAL}`", parse_mode=telegram.ParseMode.MARKDOWN)
            return cancel(update, context)
    except Exception as e:
        print(f"Error deleting DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menghapus rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)
    
def delete_idtrial(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    try:
        records = cf.zones.dns_records.get(ZONEID1, params={'name': f"{IDTRIAL}.{DOMAIN1}"})
        if records:
            cf.zones.dns_records.delete(ZONEID1, records[0]['id'])
            context.bot.send_message(chat_id=user_id, text=f"Subdomain : `{IDTRIAL}`\nDomain : `{DOMAIN1}`\nberhasil dihapus", parse_mode=telegram.ParseMode.MARKDOWN)
            return cancel(update, context)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{IDTRIAL}`", parse_mode=telegram.ParseMode.MARKDOWN)
            return cancel(update, context)
    except Exception as e:
        print(f"Error deleting DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menghapus rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)

def add_cname_pribadi(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Pilih domain :", reply_markup=markup)
    return 'wait_cname_domain_pribadi'
    
def wait_cname_domain_pribadi(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain untuk pribadi :", reply_markup=markup)
    return 'wait_cname_subdomain_pribadi'

def wait_cname_subdomain_pribadi(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['cname_subdomain_pribadi'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain server pribadi :", reply_markup=markup)
    return 'wait_server_subdomain_pribadi'

def wait_server_subdomain_pribadi(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_subdomain_pribadi'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['cname_subdomain_pribadi'], 
        'content': f"{user_data['server_subdomain_pribadi']}.{user_data['domain']}",
    }
    try:
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['cname_subdomain_pribadi']}.{user_data['domain']}"})
        if records:
            cf.zones.dns_records.delete(zone_id, records[0]['id'])
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"          *Hapus Domain Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`Name   : ``{user_data['cname_subdomain_pribadi']}`\n"
            message += f"`Sub    : ``{user_data['cname_subdomain_pribadi']}.{user_data['domain']}`\n"
            message += f"`Domain : ``{user_data['domain']}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['cname_subdomain_pribadi']}`", parse_mode=telegram.ParseMode.MARKDOWN)
        cf.zones.dns_records.post(zone_id, data=record)
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"    *Add Domain Pribadi Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['cname_subdomain_pribadi']}`\n"
        message += f"`Sub    : ``{user_data['cname_subdomain_pribadi']}.{user_data['domain']}`\n"
        message += f"`Server : ``{user_data['server_subdomain_pribadi']}.{user_data['domain']}`\n"
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error creating DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menciptakan rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)

def add_cname_pelanggan(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Pilih domain :", reply_markup=markup)    
    return 'wait_cname_domain'
    
def wait_cname_domain(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain pelanggan :", reply_markup=markup)    
    return 'wait_cname_subdomain'

def wait_cname_subdomain(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['cname_subdomain'] = update.message.text

    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)          
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain server pribadi :", reply_markup=markup)    
    return 'wait_server_subdomain'

def wait_server_subdomain(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_subdomain'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
        
    reply_keyboard = [['30', '60'], ['90', '/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Expired Hari:", reply_markup=markup)    
    return 'wait_server_subdomain_expired'

def wait_server_subdomain_expired(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_input = update.message.text
    user_data['server_subdomain_expired'] = user_input
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=int(user_data['server_subdomain_expired']))
    expiration_formatted = expiration_date.strftime('%Y-%m-%d')
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['cname_subdomain'], 
        'content': f"{user_data['server_subdomain']}.{user_data['domain']}",
        'comment': f"{expiration_formatted}", 
    }
    try:
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['cname_subdomain']}.{user_data['domain']}"})
        if records:
            cf.zones.dns_records.delete(zone_id, records[0]['id'])
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"          *Hapus Domain Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`Name   : ``{user_data['cname_subdomain']}`\n"
            message += f"`Sub    : ``{user_data['cname_subdomain']}.{user_data['domain']}`\n"
            message += f"`Domain : ``{user_data['domain']}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['cname_subdomain']}`", parse_mode=telegram.ParseMode.MARKDOWN)
        cf.zones.dns_records.post(zone_id, data=record)
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"            *Add Buyer Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Buyer   : `@{user_data['cname_subdomain']}\n"
        message += f"`Name    : ``{user_data['cname_subdomain']}`\n"
        message += f"`Sub     : ``{user_data['cname_subdomain']}.{user_data['domain']}`\n"
        message += f"`Server  : ``{user_data['server_subdomain']}.{user_data['domain']}`\n"
        message += f"`Domain  : ``{user_data['domain']}`\n"
        message += f"`Expired : ``{expiration_formatted}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"                
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error creating DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menciptakan rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)

def add_cname_server(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END        
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Pilih domain :", reply_markup=markup)    
    return 'wait_cname_domain_server'
    
def wait_cname_domain_server(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain :", reply_markup=markup)    
    return 'wait_cname_subdomain_server'

def wait_cname_subdomain_server(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['cname_subdomain_server'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input domain public yang akan dipointing :", reply_markup=markup)    
    return 'wait_server_subdomain_server'

def wait_server_subdomain_server(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_subdomain_server'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)    
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)    
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['cname_subdomain_server'], 
        'content': user_data['server_subdomain_server'],
    }
    try:
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['cname_subdomain_server']}.{user_data['domain']}"})
        if records:
            cf.zones.dns_records.delete(zone_id, records[0]['id'])
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"          *Hapus Domain Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`Name   : ``{user_data['cname_subdomain_server']}`\n"
            message += f"`Sub    : ``{user_data['cname_subdomain_server']}.{user_data['domain']}`\n"
            message += f"`Domain : ``{user_data['domain']}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['cname_subdomain_server']}`", parse_mode=telegram.ParseMode.MARKDOWN)
        cf.zones.dns_records.post(zone_id, data=record)
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"    *Add Domain Public Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['cname_subdomain_server']}`\n"
        message += f"`Sub    : ``{user_data['cname_subdomain_server']}.{user_data['domain']}`\n"
        message += f"`Public : ``{user_data['server_subdomain_server']}`\n"
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error creating DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat menciptakan rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)

def scan(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    try:
        os.system('/root/scan.sh')
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")
    return cancel(update, context)
    
def create_vless(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_vless'

def wait_domain_vless(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_subdomain_vless'
    elif selected_domain == 'cancel':
        return cancel(update, context)    
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_vless'

def wait_subdomain_vless(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_vless'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)

    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain server pribadi :", reply_markup=markup)    
    return 'wait_server_vless'

def wait_server_vless(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_vless'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    
    reply_keyboard = [['30', '60'], ['90', '/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Expired Hari:", reply_markup=markup)    
    return 'wait_exp_vless'

def wait_exp_vless(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_input = update.message.text
    user_data['wait_expired_vless'] = user_input
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=int(user_data['wait_expired_vless']))
    expiration_formatted = expiration_date.strftime('%Y-%m-%d')
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['domain_vless'], 
        'content': f"{user_data['server_vless']}.{user_data['domain']}",
        'comment': f"{expiration_formatted}", 
    }

    records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['domain_vless']}.{user_data['domain']}"})
    if records:
        cf.zones.dns_records.delete(zone_id, records[0]['id'])
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"          *Hapus Domain Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['domain_vless']}`\n"
        message += f"`Sub    : ``{user_data['domain_vless']}.{user_data['domain']}`\n"
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['domain_vless']}`", parse_mode=telegram.ParseMode.MARKDOWN)
    cf.zones.dns_records.post(zone_id, data=record)
    message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"            *Add Buyer Berhasil*\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"`Buyer   : `@{user_data['domain_vless']}\n"
    message += f"`Name    : ``{user_data['domain_vless']}`\n"
    message += f"`Sub     : ``{user_data['domain_vless']}.{user_data['domain']}`\n"
    message += f"`Server  : ``{user_data['server_vless']}.{user_data['domain']}`\n"
    message += f"`Domain  : ``{user_data['domain']}`\n"
    message += f"`Expired : ``{expiration_formatted}`\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━"        
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
      
    message = f"`{PEMBATAS}`\n"
    message += f"*         Create VLESS Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_vless']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_vless']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Port nTLS*` :` `80`\n"
    message += f"» *Path WS*`  :` `/vless-ws`\n"
    message += f"» *Path GRPC*`:` `vless-grpc`\n"
    message += f" `{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{expiration_formatted}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```vless://{UUID}@{BUGILPED}:443?path=%2Fvless-ws&security=tls&encryption=none&host={user_data['domain_vless']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless']}.{user_data['domain']}#{user_data['domain_vless']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```vless://{UUID}@{BUGVISION}:80?path=%2Fvless-ws&security=none&encryption=none&host={user_data['domain_vless']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless']}.{user_data['domain']}#{user_data['domain_vless']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```vless://{UUID}@{BUGVIDIO}:80?path=%2Fvless-ws&security=none&encryption=none&host={user_data['domain_vless']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless']}.{user_data['domain']}#{user_data['domain_vless']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```vless://{UUID}@{BUGISATEDU}:80?path=%2Fvless-ws&security=none&encryption=none&host={ISATEDU2}.{user_data['domain_vless']}.{user_data['domain']}&type=ws&sni={ISATEDU2}.{user_data['domain_vless']}.{user_data['domain']}#{user_data['domain_vless']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)


def create_trojan(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_trojan'

def wait_domain_trojan(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_subdomain_trojan'
    elif selected_domain == 'cancel':
        return cancel(update, context)    
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_trojan'

def wait_subdomain_trojan(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_trojan'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
   
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain server pribadi :", reply_markup=markup)    
    return 'wait_server_trojan'

def wait_server_trojan(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_trojan'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
        
    reply_keyboard = [['30', '60'], ['90', '/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Expired Hari:", reply_markup=markup)    
    return 'wait_exp_trojan'

def wait_exp_trojan(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_input = update.message.text
    user_data['wait_expired_trojan'] = user_input
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=int(user_data['wait_expired_trojan']))
    expiration_formatted = expiration_date.strftime('%Y-%m-%d')
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['domain_trojan'], 
        'content': f"{user_data['server_trojan']}.{user_data['domain']}",
        'comment': f"{expiration_formatted}", 
    }
    records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['domain_trojan']}.{user_data['domain']}"})
    if records:
        cf.zones.dns_records.delete(zone_id, records[0]['id'])
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"          *Hapus Domain Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['domain_trojan']}`\n"
        message += f"`Sub    : ``{user_data['domain_trojan']}.{user_data['domain']}`\n"
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['domain_trojan']}`", parse_mode=telegram.ParseMode.MARKDOWN)
    cf.zones.dns_records.post(zone_id, data=record)
    message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"            *Add Buyer Berhasil*\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"`Buyer   : `@{user_data['domain_trojan']}\n"
    message += f"`Name    : ``{user_data['domain_trojan']}`\n"
    message += f"`Sub     : ``{user_data['domain_trojan']}.{user_data['domain']}`\n"
    message += f"`Server  : ``{user_data['server_trojan']}.{user_data['domain']}`\n"
    message += f"`Domain  : ``{user_data['domain']}`\n"
    message += f"`Expired : ``{expiration_formatted}`\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━"        
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)        
           
    message = f"`{PEMBATAS}`\n"
    message += f"*           Create Trojan Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_trojan']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_trojan']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Path WS*`  :` `/trojan-ws`\n"
    message += f"» *Path GRPC*`:` `trojan-grpc`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{expiration_formatted}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```trojan://{UUID}@{BUGILPED}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan']}.{user_data['domain']}#{user_data['domain_trojan']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```trojan://{UUID}@{BUGVISION}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan']}.{user_data['domain']}#{user_data['domain_trojan']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```trojan://{UUID}@{BUGVIDIO}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan']}.{user_data['domain']}#{user_data['domain_trojan']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```trojan://{UUID}@{BUGISATEDU}:443?path=%2Ftrojan-ws&security=tls&host={ISATEDU2}.{user_data['domain_trojan']}.{user_data['domain']}&type=ws&sni={ISATEDU2}.{user_data['domain_trojan']}.{user_data['domain']}#{user_data['domain_trojan']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)


def create_vless_trial(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END        
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_vless_trial'

def wait_domain_vless_trial(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()    
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain_vless_trial'
    elif selected_domain == 'cancel':
        return cancel(update, context)   
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_vless_trial'

def wait_subdomain_vless_trial(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_vless_trial'] = update.message.text      
    
    message = f"`{PEMBATAS}`\n"
    message += f"*        Trial VLESS Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_vless_trial']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_vless_trial']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Port nTLS*` :` `80`\n"
    message += f"» *Path WS*`  :` `/vless-ws`\n"
    message += f"» *Path GRPC*`:` `vless-grpc`\n"
    message += f" `{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{WAKTU}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```vless://{UUID}@{BUGILPED}:443?path=%2Fvless-ws&security=tls&encryption=none&host={user_data['domain_vless_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless_trial']}.{user_data['domain']}#{user_data['domain_vless_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```vless://{UUID}@{BUGVISION}:80?path=%2Fvless-ws&security=none&encryption=none&host={user_data['domain_vless_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless_trial']}.{user_data['domain']}#{user_data['domain_vless_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```vless://{UUID}@{BUGVIDIO}:80?path=%2Fvless-ws&security=none&encryption=none&host={user_data['domain_vless_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_vless_trial']}.{user_data['domain']}#{user_data['domain_vless_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```vless://{UUID}@{BUGISATEDU}:80?path=%2Fvless-ws&security=none&encryption=none&host={ISATEDU2}.{user_data['domain_vless_trial']}.{user_data['domain']}&type=ws&sni={ISATEDU2}.{user_data['domain_vless_trial']}.{user_data['domain']}#{user_data['domain_vless_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)


def create_trojan_trial(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END        
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_trojan_trial'

def wait_domain_trojan_trial(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain_trojan_trial'
    elif selected_domain == 'cancel':
        return cancel(update, context)    
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_trojan_trial'

def wait_subdomain_trojan_trial(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_trojan_trial'] = update.message.text
             
    message = f"`{PEMBATAS}`\n"
    message += f"*          Trial Trojan Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_trojan_trial']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_trojan_trial']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Path WS*`  :` `/trojan-ws`\n"
    message += f"» *Path GRPC*`:` `trojan-grpc`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{WAKTU}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```trojan://{UUID}@{BUGILPED}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan_trial']}.{user_data['domain']}#{user_data['domain_trojan_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```trojan://{UUID}@{BUGVISION}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan_trial']}.{user_data['domain']}#{user_data['domain_trojan_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```trojan://{UUID}@{BUGVIDIO}:443?path=%2Ftrojan-ws&security=tls&host={user_data['domain_trojan_trial']}.{user_data['domain']}&type=ws&sni={user_data['domain_trojan_trial']}.{user_data['domain']}#{user_data['domain_trojan_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```trojan://{UUID}@{BUGISATEDU}:443?path=%2Ftrojan-ws&security=tls&host={ISATEDU2}.{user_data['domain_trojan_trial']}.{user_data['domain']}&type=ws&sni={ISATEDU2}.{user_data['domain_trojan_trial']}.{user_data['domain']}#{user_data['domain_trojan_trial']}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)

    
def get_ip_info(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END
    
    try:
        address = context.args[0]
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
            context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
            return cancel(update, context)
        else:
            update.message.reply_text("Gagal mendapatkan informasi IP")
            return cancel(update, context)
    
    except IndexError:
        update.message.reply_text("Gunakan perintah /ip_info domain/ip")
        return cancel(update, context)
    except socket.gaierror:
        update.message.reply_text("Domain atau IP tidak ditemukan")
        return cancel(update, context)
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")
        return cancel(update, context)

    
def list_subdomains(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Pilih domain untuk melihat subdomain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_list_domain'

def wait_list_domain(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_list_domain'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}    
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)    
    if user_ips[user_id]['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_ips[user_id]['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_ips[user_id]['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_ips[user_id]['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    try:        
        records = cf.zones.dns_records.get(zone_id)        
        subdomains = [f"Subdomain : {record['name']}\nServer          : {record['content']}\nExpired        : {record['comment']}" for record in records if record['type'] == 'CNAME']
        if subdomains:
            subdomains_list = "\n\n".join(subdomains)
            # Create a temporary file to store the subdomain list
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(subdomains_list)
            # Send the temporary file as a document
            context.bot.send_document(chat_id=user_id, document=open(temp_file.name, 'rb'), filename=f"{user_ips[user_id]['domain']}_cname.txt")
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak ada subdomain cname pada `{user_ips[user_id]['domain']}`", parse_mode=telegram.ParseMode.MARKDOWN)                        
        subdomains2 = [f"Domain : {record['name']}\nIP            : {record['content']}" for record in records if record['type'] == 'A']
        if subdomains2:
            subdomains_list2 = "\n\n".join(subdomains2)
            # Create a temporary file to store the subdomain list
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file2:
                temp_file2.write(subdomains_list2)
            # Send the temporary file as a document
            context.bot.send_document(chat_id=user_id, document=open(temp_file2.name, 'rb'), filename=f"{user_ips[user_id]['domain']}_A.txt")
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak ada subdomain a pada `{user_ips[user_id]['domain']}`", parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error retrieving DNS records: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat mengambil rekaman DNS. Silakan coba lagi.")
    finally:
        del user_ips[user_id]
        return cancel(update, context)
    
def ping_domain(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return
    domain_to_ping = context.args[0] if context.args else None
    if not domain_to_ping:
        context.bot.send_message(chat_id=user_id, text="Gunakan perintah /ping domain/ip")
        return cancel(update, context)
        return
    try:
        ping_command = f"ping -c 1 {domain_to_ping} | grep -o 'time=[0-9.]*' | cut -d'=' -f2"
        result = subprocess.run(ping_command, shell=True, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            response = f"ping `{domain_to_ping}` berhasil : {result.stdout.strip()} ms"
        else:
            response = f"ping `{domain_to_ping}` gagal :\n```\n{result.stderr.strip()}```"        
        context.bot.send_message(chat_id=user_id, text=response, parse_mode=telegram.ParseMode.MARKDOWN)
    except subprocess.TimeoutExpired as e:
        context.bot.send_message(chat_id=user_id, text=f"ping `{domain_to_ping}` gagal", parse_mode=telegram.ParseMode.MARKDOWN)
        return cancel(update, context)
    except subprocess.CalledProcessError as e:
        context.bot.send_message(chat_id=user_id, text=f"ping `{domain_to_ping}` gagal : `{e.stderr.strip()}`", parse_mode=telegram.ParseMode.MARKDOWN)
        return cancel(update, context)
    except Exception as e:
        context.bot.send_message(chat_id=user_id, text=f"Terjadi kesalahan saat menjalankan ping : `{e}`", parse_mode=telegram.ParseMode.MARKDOWN)
        return cancel(update, context)
    return cancel(update, context) 



def create_vmess(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_vmess'

def wait_domain_vmess(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_subdomain_vmess'
    elif selected_domain == 'cancel':
        return cancel(update, context)    
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_vmess'

def wait_subdomain_vmess(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_vmess'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
        
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain server pribadi :", reply_markup=markup)    
    return 'wait_server_vmess'

def wait_server_vmess(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['server_vmess'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
      
    reply_keyboard = [['30', '60'], ['90', '/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Expired Hari:", reply_markup=markup)    
    return 'wait_exp_vmess'

def wait_exp_vmess(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_input = update.message.text
    user_data['wait_expired_vmess'] = user_input
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=int(user_data['wait_expired_vmess']))

    expiration_formatted = expiration_date.strftime('%Y-%m-%d')
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
    record = {
        'type': 'CNAME',
        'name': user_data['domain_vmess'], 
        'content': f"{user_data['server_vmess']}.{user_data['domain']}",
        'comment': f"{expiration_formatted}", 
    }
    records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['domain_vmess']}.{user_data['domain']}"})
    if records:
        cf.zones.dns_records.delete(zone_id, records[0]['id'])
        message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"          *Hapus Domain Berhasil*\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"`Name   : ``{user_data['domain_vmess']}`\n"
        message += f"`Sub    : ``{user_data['domain_vmess']}.{user_data['domain']}`\n"
        message += f"`Domain : ``{user_data['domain']}`\n"
        message += f"━━━━━━━━━━━━━━━━━━━━━━"
        context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['domain_vmess']}`", parse_mode=telegram.ParseMode.MARKDOWN)
    cf.zones.dns_records.post(zone_id, data=record)
    message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"            *Add Buyer Berhasil*\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"`Buyer   : `@{user_data['domain_vmess']}\n"
    message += f"`Name    : ``{user_data['domain_vmess']}`\n"
    message += f"`Sub     : ``{user_data['domain_vmess']}.{user_data['domain']}`\n"
    message += f"`Server  : ``{user_data['server_vmess']}.{user_data['domain']}`\n"
    message += f"`Domain  : ``{user_data['domain']}`\n"
    message += f"`Expired : ``{expiration_formatted}`\n"
    message += f"━━━━━━━━━━━━━━━━━━━━━━"        
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    	
    ilped = {
        "v": "2",
        "ps": f"{user_data['domain_vmess']} TLS",
        "add": f"{BUGILPED}",
        "port": "443",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "tls": "tls"
    }

    vidio = {
        "v": "2",
        "ps": f"{user_data['domain_vmess']} nTLS",
        "add": f"{BUGVIDIO}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "tls": "none"
    }

    vision = {
        "v": "2",
        "ps": f"{user_data['domain_vmess']} nTLS",
        "add": f"{BUGVISION}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess']}.{user_data['domain']}",
        "tls": "none"
    }

    isatedu = {
        "v": "2",
        "ps": f"{user_data['domain_vmess']} nTLS",
        "add": f"{BUGISATEDU}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{ISATEDU2}.{user_data['domain_vmess']}.{user_data['domain']}",
        "sni": f"{ISATEDU2}.{user_data['domain_vmess']}.{user_data['domain']}",
        "tls": "none"
    }
    
    json_string = json.dumps(ilped, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_ilped = f"vmess://{base64_data}"
    
    json_string = json.dumps(vidio, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_vidio = f"vmess://{base64_data}"
    
    json_string = json.dumps(vision, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_vision = f"vmess://{base64_data}"
    
    json_string = json.dumps(isatedu, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_isatedu = f"vmess://{base64_data}"

    message = f"`{PEMBATAS}`\n"
    message += f"*         Create Vmess Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_vmess']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_vmess']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Port nTLS*` :` `80`\n"
    message += f"» *Path WS*`  :` `/vmess`\n"
    message += f"» *Path GRPC*`:` `vmess-grpc`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{expiration_formatted}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```{message_text_ilped}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```{message_text_vision}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```{message_text_vidio}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```{message_text_isatedu}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)    

def create_vmess_trial(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END    
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)    
    return 'wait_domain_vmess_trial'

def wait_domain_vmess_trial(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_subdomain_vmess_trial'
    elif selected_domain == 'cancel':
        return cancel(update, context)    
    user_ips[user_id] = {'domain': selected_domain}    
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Subdomain pelanggan :", reply_markup=markup)    
    return 'wait_subdomain_vmess_trial'


def wait_subdomain_vmess_trial(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['domain_vmess_trial'] = update.message.text
    ilped = {
        "v": "2",
        "ps": f"{user_data['domain_vmess_trial']} TLS",
        "add": f"{BUGILPED}",
        "port": "443",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "tls": "tls"
    }

    vidio = {
        "v": "2",
        "ps": f"{user_data['domain_vmess_trial']} nTLS",
        "add": f"{BUGVIDIO}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "tls": "none"
    }

    vision = {
        "v": "2",
        "ps": f"{user_data['domain_vmess_trial']} nTLS",
        "add": f"{BUGVISION}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "sni": f"{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "tls": "none"
    }

    isatedu = {
        "v": "2",
        "ps": f"{user_data['domain_vmess_trial']} nTLS",
        "add": f"{BUGISATEDU}",
        "port": "80",
        "id": f"{UUID}",
        "aid": "0",
        "net": "ws",
        "path": "/vmess",
        "type": "none",
        "host": f"{ISATEDU2}.{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "sni": f"{ISATEDU2}.{user_data['domain_vmess_trial']}.{user_data['domain']}",
        "tls": "none"
    }
    
    json_string = json.dumps(ilped, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_ilped = f"vmess://{base64_data}"
    
    json_string = json.dumps(vidio, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_vidio = f"vmess://{base64_data}"
    
    json_string = json.dumps(vision, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_vision = f"vmess://{base64_data}"
    
    json_string = json.dumps(isatedu, indent=2)
    base64_data = base64.b64encode(json_string.encode()).decode()
    message_text_isatedu = f"vmess://{base64_data}"

    message = f"`{PEMBATAS}`\n"
    message += f"*        Trial Vmess Success*\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Domain*`   :` `{user_data['domain_vmess_trial']}.{user_data['domain']}`\n"
    message += f"» *Username*` :` `{user_data['domain_vmess_trial']}`\n"
    message += f"» *UUID*`     :` `{UUID}`\n"
    message += f"» *Port TLS*`  :` `443`\n"
    message += f"» *Port nTLS*` :` `80`\n"
    message += f"» *Path WS*`  :` `/vmess`\n"
    message += f"» *Path GRPC*`:` `vmess-grpc`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *Expired*`   :` `{WAKTU}`\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *TELKOMSEL ILMUPEDIA :*\n"
    message += f"```{message_text_ilped}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VISION+ :*\n"
    message += f"```{message_text_vision}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *XL VIDIO :*\n"
    message += f"```{message_text_vidio}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *INDOSAT EDUKASI :*\n"
    message += f"```{message_text_isatedu}```\n"
    message += f"`{PEMBATAS}`\n"
    message += f"» *CARA IMPORT KONFIG :* \n"
    message += f"» *HTTP INJECTOR :* *{TUTORHI}*\n"
    message += f"» *HTTP CUSTOM :* *{TUTORHC}*\n"
    message += f"» *V2rayNG :* *{TUTORVNG}*\n"
    message += f"`{PEMBATAS}`"
    context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    return cancel(update, context)

    
# Function to decode base64 message
def decode_base64(encoded_text):
    try:
        # Decode base64 message
        decoded_message = base64.b64decode(encoded_text).decode('utf-8')
        return decoded_message
    except Exception as e:
        return None
    
# Function to handle normal messages
def handle_message(update, context):
    user_id = update.message.from_user.id    
    if user_id not in CHAT_ID:
        
        return ConversationHandler.END    
    message_text = update.message.text

    # Check if the message starts with "vmess://"
    if message_text.startswith("vmess://"):
        # Find the position of ": //"
        start_index = message_text.find("://")
        # Extract the substring after ": //"
        encoded_text = message_text[start_index + 3:]

        # Decode base64 message
        decoded_message = base64.b64decode(encoded_text).decode('utf-8')

        if decoded_message:
            try:
                # Parse JSON message
                json_data = json.loads(decoded_message)
                
                # Determine the value of tls
                tls_value = 'false' if json_data['tls'] in ['none', ''] else 'true'
                service_value = f"path: {json_data['path']}\n      headers:\n        Host: {json_data['host']}" if json_data['net'] == "ws" else f"grpc-service-name: {json_data['path']}"
                servername_value = json_data['host'] if 'sni' not in json_data or json_data['sni'] == '' else json_data['sni']

                
                # Construct the response message for vmess
                response_message = f'''port: 7890
socks-port: 7891
redir-port: 7892
mixed-port: 7893
tproxy-port: 7895
ipv6: false
mode: rule
log-level: silent
allow-lan: true
external-controller: 0.0.0.0:9090
secret: ""
bind-address: "*"
unified-delay: true
profile:
  store-selected: true
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  listen: 0.0.0.0:7874
  nameserver:
    - 8.8.8.8
    - 1.0.0.1
    - https://dns.google/dns-query
  fallback:
    - 1.1.1.1
    - 8.8.4.4
    - https://cloudflare-dns.com/dns-query
    - 112.215.203.254
  default-nameserver:
    - 8.8.8.8
    - 1.1.1.1
    - 112.215.203.254
proxies:                
  - name: {json_data['ps']}
    server: {json_data['add']}
    port: {json_data['port']}
    type: vmess
    uuid: {json_data['id']}
    alterId: {json_data['aid']}
    cipher: auto
    tls: {tls_value}
    skip-cert-verify: true
    servername: {servername_value}
    network: {json_data['net']}
    {json_data['net']}-opts:
      {service_value}
    udp: true
proxy-groups:
  - name: telegram @efwangstore
    type: fallback
    proxies:
      - {json_data['ps']}
    url: http://cp.cloudflare.com/generate_204
    interval: '5'
rules:
  - MATCH,telegram @efwangstore'''

                # Write response_message to a temporary file
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                    temp_file.write(response_message)

                # Send the temporary file as a document
                context.bot.send_document(chat_id=update.message.chat_id, document=open(temp_file.name, 'rb'), filename=f"{json_data['ps']}.yaml")
                return cancel(update, context)

            except Exception as e:
                update.message.reply_text('Gagal mendekode atau mengonversi pesan vmess. Pastikan teks yang Anda kirim adalah dalam format base64 dan berisi data JSON yang valid.')

    # Check if the message starts with "vless://"
    elif message_text.startswith("vless://"):
        try:
            # Extracting data from vless URL
            parsed_url = urllib.parse.urlparse(message_text)
            name = (lambda fragment: fragment.split('#')[-1] if fragment else '')(parsed_url.fragment)
            server = parsed_url.netloc.split('@')[1].split(':')[0] if '@' in parsed_url.netloc else ''            
            port = parsed_url.netloc.split(':')[1].split('?')[0] if ':' in parsed_url.netloc else ''
            id = parsed_url.netloc.split('@')[0] if '@' in parsed_url.netloc else ''
            servername = urllib.parse.parse_qs(parsed_url.query).get('sni', [''])[0]
            network = urllib.parse.parse_qs(parsed_url.query).get('type', [''])[0]
            path = urllib.parse.parse_qs(parsed_url.query).get('path', [''])[0]
            path_grpc = urllib.parse.parse_qs(parsed_url.query).get('serviceName', [''])[0]
            host = urllib.parse.parse_qs(parsed_url.query).get('host', [''])[0]

            # Determine the value of tls based on the port in the URL
            tls_value = port == '443'
            service_value = f"path: {path}\n      headers:\n        Host: {host}" if f"{network}" == "ws" else f"grpc-service-name: {path_grpc}"

            # Construct the response message for vless
            response_message = f'''port: 7890
socks-port: 7891
redir-port: 7892
mixed-port: 7893
tproxy-port: 7895
ipv6: false
mode: rule
log-level: silent
allow-lan: true
external-controller: 0.0.0.0:9090
secret: ""
bind-address: "*"
unified-delay: true
profile:
  store-selected: true
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  listen: 0.0.0.0:7874
  nameserver:
    - 8.8.8.8
    - 1.0.0.1
    - https://dns.google/dns-query
  fallback:
    - 1.1.1.1
    - 8.8.4.4
    - https://cloudflare-dns.com/dns-query
    - 112.215.203.254
  default-nameserver:
    - 8.8.8.8
    - 1.1.1.1
    - 112.215.203.254
proxies:     
  - name: {name}
    server: {server}
    port: {port}
    type: vless
    uuid: {id}
    cipher: auto
    tls: {str(tls_value).lower()}
    skip-cert-verify: true
    servername: {servername}
    network: {network}
    {network}-opts:
      {service_value}
    udp: true
proxy-groups:
  - name: telegram @efwangstore
    type: fallback
    proxies:
      - {name}
    url: http://cp.cloudflare.com/generate_204
    interval: '5'
rules:
  - MATCH,telegram @efwangstore'''
  
                # Write response_message to a temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(response_message)

                # Send the temporary file as a document
            context.bot.send_document(chat_id=update.message.chat_id, document=open(temp_file.name, 'rb'), filename=f"{name}.yaml")
            return cancel(update, context)

        except Exception as e:
            update.message.reply_text('Gagal mengurai pesan vless. Pastikan format URL yang Anda kirim benar dan mengandung data yang diperlukan.')

    elif message_text.startswith("trojan://"):
        try:
            # Extracting data from vless URL
            parsed_url = urllib.parse.urlparse(message_text)
            name = (lambda fragment: fragment.split('#')[-1] if fragment else '')(parsed_url.fragment)
            server = parsed_url.netloc.split('@')[1].split(':')[0] if '@' in parsed_url.netloc else ''
            id = parsed_url.netloc.split('@')[0] if '@' in parsed_url.netloc else ''
            servername = urllib.parse.parse_qs(parsed_url.query).get('sni', [''])[0]
            network = urllib.parse.parse_qs(parsed_url.query).get('type', [''])[0]
            port = parsed_url.netloc.split(':')[1].split('?')[0] if ':' in parsed_url.netloc else ''
            path = urllib.parse.parse_qs(parsed_url.query).get('path', [''])[0]
            path_grpc = urllib.parse.parse_qs(parsed_url.query).get('serviceName', [''])[0]
            host = urllib.parse.parse_qs(parsed_url.query).get('host', [''])[0]
            
            service_value = f"path: {path}\n      headers:\n        Host: {host}" if f"{network}" == "ws" else f"grpc-service-name: {path_grpc}"

            # Construct the response message for vless
            response_message = f'''port: 7890
socks-port: 7891
redir-port: 7892
mixed-port: 7893
tproxy-port: 7895
ipv6: false
mode: rule
log-level: silent
allow-lan: true
external-controller: 0.0.0.0:9090
secret: ""
bind-address: "*"
unified-delay: true
profile:
  store-selected: true
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  listen: 0.0.0.0:7874
  nameserver:
    - 8.8.8.8
    - 1.0.0.1
    - https://dns.google/dns-query
  fallback:
    - 1.1.1.1
    - 8.8.4.4
    - https://cloudflare-dns.com/dns-query
    - 112.215.203.254
  default-nameserver:
    - 8.8.8.8
    - 1.1.1.1
    - 112.215.203.254
proxies:     
  - name: {name}
    server: {server}
    port: {port}
    type: trojan
    password: {id}
    skip-cert-verify: true
    sni: {servername}
    network: {network}
    {network}-opts:
      {service_value}
    udp: true
proxy-groups:
  - name: telegram @efwangstore
    type: select
    proxies:
      - {name}
rules:
  - MATCH,telegram @efwangstore'''
  
                # Write response_message to a temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(response_message)

                # Send the temporary file as a document
            context.bot.send_document(chat_id=update.message.chat_id, document=open(temp_file.name, 'rb'), filename=f"{name}.yaml")
            return cancel(update, context)

        except Exception as e:
            update.message.reply_text('Gagal mengurai pesan trojan. Pastikan format URL yang Anda kirim benar dan mengandung data yang diperlukan.')
    else:
        return ConversationHandler.END
        
# Fungsi untuk menjalankan delete_sgtrial
def delete_sgtrial_auto():
    user_id = CHAT_ID  # Ganti dengan CHAT_ID yang benar
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    try:
        # Hapus subdomain SGTRIAL
        records_sgtrial = cf.zones.dns_records.get(ZONEID1, params={'name': f"{SGTRIAL}.{DOMAIN1}"})
        if records_sgtrial:
            cf.zones.dns_records.delete(ZONEID1, records_sgtrial[0]['id'])
            
        else:
            return None
    except Exception as e:
        print(f"Error deleting DNS record: {e}")
        
        
def delete_idtrial_auto():
    user_id = CHAT_ID  # Ganti dengan CHAT_ID yang benar
    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    try:
        # Hapus subdomain IDTRIAL
        records_idtrial = cf.zones.dns_records.get(ZONEID1, params={'name': f"{IDTRIAL}.{DOMAIN1}"})
        if records_idtrial:
            cf.zones.dns_records.delete(ZONEID1, records_idtrial[0]['id'])
            
        else:
            return None
    except Exception as e:
        print(f"Error deleting DNS record: {e}")

def renew(update, context):
    user_id = update.message.from_user.id
    if user_id not in CHAT_ID:
        context.bot.send_message(chat_id=user_id, text="Anda tidak diizinkan menggunakan bot ini.")
        return ConversationHandler.END  
    reply_keyboard = [[DOMAIN1, DOMAIN2], [DOMAIN3, DOMAIN4], ['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text=f"Pilih domain:", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return 'wait_domain_renew'

def wait_domain_renew(update, context):
    user_id = update.message.from_user.id
    selected_domain = update.message.text.lower()
    if selected_domain not in [DOMAIN1, DOMAIN2, DOMAIN3, DOMAIN4, 'cancel']:
        context.bot.send_message(chat_id=user_id, text="Pilihan domain tidak valid. Silakan pilih domain yang benar.")
        return 'wait_domain_renew'
    elif selected_domain == 'cancel':
        return cancel(update, context)
    user_ips[user_id] = {'domain': selected_domain}
    reply_keyboard = [['/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input subdomain :", reply_markup=markup)
    return 'wait_subdomain_renew'
 

def wait_subdomain_renew(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_data['subdomain'] = update.message.text
    if 'domain' not in user_data:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)
        
    reply_keyboard = [['30', '60'], ['90', '/cancel']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id=user_id, text="Input Expired Hari:", reply_markup=markup)    
    return 'wait_comment'

def wait_comment(update, context):
    user_id = update.message.from_user.id
    user_data = user_ips[user_id]
    user_input = update.message.text
    
    # Memeriksa apakah input adalah angka yang valid
    try:
        expiration_days = int(user_input)
    except ValueError:
        context.bot.send_message(chat_id=user_id, text="Masukan tidak valid. Mohon masukkan angka yang valid.")
        return 'wait_comment'

    cf = CloudFlare(email=CLOUDFLARE_EMAIL, token=CLOUDFLARE_API_KEY)
    if user_data['domain'] == DOMAIN1:
        zone_id = ZONEID1
    elif user_data['domain'] == DOMAIN2:
        zone_id = ZONEID2
    elif user_data['domain'] == DOMAIN3:
        zone_id = ZONEID3
    elif user_data['domain'] == DOMAIN4:
        zone_id = ZONEID4
    else:
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan. Silakan coba lagi.")
        return cancel(update, context)

    try:
        # Dapatkan rekaman DNS yang sesuai dengan subdomain dan domain yang ditentukan
        records = cf.zones.dns_records.get(zone_id, params={'name': f"{user_data['subdomain']}.{user_data['domain']}"})
        if records:       
            record_id = records[0]['id']
            # Ambil waktu dari komentar sebagai tanggal kedaluwarsa
            expiration_date = datetime.datetime.strptime(records[0]['comment'], '%Y-%m-%d')
            # Hitung tanggal kedaluwarsa yang baru
            new_expiration_date = expiration_date + datetime.timedelta(days=expiration_days)
            expiration_formatted = new_expiration_date.strftime('%Y-%m-%d')

            record_data = {
                'name': records[0]['name'],
                'type': records[0]['type'],
                'content': records[0]['content'],
                'ttl': records[0]['ttl'],
                'proxied': records[0]['proxied'],
                'comment': f"{expiration_formatted}",  # Perbarui komentar
            }
            cf.zones.dns_records.put(zone_id, record_id, data=record_data)  # Perbarui rekaman dengan komentar baru
            message = f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"                *Renew Berhasil*\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"`User    : ``{user_data['subdomain']}`\n"
            message += f"`Domain  : ``{user_data['subdomain']}.{user_data['domain']}`\n"
            message += f"`Extend  : ``{user_input} Hari`\n"
            message += f"`Expired : ``{expiration_formatted}`\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━"            
            context.bot.send_message(chat_id=user_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=user_id, text=f"Tidak dapat menemukan subdomain `{user_data['subdomain']}`", parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Error updating DNS record: {e}")
        context.bot.send_message(chat_id=user_id, text="Terjadi kesalahan saat memperbarui rekaman DNS. Silakan coba lagi.")
    del user_ips[user_id]
    return cancel(update, context)
    

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add_subdomain', add_subdomain)],
        states={
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
           'wait_subdomain': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain)],
           'wait_ip': [MessageHandler(Filters.text & ~Filters.command, wait_ip)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )   
    conv_handler_delete = ConversationHandler(
    entry_points=[CommandHandler('delete_subdomain', delete_subdomain)],
    states={
        'wait_delete_domain': [MessageHandler(Filters.text & ~Filters.command, wait_delete_domain)],
        'wait_delete_subdomain': [MessageHandler(Filters.text & ~Filters.command, wait_delete_subdomain)],
        'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
      fallbacks=[CommandHandler('cancel', cancel)],
   )   
    conv_handler_cname_pribadi = ConversationHandler(
        entry_points=[CommandHandler('add_cname_pribadi', add_cname_pribadi)],
        states={
           'wait_cname_domain_pribadi': [MessageHandler(Filters.text & ~Filters.command, wait_cname_domain_pribadi)],
           'wait_cname_subdomain_pribadi': [MessageHandler(Filters.text & ~Filters.command, wait_cname_subdomain_pribadi)],
           'wait_server_subdomain_pribadi': [MessageHandler(Filters.text & ~Filters.command, wait_server_subdomain_pribadi)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )   
    conv_handler_cname = ConversationHandler(
        entry_points=[CommandHandler('add_cname_pelanggan', add_cname_pelanggan)],
        states={
           'wait_cname_domain': [MessageHandler(Filters.text & ~Filters.command, wait_cname_domain)],
           'wait_cname_subdomain': [MessageHandler(Filters.text & ~Filters.command, wait_cname_subdomain)],
           'wait_server_subdomain': [MessageHandler(Filters.text & ~Filters.command, wait_server_subdomain)],
           'wait_server_subdomain_expired': [MessageHandler(Filters.text & ~Filters.command, wait_server_subdomain_expired)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )    
    conv_handler_cname_server = ConversationHandler(
        entry_points=[CommandHandler('add_cname_public', add_cname_server)],
        states={
           'wait_cname_domain_server': [MessageHandler(Filters.text & ~Filters.command, wait_cname_domain_server)],
           'wait_cname_subdomain_server': [MessageHandler(Filters.text & ~Filters.command, wait_cname_subdomain_server)],
           'wait_server_subdomain_server': [MessageHandler(Filters.text & ~Filters.command, wait_server_subdomain_server)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )    
    conv_handler_create_vless = ConversationHandler(
        entry_points=[CommandHandler('create_vless', create_vless)],
        states={
           'wait_domain_vless': [MessageHandler(Filters.text & ~Filters.command, wait_domain_vless)],
           'wait_subdomain_vless': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_vless)],
           'wait_server_vless': [MessageHandler(Filters.text & ~Filters.command, wait_server_vless)],
           'wait_exp_vless': [MessageHandler(Filters.text & ~Filters.command, wait_exp_vless)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    ) 
    conv_handler_create_vmess = ConversationHandler(
        entry_points=[CommandHandler('create_vmess', create_vmess)],
        states={
           'wait_domain_vmess': [MessageHandler(Filters.text & ~Filters.command, wait_domain_vmess)],
           'wait_subdomain_vmess': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_vmess)],
           'wait_server_vmess': [MessageHandler(Filters.text & ~Filters.command, wait_server_vmess)],
           'wait_exp_vmess': [MessageHandler(Filters.text & ~Filters.command, wait_exp_vmess)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    ) 
    conv_handler_create_trojan = ConversationHandler(
        entry_points=[CommandHandler('create_trojan', create_trojan)],
        states={
           'wait_domain_trojan': [MessageHandler(Filters.text & ~Filters.command, wait_domain_trojan)],
           'wait_subdomain_trojan': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_trojan)],
           'wait_server_trojan': [MessageHandler(Filters.text & ~Filters.command, wait_server_trojan)],
           'wait_exp_trojan': [MessageHandler(Filters.text & ~Filters.command, wait_exp_trojan)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )    
    conv_handler_create_vless_trial = ConversationHandler(
        entry_points=[CommandHandler('create_vless_trial', create_vless_trial)],
        states={
           'wait_domain_vless_trial': [MessageHandler(Filters.text & ~Filters.command, wait_domain_vless_trial)],
           'wait_subdomain_vless_trial': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_vless_trial)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    ) 
    conv_handler_create_vmess_trial = ConversationHandler(
        entry_points=[CommandHandler('create_vmess_trial', create_vmess_trial)],
        states={
           'wait_domain_vmess_trial': [MessageHandler(Filters.text & ~Filters.command, wait_domain_vmess_trial)],
           'wait_subdomain_vmess_trial': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_vmess_trial)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    ) 
    conv_handler_create_trojan_trial = ConversationHandler(
        entry_points=[CommandHandler('create_trojan_trial', create_trojan_trial)],
        states={
           'wait_domain_trojan_trial': [MessageHandler(Filters.text & ~Filters.command, wait_domain_trojan_trial)],
           'wait_subdomain_trojan_trial': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_trojan_trial)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )  
    conv_handler_list_subdomain = ConversationHandler(
        entry_points=[CommandHandler('list_subdomain', list_subdomains)],
        states={
           'list_subdomains': [MessageHandler(Filters.text & ~Filters.command, list_subdomains)],
           'wait_list_domain': [MessageHandler(Filters.text & ~Filters.command, wait_list_domain)],
           'wait_domain': [MessageHandler(Filters.text & ~Filters.command, wait_domain)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler_renew = ConversationHandler(
        entry_points=[CommandHandler('renew', renew)],
        states={
           'wait_domain_renew': [MessageHandler(Filters.text & ~Filters.command, wait_domain_renew)],
           'wait_subdomain_renew': [MessageHandler(Filters.text & ~Filters.command, wait_subdomain_renew)],
           'wait_comment': [MessageHandler(Filters.text & ~Filters.command, wait_comment)],
      },
        fallbacks=[CommandHandler('cancel', cancel)],
    )   
    dp.add_handler(conv_handler)
    dp.add_handler(conv_handler_delete)
    dp.add_handler(conv_handler_cname_pribadi) 
    dp.add_handler(conv_handler_cname) 
    dp.add_handler(conv_handler_cname_server)
    dp.add_handler(conv_handler_create_vless)
    dp.add_handler(conv_handler_create_vmess)
    dp.add_handler(conv_handler_create_trojan)
    dp.add_handler(conv_handler_create_vless_trial)
    dp.add_handler(conv_handler_create_vmess_trial)
    dp.add_handler(conv_handler_create_trojan_trial)    
    dp.add_handler(conv_handler_list_subdomain)
    dp.add_handler(conv_handler_renew)
    dp.add_handler(CommandHandler('scan', scan))
    dp.add_handler(CommandHandler('menu', cancel))
    dp.add_handler(CommandHandler('start', cancel))
    dp.add_handler(CommandHandler('ip_info', get_ip_info, pass_args=True))
    dp.add_handler(CommandHandler('ping', ping_domain, pass_args=True))
    dp.add_handler(CommandHandler('delete_sgtrial', delete_sgtrial))
    dp.add_handler(CommandHandler('delete_idtrial', delete_idtrial))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    delete_sgtrial_auto()
    delete_idtrial_auto() 
    updater.start_polling()
    updater.idle()
              
if __name__ == '__main__':
    main()
