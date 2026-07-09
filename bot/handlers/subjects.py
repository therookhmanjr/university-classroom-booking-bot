# bot/handlers/subjects.py

from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards.reply import get_subjects_keyboard
from database.subjects import (
    get_subjects,
    add_subject,
    delete_subject,
    format_subjects_list
)

# Создаем роутер для предметов
router = Router()

# Определяем состояния для FSM (машина состояний)
class SubjectStates(StatesGroup):
    """Состояния для работы с предметами"""
    waiting_for_subject_name = State()  # Ожидаем ввод названия предмета


# ============================================
# 1. Обработчик команды "📚 Предметы"
# ============================================

@router.message(F.text == "📚 Предметы")
async def show_subjects(message: Message):
    """Показывает список всех предметов"""
    # Получаем все предметы из БД
    subjects = get_subjects()

    # Форматируем список для вывода
    subjects_text = format_subjects_list(subjects)

    # TODO: Заменить на реальную проверку прав
    # Пока что всегда админ для тестирования
    is_admin = True

    # Создаем клавиатуру
    keyboard = get_subjects_keyboard(is_admin=is_admin)

    # Отправляем сообщение
    await message.answer(
        subjects_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ============================================
# 2. Обработчик кнопки "➕ Добавить предмет"
# ============================================

@router.message(F.text == "➕ Добавить предмет")
async def start_add_subject(message: Message, state: FSMContext):
    """Начинает процесс добавления нового предмета"""
    # TODO: Проверить, что пользователь админ

    # Устанавливаем состояние - ожидаем ввод названия
    await state.set_state(SubjectStates.waiting_for_subject_name)

    # Отправляем сообщение с запросом названия
    await message.answer(
        "✏️ Введите название нового предмета:\n\n"
        "Пример: <b>Базы данных</b>",
        reply_markup=ReplyKeyboardRemove(),  # Убираем клавиатуру
        parse_mode="HTML"
    )


# ============================================
# 3. Обработчик ввода названия предмета (FSM)
# ============================================

@router.message(SubjectStates.waiting_for_subject_name)
async def process_subject_name(message: Message, state: FSMContext):
    """Обрабатывает введенное название предмета"""
    # Получаем название из сообщения
    subject_name = message.text.strip()

    # Проверяем, что название не пустое
    if len(subject_name) < 2:
        await message.answer(
            "❌ Название должно содержать минимум 2 символа."
        )
        return

    # Добавляем предмет в БД
    try:
        add_subject(subject_name)

        # Очищаем состояние
        await state.clear()

        # Показываем успешное сообщение
        await message.answer(
            f"✅ Предмет <b>«{subject_name}»</b> успешно добавлен!",
            parse_mode="HTML"
        )

        # Показываем обновленный список предметов
        await show_subjects(message)


    except Exception as e:

        print(e)

        await message.answer(

            "❌ Не удалось добавить предмет."

        )


# ============================================
# 4. Обработчик кнопки "❌ Удалить предмет"
# ============================================

@router.message(F.text == "❌ Удалить предмет")
async def start_delete_subject(message: Message):
    """Показывает список предметов для удаления"""
    # TODO: Проверить, что пользователь админ

    # Получаем все предметы
    subjects = get_subjects()

    if not subjects:
        await message.answer(
            "📭 Нет предметов для удаления",
            reply_markup=get_subjects_keyboard(is_admin=True)
        )
        return

    # Создаем список для вывода с номерами
    subjects_text = "🗑 <b>Выберите предмет для удаления:</b>\n\n"

    for i, subject in enumerate(subjects, 1):
        subjects_text += f"{i}. {subject['name']}\n"

    subjects_text += "\n<i>Введите номер предмета, который хотите удалить</i>"

    # Отправляем сообщение
    await message.answer(
        subjects_text,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML"
    )


# ============================================
# 5. Обработчик удаления предмета по номеру
# ============================================

@router.message(F.text.regexp(r'^\d+$'))  # Регулярка: только цифры
async def process_delete_subject(message: Message):
    """Обрабатывает выбор предмета для удаления по номеру"""
    # Проверяем, что сообщение содержит только число
    try:
        number = int(message.text.strip())
    except ValueError:
        return

    # Получаем все предметы
    subjects = get_subjects()

    # Проверяем, что номер в допустимом диапазоне
    if number < 1 or number > len(subjects):
        await message.answer(
            f"❌ Некорректный номер. Введите число от 1 до {len(subjects)}"
        )
        return

    # Получаем предмет по номеру (индекс = номер - 1)
    subject_to_delete = subjects[number - 1]
    subject_id = subject_to_delete["id"]
    subject_name = subject_to_delete["name"]

    # Удаляем предмет
    try:
        success = delete_subject(subject_id)

        if success:
            await message.answer(
                f"✅ Предмет <b>«{subject_name}»</b> успешно удален!",
                parse_mode="HTML"
            )

            # Показываем обновленный список
            await show_subjects(message)
        else:
            await message.answer(
                "❌ Не удалось найти предмет для удаления"
            )


    except Exception as e:

        print(e)

        await message.answer(

            "❌ Не удалось удалить предмет."

        )


# ============================================
# 6. Обработчик кнопки "🔙 Назад"
# ============================================

@router.message(F.text == "🔙 Назад")
async def go_back(message: Message, state: FSMContext):
    """Возвращает в главное меню"""
    # Очищаем состояние, если оно было
    await state.clear()

    # Импортируем главное меню
    from bot.keyboards.reply import main_keyboard

    await message.answer(
        "Вы вернулись в главное меню",
        reply_markup=main_keyboard
    )