from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Расписание"),
            KeyboardButton(text="📚 Предметы")
        ],
        [
            KeyboardButton(text="🏫 Свободные аудитории")
        ],
        [
            KeyboardButton(text="📝 Мои заявки")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder = "Выберите действие"
)