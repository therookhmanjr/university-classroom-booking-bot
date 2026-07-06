from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def subjects_main_keyboard(is_admin: bool = False):
    buttons = [[KeyboardButton(text="Все предметы")]]
    if is_admin:
        buttons.append([
            KeyboardButton(text="Добавить предмет"),
            KeyboardButton(text="Удалить предмет")
        ])
    buttons.append([KeyboardButton(text="Назад")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def subjects_list_keyboard(subjects):
    buttons = []
    for subject in subjects:
        buttons.append([
            InlineKeyboardButton(
                text=f"X {subject[1]}",
                callback_data=f"delete_subject_{subject[0]}"
            )
        ])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="subjects_back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def subject_confirmation_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да, удалить", callback_data="confirm_delete"),
            InlineKeyboardButton(text="Отмена", callback_data="cancel_delete")
        ]
    ])