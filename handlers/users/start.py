from time import sleep
#Dasturchi @Mrgayratov kanla @Kingsofpy
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from aiogram import types
from aiogram.types import CallbackQuery

from data.config import ADMINS
from filters import IsUser, IsSuperAdmin, IsGuest
from filters.admins import IsAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, main_menu_for_admin
from loader import dp, db, bot
from states.send_chanell import SuperAdminStateChannel
import random
logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(text="start")
async def bot_echo(message: CallbackQuery):
    user = message.from_user
    try:
        db.add_user(user_id=user.id,name=user.first_name)
    except:
        pass

    await bot.send_message(chat_id=user.id,text="<b>– Yaxshi Qo'shimcha Ma'lumotlar Uchun:\n\nSizga Kerakli Bo'lgan Ma'lumot Kodini Kiriting yoki Bu Botga O'tgan Tugmangizni Qaytadan Bosing.</b>")

@dp.message_handler(IsAdmin(), commands="admin", state="*")
async def bot_start_admin(message: types.Message):
    await message.answer(f"Assalom alaykum Admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_admin)

@dp.message_handler(IsSuperAdmin(), commands="panel", state="*")
async def bot_start_super_admin(message: types.Message):
    await message.answer(f"Assalom alaykum Bosh Admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_super_admin)

@dp.message_handler(IsGuest(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    try:
        db.add_user(user_id=user.id,name=user.first_name)
    except:
        pass
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Salom {user_id}</b>")


@dp.message_handler(IsUser(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    try:
        db.add_user(user_id=user.id,name=user.first_name)
    except:
        pass
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Salom {user_id}</b>")