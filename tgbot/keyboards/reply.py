from aiogram.types import ReplyKeyboardMarkup

from tgbot.misc.buttons.reply import CREATE_GAME_BUTTON, UPCOMING_GAMES_BUTTON, MY_GAMES_BUTTON, ARCHIVE_BUTTON


ADMIN_KEYBOARDS = ReplyKeyboardMarkup(keyboard=[
    [CREATE_GAME_BUTTON, UPCOMING_GAMES_BUTTON],
    [MY_GAMES_BUTTON, ARCHIVE_BUTTON],
], resize_keyboard=True)


USER_KEYBOARDS = ReplyKeyboardMarkup(keyboard=[
    [UPCOMING_GAMES_BUTTON],
    [MY_GAMES_BUTTON, ARCHIVE_BUTTON],
], resize_keyboard=True)