from aiogram import types
from misc import dp
from aiogram.types import Message
from aiogram.filters import Command
import db


@dp.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Введи команду /report для получения отчета")

@dp.message(Command("report"))
async def message_handler(msg: types.Document):
    try:
        report = await db.report()
        await msg.reply_document(report)
    except Exception:
        await msg.answer('не могу составить отчет')
