#!/bin/bash
TOKEN_BOT=$(sed -n "22s/.*TELEGRAM_TOKEN *= *['\"]\([^'\"]*\)['\"].*/\1/p" /root/bot.py) 
CHAT_IDS=$(awk -F'[][]' '/CHAT_ID/{print $2}' /root/bot.py)
FILE_PATH="/root/List-IP-FT.txt"
API_URL="https://api.telegram.org/bot$TOKEN_BOT/sendDocument" 
CAPTION=$(date +"%Y-%m-%d %H:%M:%S")
rm ip.txt
wget -O ip.txt https://ip.yha.my.id/ip
grep -Eo "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" ip.txt >List-IP-FT.txt
for CHAT_ID in ${CHAT_IDS//,/ }; do
    echo "Sending document to chat ID: $CHAT_ID" RESPONSE=$(curl -s -F "chat_id=$CHAT_ID" -F "document=@$FILE_PATH" -F "caption=$CAPTION" $API_URL) echo "Response: $RESPONSE"
done
