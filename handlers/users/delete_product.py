from aiogram import types
from loader import dp
from loader import bot
from keyboards.inline.categories_inline import categorysdelete
from utils.db_api.database import send_ex
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from filters.guruh import AdminFilter
from filters.private import PrivateChatFilter



@dp.message_handler(PrivateChatFilter(), text="🛍Mahsulot o'chirish")
async def deteproduc(msg: types.Message):
    await msg.answer('Qaysi kategoriyadan mahsulotni o\'chirmoqchisiz?', reply_markup=categorysdelete)





##########################################################################################################

@dp.callback_query_handler(text='del1')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM ForFace")
    print(products)
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    # print(products)
    else:
        for i in products:
            print(i)
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='delproduct_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        

    async def is_delproduct_callback(call):
        return call.data.startswith('delproduct_')



    @dp.callback_query_handler(is_delproduct_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        print(product_id)
        try:
            test = send_ex(f"DELETE FROM ForFace WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()



##########################################################################################################


@dp.callback_query_handler(text='del2')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM makiyaj")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:    
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del2product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del2product_callback(call):
        return call.data.startswith('del2product_')


    @dp.callback_query_handler(is_del2product_callback)
    async def buy_product(call: types.CallbackQuery, state: FSMContext):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM makiyaj WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()



##########################################################################################################


@dp.callback_query_handler(text='del3')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM iforlar")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            print(i)
            print(i[2])
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del3product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=f"{i[2]}", caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del3product_callback(call):
        return call.data.startswith('del3product_')


    @dp.callback_query_handler(is_del3product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM iforlar WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()



##########################################################################################################




@dp.callback_query_handler(text='del4')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM tana_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:    
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del4product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del4product_callback(call):
        return call.data.startswith('del4product_')


    @dp.callback_query_handler(is_del4product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM tana_uchun WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()



##########################################################################################################





@dp.callback_query_handler(text='del5')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM soch_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del5product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del5product_callback(call):
        return call.data.startswith('del5product_')


    @dp.callback_query_handler(is_del5product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM soch_uchun WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()




##########################################################################################################






@dp.callback_query_handler(text='del6')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM aksessuarlar")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del6product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del6product_callback(call):
        return call.data.startswith('del6product_')


    @dp.callback_query_handler(is_del6product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM aksessuarlar WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()



##########################################################################################################





@dp.callback_query_handler(text='del7')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM wellness")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del7product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del7product_callback(call):
        return call.data.startswith('del7product_')


    @dp.callback_query_handler(is_del7product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM wellness WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()




##########################################################################################################




@dp.callback_query_handler(text='del8')
async def del222(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM erkaklar_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyada hech qanday mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            del_btn = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [types.InlineKeyboardButton("🗑 Mahsulotni o'chirish", callback_data='del8product_' + str(i[0]))]
                ]
            )

            await bot.send_photo(call.from_user.id, photo=str(i[2]), caption=f'Mahsulot :  \n\nID Raqami:  {i[0]}\nNomi:  {i[1]}\nNarxi:   {i[3]}',reply_markup=del_btn)
        


    async def is_del8product_callback(call):
        return call.data.startswith('del8product_')


    @dp.callback_query_handler(is_del8product_callback)
    async def buy_product(call: types.CallbackQuery):
        product_id = call.data.split('_')[1]
        try:
            test = send_ex(f"DELETE FROM erkaklar_uchun WHERE id={product_id}")
            await call.answer("Mahsulot o'chirildi!!!", show_alert=True)
        except Exception as err:
            await call.answer(f'Nimadur Xato ketdi((\n{err}')
        await call.message.delete()