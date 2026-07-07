from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Подтвердить"),
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True
)