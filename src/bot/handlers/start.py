from aiogram import Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_command(message):
    await message.answer("Hello! I'm a bot!")
    await message.answer("You can use /help command to get help.")
