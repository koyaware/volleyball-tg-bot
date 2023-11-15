from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.keyboards.reply import USER_KEYBOARDS


async def user_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!\nИгры на сегодня: ⬇️',
                         reply_markup=USER_KEYBOARDS)


def register_user(dp: Dispatcher):
    dp.message.register(user_start, Command(commands=['start']))
