from aiogram import Dispatcher

from tgbot.handlers.admin.admin import register_admin
from tgbot.handlers.admin.create_game import register_game


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_game(dp)