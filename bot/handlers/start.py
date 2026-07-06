from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.reply import main_keyboard
# from database.users import get_user, register_user


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.first_name}!",
        reply_markup=main_keyboard
    )