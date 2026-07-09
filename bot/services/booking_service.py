from datetime import datetime

from database.users import get_user
from database.booking import create_booking as create_booking_db
from database.classrooms import get_classroom_by_number

def format_booking_info(data: dict) -> str:
    return (
        "📋 Проверьте данные:\n\n"
        f"📅 Дата: {data['booking_date']}\n"
        f"🕒 Начало: {data['start_time']}\n"
        f"🕔 Конец: {data['end_time']}\n"
        f"🏫 Аудитория: {data['classroom']}\n"
        f"📝 Цель: {data['purpose']}"
    )

def create_booking(data: dict) -> bool:

    user = get_user(data["telegram_id"])

    if not user:
        return False

    classroom = get_classroom_by_number(data["classroom"])

    if not classroom:
        return False

    create_booking_db(
        classroom_id=classroom[0],
        user_id=user[0],
        booking_date=datetime.strptime(
            data["booking_date"],
            "%d.%m.%Y"
        ).date(),
        start_time=datetime.strptime(
            data["start_time"],
            "%H:%M"
        ).time(),
        end_time=datetime.strptime(
            data["end_time"],
            "%H:%M"
        ).time(),
        purpose=data["purpose"]
    )

    return True


