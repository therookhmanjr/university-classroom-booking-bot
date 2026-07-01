from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.text == "🏫 Свободные аудитории")
async def classrooms(message: Message):
    await message.answer("Раздел 'Свободные аудитории' находится в разработке.")

@router.message(F.text == "📝 Мои заявки")
async def my_booking(message: Message):
    await message.answer("Раздел 'Мои заявки' находится в разработке.")