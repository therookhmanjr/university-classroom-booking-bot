from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from bot.keyboards.reply import main_keyboard

from bot.keyboards.booking import confirm_keyboard
from bot.states.booking import BookingState
from utils.validators import is_valid_date, is_valid_time
from datetime import datetime
from bot.keyboards.time import time_keyboard
from bot.services.booking_service import format_booking_info
from config.messages import BOOKING_CANCELED
from bot.keyboards.classrooms import classroom_keyboard
from config.constants import AVAILABLE_CLASSROOMS
from bot.services.booking_service import create_booking

router = Router()

@router.message(StateFilter("*"), lambda message: message.text == "❌ Отмена")
async def cancel_booking(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        BOOKING_CANCELED,
        reply_markup = main_keyboard
    )

@router.message(F.text == "🏫 Свободные аудитории")
async def classrooms(message: Message):
    await message.answer("Раздел 'Свободные аудитории' находится в разработке.")

@router.message(F.text == "📝 Мои заявки")
async def my_booking(message: Message):
    await message.answer("Раздел 'Мои заявки' находится в разработке.")

@router.message(BookingState.choosing_date)
async def booking_date(message: Message, state: FSMContext):
    if not is_valid_date(message.text):
        await message.answer(
            "❌ Неверный формат даты.\n\n"
            "Введите дату в формате ДД.ММ.ГГГГ."
        )
        return

    await state.update_data(
        booking_date=message.text
    )

    await state.set_state(
        BookingState.choosing_start_time
    )

    await message.answer(
        "Введите время начала:",
        reply_markup = time_keyboard
    )

@router.message(BookingState.choosing_start_time)
async def booking_start_time(message: Message, state: FSMContext):

    if not is_valid_time(message.text):
        await message.answer(
            "❌ Неверный формат времени.\n\n"
            "Введите время в формате ЧЧ:ММ."
        )
        return

    await state.update_data(start_time=message.text)

    await state.set_state(BookingState.choosing_end_time)

    await message.answer(
        "Введите время окончания:",
        reply_markup = time_keyboard

    )

@router.message(BookingState.choosing_end_time)
async def booking_end_time(message: Message, state: FSMContext):

    if not is_valid_time(message.text):
        await message.answer(
            "❌ Неверный формат времени."
        )
        return

    data = await state.get_data()

    start = datetime.strptime(data["start_time"], "%H:%M")
    end = datetime.strptime(message.text, "%H:%M")

    if end <= start:
        await message.answer(
            "❌ Время окончания должно быть позже времени начала."
        )
        return

    await state.update_data(end_time=message.text)

    await state.set_state(BookingState.choosing_classroom)

    await message.answer(
        "Выберите аудиторию:",
        reply_markup=classroom_keyboard
    )

@router.message(BookingState.choosing_classroom)
async def booking_classroom(message:Message, state: FSMContext):
    if message.text not in AVAILABLE_CLASSROOMS:
        await message.answer(
            "Пожалуйста, выберите аудиторию с помощью кнопок."
        )
        return

    await state.update_data(classroom=message.text)

    await state.set_state(BookingState.entering_purpose)

    await message.answer(
        "Введите цель бронирования.",
        reply_markup = ReplyKeyboardRemove()
    )

@router.message(BookingState.entering_purpose)
async def booking_purpose(message: Message, state: FSMContext):
    purpose = message.text.strip()

    if len(purpose) < 5:
        await message.answer(
            "Опишите цель бронирования подробнее."
        )
        return

    await state.update_data(purpose=purpose)

    data = await state.get_data()

    text = format_booking_info(data)

    await state.set_state(BookingState.confirming)

    await message.answer(
        text,
        reply_markup=confirm_keyboard
    )

@router.message(BookingState.confirming)
async def booking_confirm(message:Message, state: FSMContext):
    if message.text == "✅ Подтвердить":
        data = await state.get_data()

        data["telegram_id"] = message.from_user.id

        create_booking(data)

        await message.answer(
            "✅ Заявка успешно создана.",
            reply_markup=main_keyboard
        )

    elif message.text == "❌ Отмена":
        await message.answer(
            "❌ Бронирование отменено.",
            reply_markup = main_keyboard
        )

    else:
        await message.answer(
            "Пожалуйста, воспользуйтесь кнопками."
        )
        return

    await state.clear()