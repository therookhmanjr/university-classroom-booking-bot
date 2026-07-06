from aiogram.fsm.state import State, StatesGroup

class BookingState(StatesGroup):
    choosing_date = State()
    choosing_start_time = State()
    choosing_end_time = State()
    choosing_classroom = State()
    entering_purpose = State()
    confirming = State()