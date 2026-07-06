from datetime import datetime


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
    print("Создание заявки:", data)
    return True