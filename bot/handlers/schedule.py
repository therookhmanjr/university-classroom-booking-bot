from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.text == "📅 Расписание")
async def schedule(message: Message):
    await message.answer("Раздел 'Расписание' находится в разработке.")