# MAKIYAJ UCHUN MAHSULOT QUSHISH QISMI
from aiogram import types
from loader import dp, bot
from keyboards.inline.categories_inline import categorys
from states.AddProduct import AddProduct3, AddProduct2, AddProduct4, AddProduct3, AddProduct5, AddProduct6, AddProduct7, AddProduct8
from aiogram.dispatcher import FSMContext
from utils.db_api.database import send_ex
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.categories_inline import categorysdelete
from keyboards.inline.categories_inline import botShare
from data.config import GROUP_ID


@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)




@dp.callback_query_handler(text='admin2', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct2.product_name.set()



@dp.message_handler(state=AddProduct2.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct2.next()


@dp.message_handler(content_types='photo', state = AddProduct2.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct2.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct2.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct2.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct2.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS makiyaj(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO makiyaj(name, photoID, price, description)\
                             VALUES ('{name}', '{photo}', '{price}', '{desc}') ")
    except Exception as err:
        print(err)
        print('ERROR :  ', err)


    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr2_{name}")]
    ])

    


    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
                        #  \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()





@dp.callback_query_handler(text_startswith='send2gr2_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    # product = send_ex("SELECT * FROM ForFace")
    product = send_ex("SELECT * FROM makiyaj ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:\
        <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:    <b>{product[0][3]}</b>\n\nℹ️ Mahsulot haqida malumot:    <b>    {product[0][4]}</b>")
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)





































# IFORLAR UCHUN MAHSULOT QUSHISH


@dp.callback_query_handler(text='admin3', state=None)
async def cqq(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct3.product_name.set()


@dp.message_handler(state=AddProduct3.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct3.next()


@dp.message_handler(content_types='photo', state = AddProduct3.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct3.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct3.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct3.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct3.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va guruhga yuborildi!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS iforlar(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO iforlar(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)

    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr3_{name}")]
    ])
    
    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
    #                      \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()








@dp.callback_query_handler(text_startswith='send2gr3_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM iforlar ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}s'om</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)

























# TANA UCHUN MAHSULOT QUSHISH


@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)


@dp.callback_query_handler(text='admin4', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct4.product_name.set()


@dp.message_handler(state=AddProduct4.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct4.next()


@dp.message_handler(content_types='photo', state = AddProduct4.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct4.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct4.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct4.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct4.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va Guruhga yuborildi!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS tana_uchun(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO tana_uchun(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)
    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr4_{name}")]
    ])
    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
#     await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
#  \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()






@dp.callback_query_handler(text_startswith='send2gr4_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM tana_uchun ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)























# SOCHLAR  UCHUN MAHSULOT QUSHISH

@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)


@dp.callback_query_handler(text='admin5', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct5.product_name.set()


@dp.message_handler(state=AddProduct5.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct5.next()


@dp.message_handler(content_types='photo', state = AddProduct5.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct5.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct5.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct5.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct5.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va gutuhga yuborildi!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS soch_uchun(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO soch_uchun(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)
    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr5_{name}")]
    ])
    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
    #                       \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()







@dp.callback_query_handler(text_startswith='send2gr5_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM tana_uchun ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
















# AKSEESSSULAR   UCHUN MAHSULOT QUSHISH

@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)


@dp.callback_query_handler(text='admin6', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct6.product_name.set()


@dp.message_handler(state=AddProduct6.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct6.next()


@dp.message_handler(content_types='photo', state = AddProduct6.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct6.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct6.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct6.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct6.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va Mufavvaqiyatli guruhga yuborildi!!!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS aksessuarlar(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO aksessuarlar(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)

 #aksessuarlar

    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr6_{name}")]
    ])

    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
    #                      \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()




@dp.callback_query_handler(text_startswith='send2gr6_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM aksessuarlar ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)




















# WELLNESS  UCHUN MAHSULOT QUSHISH

@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)


@dp.callback_query_handler(text='admin7', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct7.product_name.set()


@dp.message_handler(state=AddProduct7.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct7.next()


@dp.message_handler(content_types='photo', state = AddProduct7.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct7.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct7.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct7.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct7.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va muvaffaqiyatli guruhga yuborildi!!!")

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS wellness(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO wellness(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)
    
    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr7_{name}")]
    ])

    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    
    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
                        #  \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
    await state.finish()





@dp.callback_query_handler(text_startswith='send2gr7_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM wellness ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)


































# ERKAKLAR  UCHUN MAHSULOT QUSHISH

@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!")


@dp.callback_query_handler(text='admin8', state=None)
async def cat1(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct8.product_name.set()


@dp.message_handler(state=AddProduct8.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct8.next()


@dp.message_handler(content_types='photo', state = AddProduct8.photo)
async def photo(msg: types.Message, state :FSMContext):
    if msg.photo:
        photo = msg.photo[-1]

        # PHOTO ID
        photo_id = photo.file_id
        print(photo_id)
        await state.update_data(
            {"photoID" :photo_id}
        )
        await msg.answer('<b>💲 Ajoyib endi mahsulotning NARXINI kiriting...</b>')
        await AddProduct8.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct8.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct8.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct8.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va muvaffaqiyatli guruhga yuborildi!!!")
    # await msg.answer('')

    data = await state.get_data()

    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS erkaklar_uchun(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO erkaklar_uchun(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)
        await msg.answer("NImadur xato ketdi!!!")

    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr8_{name}")]
    ])
        
    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)

    # await bot.send_photo(chat_id=GROUP_ID, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>\
                        #  \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
       
    await state.finish()



 

@dp.callback_query_handler(text_startswith='send2gr8_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    product = send_ex("SELECT * FROM erkaklar_uchun ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:   <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:   <b>{product[0][3]}so'm</b>\n\nℹ️ Mahsulot haqida malumot: <b>{product[0][4]}</b>\
                         \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)





