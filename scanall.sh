#!/bin/bash

# Mendapatkan TOKEN_BOT dan CHAT_IDS dari file bot.py
TOKEN_BOT=$(awk -F'=' '/TELEGRAM_TOKEN/ {gsub(/[[:space:]]+/, "", $2); gsub(/["'"'"']/,"",$2); print $2; exit}' /root/bot.py) 
CHAT_IDS=$(awk -F'[][]' '/CHAT_ID/{print $2}' /root/bot.py)

# Path file output
FILE_PATH="/root/List-IP-ALL.txt"

# API URL Telegram
API_URL="https://api.telegram.org/bot$TOKEN_BOT/sendDocument" 

# Hapus file all.txt sebelumnya jika ada
rm all.txt

# Mendownload data dari berbagai sumber
wget -O all.txt arisctunnel.xyz/ip-script
wget -O - https://raw.githubusercontent.com/wggly/izin/main/ipvps >> all.txt
wget -O - https://raw.githubusercontent.com/Tomketstore/izin/main/ip >> all.txt
wget -O - https://raw.githubusercontent.com/bmayu1/izin/main/ip >> all.txt
wget -O - https://raw.githubusercontent.com/BmyVpn/bumiayuvpn/main/izin >> all.txt

# Debugging: Cek isi all.txt
echo "Isi file all.txt:"
cat all.txt

# Memproses setiap baris di all.txt
while read -r line; do
    # Mendapatkan URL dan tanggal kadaluarsa dari kolom yang tepat
    url=$(echo "$line" | awk '{print $4}')
    exp=$(echo "$line" | awk '{print $3}')
    
    # Debugging: Cetak URL dan exp
    echo "Processing URL: $url with expiration date: $exp"
    
    # Mengecek apakah URL valid
    if curl -s -m 1 -I "$url" | grep -q "Switching Protocols"; then
        # Mengambil informasi ISP, kota, dan negara dari API
        info=$(curl -s "http://ip-api.com/json/$url" | jq -r '"\(.isp) | \(.city) | \(.country)"')
        # Menulis hasil ke file List-IP-ALL.txt
        printf "%-15s | %s | %s\n" "$url" "$info" "$exp" >> List-IP-ALL.txt
    else
        # Jika URL tidak valid, simpan dalam log
        echo "Invalid URL: $url" >> error.log
    fi
done < all.txt

# Debugging: Cek isi file output
echo "Isi file List-IP-ALL.txt:"
cat List-IP-ALL.txt

# Mendapatkan tanggal dan waktu saat ini
CAPTION=$(date +"%Y-%m-%d %H:%M:%S")

# Keyboard inline untuk Telegram
KEYBOARD='{"inline_keyboard":[[{"text":"Menu","callback_data":"cancel"}]]}'

# Mengirim file ke semua chat_id yang terdaftar
for CHAT_ID in ${CHAT_IDS//,/ }; do
    echo "Sending document to chat ID: $CHAT_ID"
    RESPONSE=$(curl -s -F "chat_id=$CHAT_ID" -F "document=@$FILE_PATH" -F "caption=$CAPTION" -F "reply_markup=$KEYBOARD" $API_URL)
    echo "Response: $RESPONSE"
done
