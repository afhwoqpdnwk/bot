#!/bin/bash
TOKEN_BOT="7180943695:AAHdjI562H8aMRwhcbco9VJ5hzYRARcbzdM" 
CHAT_ID="5066246825"
FILE_PATH="/root/List-IP-FT.txt" 
API_URL="https://api.telegram.org/bot$TOKEN_BOT/sendDocument"
CAPTION=$(date +"%Y-%m-%d %H:%M:%S")
rm ip.txt
wget -O ip.txt https://ip.yha.my.id/ip 
grep -Eo "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" ip.txt > List-IP-FT.txt
curl -s -F chat_id=$CHAT_ID -F document=@$FILE_PATH -F caption="$CAPTION" $API_URL
