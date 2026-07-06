from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

time_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="08:00"),
            KeyboardButton(text="09:30")
        ],
        [
            KeyboardButton(text="11:00"),
            KeyboardButton(text="12:30")
        ],
        [
            KeyboardButton(text="14:00"),
            KeyboardButton(text="15:30")
        ],
        [
            KeyboardButton(text="17:00"),
            KeyboardButton(text="18:30")
        ],
        [
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True
)