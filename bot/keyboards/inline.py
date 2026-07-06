from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def buildings_keyboard(buildings):
    #Клавиатура со списком корпусов
    buttons = []
    for building_id, name in buildings:
        buttons.append([
            InlineKeyboardButton(
                text=f"{name}",
                callback_data=f"building_{building_id}"
            )
        ])
    buttons.append([InlineKeyboardButton(text="Отмена", callback_data="cancel")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def classrooms_keyboard(classrooms):
    #Клавиатура со списком аудиторий
    buttons = []
    for classroom_id, room_number, building_name in classrooms:
        buttons.append([
            InlineKeyboardButton(
                text=f"{room_number} ({building_name})",
                callback_data=f"classroom_{classroom_id}"
            )
        ])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_buildings")])
    buttons.append([InlineKeyboardButton(text="Отмена", callback_data="cancel")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)