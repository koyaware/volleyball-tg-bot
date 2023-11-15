from aiogram.types import KeyboardButton

from tgbot.misc.commands import Commands

CREATE_GAME_BUTTON = KeyboardButton(text=str(Commands.create_game.value))
UPCOMING_GAMES_BUTTON = KeyboardButton(text=str(Commands.upcoming_games.value))
MY_GAMES_BUTTON = KeyboardButton(text=str(Commands.my_games.value))
ARCHIVE_BUTTON = KeyboardButton(text=str(Commands.archive.value))