from aiogram.types import InlineKeyboardMarkup

from tgbot.misc.buttons.inline import btnCancel


cancel_inline = InlineKeyboardMarkup(inline_keyboard=[
    [btnCancel]
])