import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def get_random_image():
    try:
        response = requests.get("https://aleatori.cat/random.json")
        response.raise_for_status()  # Проверка на HTTP ошибки
        data = response.json()
        return data['url']
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении изображения: {e}")
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Привет! Отправь команду /cat, чтобы получить случайное изображение.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        image_url = get_random_image()
        if image_url:
            await update.message.reply_photo(photo=image_url)
        else:
            await update.message.reply_text("Не удалось получить изображение. Попробуйте позже.")
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")

# Основная функция для запуска бота
def main():
    try:
        application = ApplicationBuilder().token('8148202030:AAFd-ixQa7Ejl5VjYDnZ3KF5XjERaO8DOoc').build()

        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("cat", send_image))  # Исправлено с "car" на "cat"

        # Запускаем бота
        application.run_polling()
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    main()