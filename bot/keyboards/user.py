from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Забронировать"),
                KeyboardButton(text="Мои бронирования")
            ],
            [
                KeyboardButton(text="Предметы"),
                KeyboardButton(text="Отменить")
            ],
            [
                KeyboardButton(text="Помощь")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )