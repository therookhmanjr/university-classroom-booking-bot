from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

date_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Сегодня"),
            KeyboardButton(text="📅 Завтра")
        ],
        [
            KeyboardButton(text="📅 Другая дата")
        ],
        [
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True
)