
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

BOT_TOKEN = "your-telegram-bot-token-here"  # Replace with your actual bot token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me any message and I'll translate it to English.")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original_text = update.message.text
    translated_text = GoogleTranslator(source='auto', target='en').translate(original_text)
    await update.message.reply_text(translated_text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))
    app.run_polling()
