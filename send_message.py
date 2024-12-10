from pyrogram import Client
import time

# Ваши данные Telegram API
API_ID = "2845"  
API_HASH = "7133b2cc9b88fdc160d7264a"  

# Указываем ссылку или имя чата напрямую
CHAT_INPUT = "https://t.me/+Wt4NyCCTfK"  # Например, ссылка на приглашение
# или
# CHAT_INPUT = "@my_channel"  # Имя сообщества с @

# Сообщение
MESSAGE = """
сообщение которое я хочу отправить 😄
вторая строка сообщения 2
"""

# Проверяем и добавляем @, если отсутствует
if not CHAT_INPUT.startswith(("https://", "@")):
    CHAT_INPUT = f"@{CHAT_INPUT}"

# Создание клиента Telegram
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

# Запуск клиента и отправка сообщения
with app:
    try:
        # Получаем ID чата
        chat = app.get_chat(CHAT_INPUT)
        CHAT_ID = chat.id  

        while True:
            # Отправка сообщения
            app.send_message(CHAT_ID, MESSAGE)
            print("✅ Сообщение отправлено!")

            # Таймер
            wait_time = 3600  
            for remaining in range(wait_time, 0, -60):  
                minutes_left = remaining // 60
                print(f"⏳ Следующее сообщение через {minutes_left} мин.", end="\r")
                time.sleep(60)

    except Exception as e:
        print(f"❌ Ошибка: {type(e).__name__}: {e}")
        time.sleep(60)
