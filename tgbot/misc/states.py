from aiogram.fsm.state import StatesGroup, State


class CreateGameState(StatesGroup):
    name = State()
    address = State()
    date = State()
    time = State()
    duration = State()
    min_players = State()
    max_players = State()
    cost = State()
    payment = State()