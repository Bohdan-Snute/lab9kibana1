import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Увімкнення логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен твого бота
BOT_TOKEN = "8182334735:AAGJSB1IGEPQjM5oxK7g0BaeHwr4e7PSobY"
FLUENTD_URL = "http://localhost:8080"  # Це адреса Fluentd

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text

    data = {
        "UserId": user.id,
        "UserName": user.username,
        "Text": message,
    }

    # Відправка логів у Fluentd
    try:
        requests.post(FLUENTD_URL, json=data)
        logging.info("Лог надіслано у Fluentd")
    except Exception as e:
        logging.error(f"Не вдалося надіслати лог: {e}")

    await update.message.reply_text("Повідомлення отримано та залоговано!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущено. Надішли повідомлення в Telegram.")
    app.run_polling()
