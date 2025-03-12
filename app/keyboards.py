from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Help")],
    [KeyboardButton(text="Links")],
],
    resize_keyboard=True,
    input_field_placeholder="Choose smth..."
)

my_tg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="My Telegram", url="tg://resolve?domain=killmont")]
])

#builder example
# cars = ["Audi", "Toyota", "Porsche", "Mersedes"]
#
# async def inline_cars():
#     keybord = InlineKeyboardBuilder()
#     for car in cars:
#         keybord.add(InlineKeyboardButton(text=car, url=""))
#     return  keybord.adjust(2).as_markup
#
# при виклику в роутері в кінці треба прописати:
# reply_markup=await kb.inline_cars()
