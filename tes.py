from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Token bot Telegram Anda
TOKEN = '7097508990:AAEWQdanPLIBD0biXuJIG5x2PlvytV4e8IA'

def start(update, context):
    update.message.reply_text('Bot inline telah diaktifkan!')

def inlinequery(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = [
        InlineQueryResultArticle(
            id='1',
            title='Contoh Judul',
            input_message_content=InputTextMessageContent('Ini adalah contoh pesan')
        )
    ]
    update.inline_query.answer(results)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
