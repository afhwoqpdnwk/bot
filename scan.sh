#!/bin/bash
TOKEN_BOT=$(awk -F'=' '/TELEGRAM_TOKEN/ {gsub(/[[:space:]]+/, "", $2); gsub(/["'"'"']/,"",$2); print $2; exit}' /root/bot.py) 
CHAT_IDS=$(awk -F'[][]' '/CHAT_ID/{print $2}' /root/bot.py)
FILE_PATH="/root/List-IP-FT.txt"
API_URL="https://api.telegram.org/bot$TOKEN_BOT/sendDocument" 
CAPTION=$(date +"%Y-%m-%d %H:%M:%S")
rm ip.txt
wget -O ip.txt https://ip.yha.my.id/ip
while read -r line; do
    url=$(echo "$line" | awk '{print $4}')
    exp=$(echo "$line" | awk '{print $3}')
    if curl -s -m 1 -I "$url" | grep -q "Switching Protocol"; then
        info=$(curl -s "http://ip-api.com/json/$url" | jq -r '"\(.isp) | \(.city) | \(.country)"')
        printf "%-15s | %s | %s\n" "$url" "$info" "$exp"
    fi
done < ip.txt > List-IP-FT.txt
for CHAT_ID in ${CHAT_IDS//,/ }; do
    echo "Sending document to chat ID: $CHAT_ID" RESPONSE=$(curl -s -F "chat_id=$CHAT_ID" -F "document=@$FILE_PATH" -F "caption=$CAPTION" $API_URL) echo "Response: $RESPONSE"
done

