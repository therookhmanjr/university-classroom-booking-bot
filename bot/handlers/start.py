from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.users import get_user
from database.users import register_user

from bot.keyboards.reply import main_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = get_user(message.from_user.id)

    if user is None:
        register_user(
            telegram_id = message.from_user.id,
            full_name = message.from_user.full_name,
        )

        text = (
            f"Здравствуйте, {message.from_user.first_name}!\n\n"
            "Вы успешно зарегистрированы"
        )
    else:
        text = (
            f"С возвращением, {message.from_user.first_name}!"
        )

    await message.answer(text = text, reply_markup = main_keyboard)