from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="♻️ Перезагрузка", callback_data="restart_server")

def return_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅️ Назад", callback_data="return_start")