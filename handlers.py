from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import keyboards as kb
import func

router = Router()

def start():
    return {

            "start_text": "👋 Привет! 🤖✨\n\n"
            "Я бот для управления сервером, на котором я запущен! 🖥️⚡️\n\n"
            "Готов принимать команды! 🚀 Жми кнопку в меню или пиши /help 🛠️📊",

            "start_keyboard": kb.get_start_keyboard()

            }


@router.message(Command("start"))
async def start_handler(message: Message):
    data = start()

    await message.answer(text=data["start_text"], reply_markup=data["start_keyboard"])

@router.callback_query(F.data == "restart_server")
async def restart_server_handler(callback: CallbackQuery):
    await callback.message.edit_text("🤖 Запущена перезагрузка")

    result = await func.restart_server()

    if result["returncode"] == 0:
        await callback.message.edit_text("🚀🤖 Успешная перезагрузка", reply_markup=)
    else:
        await callback.message.edit_text(f"❌ Ошибка: {result['stderr']}")

    await callback.answer()

@router.callback_query(F.data == "return_start")
async def return_start_handler(callback: CallbackQuery):
    data = start()

    await callback.message.edit_text(data["start_text"], reply_markup=data["start_keyboard"])