from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

# API ID dan API Hash Anda dari Telegram
api_id = '6'
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
bot_token = '7097508990:AAEWQdanPLIBD0biXuJIG5x2PlvytV4e8IA'

# Membuat klien bot menggunakan Pyrogram
app = Client('my_bot', api_id, api_hash, bot_token=bot_token)


@app.on_message(filters.command('start', prefixes='@'))
async def start_handler(client, message):
    username = message.text.split('@')[1].split()[0]  # Mengambil username dari pesan
    await message.reply_text(f'Halo @{username}! Terima kasih telah memulai bot ini.')


@app.on_inline_query()
async def inline_handler(client, inline_query):
    query = inline_query.query.strip().lower()

    # Memeriksa jika query mengandung 'start' dari username bot
    if query.startswith('@usernamebot start'):
        username = query.split('@')[1].split()[0]  # Mengambil username dari query

        # Membuat pesan balasan dengan username
        message = f'Halo @{username}! Terima kasih telah memulai bot ini.'

        # Membuat hasil inline
        results = [
            InlineQueryResultArticle(
                title='Start Bot',
                description=f'Start bot untuk @{username}',
                input_message_content=InputTextMessageContent(message_text=message)
            )
        ]

        # Mengirim hasil inline
        await inline_query.answer(results, cache_time=1)


print("Bot is running...")
app.run()
