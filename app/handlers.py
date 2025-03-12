from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import  app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello, {message.from_user.first_name}!",
                        reply_markup=kb.main)

@router.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "links":
        await message.answer("If you have questions - text me", reply_markup=kb.my_tg)

