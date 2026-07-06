from aiogram.fsm.state import State, StatesGroup

class SubjectState(StatesGroup):
    adding_subject = State()
    deleting_subject = State()