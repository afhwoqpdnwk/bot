from telethon import TelegramClient, events
from telethon.tl.types import InputBotInlineResult, InputBotInlineMessageText, DocumentAttributeFilename

# API ID dan API Hash Anda dari Telegram
api_id = '6'
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
bot_token = '7097508990:AAEWQdanPLIBD0biXuJIG5x2PlvytV4e8IA'

# Membuat klien bot
client = TelegramClient('tes', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.InlineQuery)
async def inline_handler(event):
    if event.text.strip() == 'start':
        query = event.text

        # Membuat hasil inline
        results = [
            InputBotInlineResult(
                id='1',
                type='article',
                title='Result 1',
                description='This is the first result for query: {}'.format(query),
                message=InputBotInlineMessageText(message='Halo! Anda memulai bot ini.')
            )
        ]

        # Mengirim hasil inline
        await event.answer(results, cache_time=1)

print("Bot is running...")
client.run_until_disconnected()
