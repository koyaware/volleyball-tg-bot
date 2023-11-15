import re
from datetime import datetime, timedelta

from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.inline import cancel_inline
from tgbot.misc.commands import Commands
from tgbot.misc.states import CreateGameState


async def create_game(message: Message, state: FSMContext):
    await message.bot.send_message(message.from_user.id, 'Площадка: \n\n<code>Пример: Название площадки</code>',
                                   reply_markup=cancel_inline)
    await state.set_state(CreateGameState.name)


async def address_game(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(CreateGameState.address)
    await message.bot.send_message(message.from_user.id, 'Адрес: \n\n<code>Пример: Адресс площадки</code>',
                                   reply_markup=cancel_inline)


async def date_game(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await state.set_state(CreateGameState.date)
    await message.bot.send_message(message.from_user.id, 'Дата: \n\n<code>Пример: Дата игры</code>',
                                   reply_markup=cancel_inline)


async def time_game(message: Message, state: FSMContext):
    date_pattern = re.compile(r'^\d{1,2}\.\d{1,2}$')
    if not date_pattern.match(message.text):
        return await message.bot.send_message(message.from_user.id, 'Повторите заново!')
    day, month = map(int, message.text.split('.'))
    if not (1 <= month <= 12):
        return await message.bot.send_message(message.from_user.id, 'Введите правильное значение!')
    current_date = datetime.now().date()
    game_date = datetime(current_date.year, month, day).date()
    if not current_date <= game_date <= current_date + timedelta(days=7):
        return await message.bot.send_message(message.from_user.id,
                                              'Объявление об игре не может быть раньше текущей даты '
                                              'и позже чем 7 дней от текущей даты!\nПовторите заново!')
    await state.update_data(date=message.text)
    await state.set_state(CreateGameState.time)
    await message.bot.send_message(message.from_user.id, 'Время: \n\n<code>Пример: Время игры</code>',
                                   reply_markup=cancel_inline)


async def duration_game(message: Message, state: FSMContext):
    time_pattern = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
    if not time_pattern.match(message.text):
        return await message.bot.send_message(message.from_user.id, 'Повторите заново!')
    await state.update_data(time=message.text)
    await state.set_state(CreateGameState.duration)
    await message.bot.send_message(message.from_user.id, 'Продолжительность: '
                                                         '\n\n<code>Пример: Продолжительность игры</code>',
                                   reply_markup=cancel_inline)


def register_game(dp: Dispatcher):
    dp.message.register(create_game, AdminFilter(), F.text.in_([Commands.create_game.value, '/create']))
    dp.message.register(address_game, AdminFilter(), CreateGameState.name)
    dp.message.register(date_game, AdminFilter(), CreateGameState.address)
    dp.message.register(time_game, AdminFilter(), CreateGameState.date)
    dp.message.register(duration_game, AdminFilter(), CreateGameState.time)