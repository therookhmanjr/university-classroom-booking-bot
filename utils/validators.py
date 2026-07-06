from datetime import datetime
from datetime import timedelta
from config.constants import (
    UNIVERSITY_OPEN_TIME,
    UNIVERSITY_CLOSE_TIME,
)
from config.constants import MAX_BOOKING_HOURS


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def is_valid_time(time_str: str) -> bool:
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def is_future_date(date_str: str) -> bool:
    booking_date = datetime.strptime(date_str, "%d.%m.%Y").date()
    today = datetime.today().date()

    return booking_date >= today

def is_working_time(time_str: str) -> bool:
    current = datetime.strptime(time_str, "%H:%M").time()

    start = datetime.strptime(
        UNIVERSITY_OPEN_TIME,
        "%H:%M"
    ).time()

    end = datetime.strptime(
        UNIVERSITY_CLOSE_TIME,
        "%H:%M"
    ).time()

    return start <= current <= end

def is_booking_duration_valid(start_time: str, end_time: str) -> bool:
    start = datetime.strptime(start_time, "%H:%M").time()
    end = datetime.strptime(end_time, "%H:%M").time()

    duration = end - start

    return duration <= timedelta(hours=MAX_BOOKING_HOURS)