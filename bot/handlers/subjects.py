from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from database.subjects import get_subjects, add_subject, delete_subject, get_subject_by_id
from database.users import get_user
from bot.states.subjects import SubjectStates
from bot.keyboards.subjects import (
    subjects_main_keyboard,
    subjects_list_keyboard,
    subject_confirmation_keyboard
)

router = Router()


@router.message(F.text == "Предметы")
@router.message(Command("subjects"))
async def cmd_subjects(message: Message):
    user_id = message.from_user.id
    user = get_user(user_id)

    if not user:
        await message.answer("Сначала зарегистрируйтесь: /start")
        return

    is_admin = (user[3] == "admin")
    subjects = get_subjects()

    if not subjects:
        await message.answer(
            "В системе пока нет предметов.",
            reply_markup=subjects_main_keyboard(is_admin)
        )
        return

    text = "Список предметов:\n\n"
    for i, subject in enumerate(subjects, 1):
        text += f"{i}. {subject[1]} (ID: {subject[0]})\n"

    await message.answer(
        text,
        reply_markup=subjects_main_keyboard(is_admin)
    )


@router.message(F.text == "Все предметы")
async def show_all_subjects(message: Message):
    await cmd_subjects(message)


@router.message(F.text == "Добавить предмет")
async def cmd_add_subject(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)

    if not user or user[3] != "admin":
        await message.answer("У вас нет прав администратора.")
        return

    await message.answer("Введите название нового предмета:")
    await state.set_state(SubjectStates.adding_name)


@router.message(SubjectStates.adding_name)
async def process_add_subject(message: Message, state: FSMContext):
    name = message.text.strip()

    if len(name) < 2:
        await message.answer("Название должно содержать минимум 2 символа.")
        return

    try:
        add_subject(name)
        await message.answer(f"Предмет '{name}' добавлен.")
    except Exception:
        await message.answer(f"Предмет '{name}' уже существует.")

    await state.clear()


@router.message(F.text == "Удалить предмет")
async def cmd_delete_subject(message: Message):
    user = get_user(message.from_user.id)

    if not user or user[3] != "admin":
        await message.answer("У вас нет прав администратора.")
        return

    subjects = get_subjects()

    if not subjects:
        await message.answer("Нет предметов для удаления.")
        return

    await message.answer(
        "Выберите предмет для удаления:",
        reply_markup=subjects_list_keyboard(subjects)
    )


@router.callback_query(F.data.startswith("delete_subject_"))
async def confirm_delete_subject(callback: CallbackQuery, state: FSMContext):
    subject_id = int(callback.data.split("_")[2])
    subject = get_subject_by_id(subject_id)

    if not subject:
        await callback.message.edit_text("Предмет не найден.")
        await callback.answer()
        return

    await state.update_data(delete_subject_id=subject_id)

    await callback.message.edit_text(
        f"Удалить '{subject[1]}' (ID: {subject_id})?",
        reply_markup=subject_confirmation_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "confirm_delete")
async def process_delete_subject(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    subject_id = data.get("delete_subject_id")

    if not subject_id:
        await callback.message.edit_text("Ошибка: ID предмета не найден.")
        await callback.answer()
        return

    try:
        delete_subject(subject_id)
        await callback.message.edit_text("Предмет успешно удалён.")
    except Exception:
        await callback.message.edit_text(
            "Нельзя удалить предмет. Он используется в расписании."
        )

    await state.clear()
    await callback.answer()


@router.callback_query(F.data == "cancel_delete")
async def cancel_delete_subject(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Удаление отменено.")
    await state.clear()
    await callback.answer()


@router.callback_query(F.data == "subjects_back")
async def subjects_back(callback: CallbackQuery):
    subjects = get_subjects()

    if not subjects:
        await callback.message.edit_text("В системе пока нет предметов.")
        await callback.answer()
        return

    text = "Список предметов:\n\n"
    for i, subject in enumerate(subjects, 1):
        text += f"{i}. {subject[1]} (ID: {subject[0]})\n"

    await callback.message.edit_text(
        text,
        reply_markup=subjects_list_keyboard(subjects)
    )
    await callback.answer()


@router.message(F.text == "Назад")
async def back_to_main(message: Message):
    from bot.keyboards.user import main_menu_keyboard

    await message.answer(
        "Главное меню:",
        reply_markup=main_menu_keyboard()
    )