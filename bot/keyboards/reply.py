from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
    input_field_placeholder="Выберите действие"
)

main_menu_keyboard = main_keyboard

def get_subjects_keyboard(is_admin: bool = False) -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для модуля "Предметы"

    Args:
        is_admin: True - показывать кнопки для админа, False - только просмотр

    Returns:
        ReplyKeyboardMarkup: готовая клавиатура с кнопками
    """
    # Базовые кнопки для всех пользователей
    buttons = [
        [KeyboardButton(text="📚 Все предметы")]
    ]

    # Если пользователь админ - добавляем дополнительные кнопки
    if is_admin:
        buttons.append([
            KeyboardButton(text="➕ Добавить предмет"),
            KeyboardButton(text="❌ Удалить предмет")
        ])

    # Кнопка "Назад" всегда в конце
    buttons.append([KeyboardButton(text="🔙 Назад")])

    # Создаем и возвращаем клавиатуру
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )

    return keyboard