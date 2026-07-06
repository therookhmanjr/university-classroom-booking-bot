from aiogram.fsm.state import State, StatesGroup

class BookingStates(StatesGroup):
    #Состояния для процесса бронирования
    selecting_building = State()
    selecting_classroom = State()
    selecting_date = State()
    selecting_start_time = State()
    selecting_end_time = State()
    entering_purpose = State()
    confirming = State()