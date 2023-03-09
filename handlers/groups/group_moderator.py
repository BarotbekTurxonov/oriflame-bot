from aiogram import types
from filters.guruh import MyGroupFilter
from filters.private import PrivateChatFilter
from filters.guruh import AdminFilter
from loader import dp, bot
from aiogram.dispatcher.filters import Command
import re
import asyncio
from langdetect import detect
from data.config import ADMINS

@dp.message_handler(MyGroupFilter(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def delete_join_message(msg: types.Message):
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)


@dp.message_handler(MyGroupFilter(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def delete_leave_message(msg: types.Message):
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)




@dp.message_handler(MyGroupFilter(), Command("ban", prefixes="!"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()






link_2 = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"


link_pattern = re.compile(link_2)


@dp.message_handler(MyGroupFilter())
async def tes(msg: types.Message):
    if msg.text in ADMINS:
        pass

    else:
        try:
            if link_pattern.search(msg.text):
                await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
                # await msg.chat.kick(user_id=msg.from_user.id)

            elif msg.text in ['ish', 'иш', 'lichka', 'lichkaga', 'orgataman', 'ish bor']:
                await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
                # await msg.chat.kick(user_id=msg.from_user.id)

            elif detect(f"{msg.text}") == 'ar':
                await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
                await msg.chat.kick(user_id=msg.from_user.id)
            
            else:
                pass
        except:
            pass

