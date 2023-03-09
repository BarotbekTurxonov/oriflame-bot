from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.database import send_ex
from loader import dp, bot
from keyboards.default.categories import categoryAdmin, categoryUser
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from filters.private import PrivateChatFilter

@dp.message_handler(PrivateChatFilter(), CommandStart(), state="*")
async def bot_start(message: types.Message, state:FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer('Assalom alaykum!\n<b>Admin panelga xush kelibsiz</b>', reply_markup=categoryAdmin)
        await state.finish()
    else:
        user_id = message.from_user.id
        try:
            test = send_ex("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY)")

            user = send_ex(f"""INSERT INTO users (user_id) 
                    VALUES ({user_id})""")


            print(f"|INFO| - {message.from_user.full_name.upper()} ADDED TO DATABASE")
            await message.answer(f'Assalo alaykum  {message.from_user.full_name}', reply_markup=categoryUser)
            await state.finish()
        except Exception as ex:
            print(ex)
            await message.answer(f'Assalom alaykum {message.from_user.full_name}!', reply_markup=categoryUser)
            await state.finish()


    






# @dp.message_handler('🔵 Biz ijtimoiy tarmoqlarda')
# async def smm(msg: types.Message):
#     await msg.answer("🔵 Biz ijtimoiy tarmoqlarda \n\n<a href='https://t.me/oriflameishga'>Original Oriflame</a>Guruhiga Obuna Bo'ling")


# @dp.message_handler("📞 Biz bilan bog'lanish")
# async def contact(msg: types.Message):
#     await msg.answer("Adminga Yubormoqchi bo'lgan xabaringizni yozing.....")
#     await Admin.msg.set()


# @dp.message_handler(state=Admin.msg)
# async def test1(msg: types.Message):
#     admin2msg = msg.text
#     await bot.send_message(chat_id=ADMINS[0], text=f"Foydalanuvchidan yangi xabar :\n\nIsmi:  {msg.from_user.full_name}\nTelegram :   @{msg.from_user.username}\nXabar matni:   <b>{admin2msg}</b>")