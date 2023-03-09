from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.new import New
from loader import dp, bot
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from keyboards.default.categories import categoryUser
from filters.private import PrivateChatFilter

@dp.message_handler(PrivateChatFilter(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))








@dp.message_handler(PrivateChatFilter(),text="🔵 Biz ijtimoiy tarmoqlarda")
async def smm(msg: types.Message):
    await msg.answer("🔵 Biz ijtimoiy tarmoqlarda :\n\n<a href='https://t.me/oriflameishga'>Original Oriflame</a>Guruhiga Obuna Bo'ling")


@dp.message_handler(PrivateChatFilter(),text="📞 Biz bilan bog'lanish")
async def contact(msg: types.Message):
    await msg.answer("Adminga Yubormoqchi bo'lgan xabaringizni yozing.....")
    await New.msg.set()


@dp.message_handler(state=New.msg)
async def test1(msg: types.Message, state :FSMContext):
    admin2msg = msg.text
    await bot.send_message(chat_id=ADMINS[0], text=f"Foydalanuvchidan yangi xabar :\n\nIsmi:  {msg.from_user.full_name}\nTelegram :   @{msg.from_user.username}\nXabar matni:   <b>{admin2msg}</b>")
    await msg.answer("✅ Xabaringiz Adminga yuborildi!", reply_markup=categoryUser)
    await state.finish()





