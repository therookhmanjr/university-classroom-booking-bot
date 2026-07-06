from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

classroom_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏫 101"),
            KeyboardButton(text="🏫 102")
        ],
        [
            KeyboardButton(text="🏫 201"),
            KeyboardButton(text="🏫 315")
        ],
        [
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True
)