from aiogram.dispatcher.filters.state import StatesGroup, State


class New(StatesGroup):
    msg = State()

class EditCalatog(StatesGroup):
    name = State()