#!/bin/bash
TOKEN_BOT=$(awk -F'=' '/TELEGRAM_TOKEN/ {gsub(/[[:space:]]+/, "", $2); gsub(/["'"'"']/,"",$2); print $2; exit}' /root/bot.py) 
CHAT_IDS=$(awk -F'[][]' '/CHAT_ID/{print $2}' /root/bot.py)
FILE_PATH="/root/List-IP-TOMKET.txt"
API_URL="https://api.telegram.org/bot$TOKEN_BOT/sendDocument" 
rm tomket.txt
wget -O tomket.txt https://raw.githubusercontent.com/Tomketstore/izin/main/ip
while read -r line; do
    url=$(echo "$line" | awk '{print $4}')
    exp=$(echo "$line" | awk '{print $3}')
    if curl -s -m 1 -I "$url" | grep -q "Switching Protocols"; then
        # Dapatkan data ISP, City, dan Country
        info=$(curl -s "http://ip-api.com/json/$url")
        isp=$(echo "$info" | jq -r '.isp')
        city=$(echo "$info" | jq -r '.city')
        country=$(echo "$info" | jq -r '.country')

        # Tentukan apakah city dan country sama atau berbeda
        if [ "$city" == "$country" ]; then
            location="$city"
        else
            location="$city/$country"
        fi

        printf "%-15s | %s | %s | %s\n" "$url" "$isp" "$location" "$exp"
    fi
done < tomket.txt > List-IP-TOMKET.txt

CAPTION=$(date +"%Y-%m-%d %H:%M:%S")

KEYBOARD='{"inline_keyboard":[[{"text":"Menu","callback_data":"cancel"}]]}'

for CHAT_ID in ${CHAT_IDS//,/ }; do
    echo "Sending document to chat ID: $CHAT_ID" 
    RESPONSE=$(curl -s -F "chat_id=$CHAT_ID" -F "document=@$FILE_PATH" -F "caption=$CAPTION" -F "reply_markup=$KEYBOARD" $API_URL) 
    echo "Response: $RESPONSE"
done
