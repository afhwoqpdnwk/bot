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
    query = event.text

    # Membuat hasil inline
    results = [
        InputBotInlineResult(
            id='1',
            type='document',
            title='Result 1',
            description='This is the first result for query: {}'.format(query),
            document='https://example.com/document.pdf',
            attributes=[
                DocumentAttributeFilename('document.pdf')
            ],
            send_message=InputBotInlineMessageText(message='You selected result 1 for query: {}'.format(query))
        ),
        InputBotInlineResult(
            id='2',
            type='document',
            title='Result 2',
            description='This is the second result for query: {}'.format(query),
            document='https://example.com/document2.pdf',
            attributes=[
                DocumentAttributeFilename('document2.pdf')
            ],
            send_message=InputBotInlineMessageText(message='You selected result 2 for query: {}'.format(query))
        )
    ]

    # Mengirim hasil inline
    await event.answer(results, cache_time=1, switch_pm_text='Go to bot', switch_pm_parameter='start')

print("Bot is running...")
client.run_until_disconnected()
