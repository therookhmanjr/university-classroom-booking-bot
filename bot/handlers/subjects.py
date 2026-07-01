from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.text == "📚 Предметы")
async def subjects(message: Message):
    await message.answer("Раздел 'Предметы' находится в разработке")