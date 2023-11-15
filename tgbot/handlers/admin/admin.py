from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.reply import ADMIN_KEYBOARDS


async def admin_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}!\nИгры на сегодня: ⬇️'
                         f'\n\n\nКоманды для администраторов: \n<code>/create</code>, ',
                         reply_markup=ADMIN_KEYBOARDS)


async def cancel_button(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.bot.delete_message(call.from_user.id, call.message.message_id)
    await call.bot.send_message(call.from_user.id, "Действие отменено.")


def register_admin(dp: Dispatcher):
    dp.message.register(admin_start, AdminFilter(), Command(commands=['start']))
    dp.callback_query.register(cancel_button, F.data == 'cancelbutton')
