import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def get_random_image():
    response = requests.get("https://aleatori.cat/random.json")
    if response.status_code == 200:
        data = response.json()
        return data['url']
    else:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь команду /cat, чтобы получить случайное изображение.")

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    image_url = get_random_image()
    if image_url:
        await update.message.reply_photo(photo=image_url)
    else:
        await update.message.reply_text("Не удалось получить изображение. Попробуйте позже.")

# Основная функция для запуска бота
def main():
    application = ApplicationBuilder().token('8148202030:AAFd-ixQa7Ejl5VjYDnZ3KF5XjERaO8DOoc').build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cat", send_image))  # Исправлено с "car" на "cat"

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()