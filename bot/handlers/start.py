from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# from database.users import get_user, register_user

from bot.keyboards.reply import main_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=(
            f"Здравствуйте, {message.from_user.first_name}!\n\n"
            "Добро пожаловать в систему бронирования аудиторий."
        ),
        reply_markup=main_keyboard
    )