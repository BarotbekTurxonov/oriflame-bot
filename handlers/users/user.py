from aiogram import types
from loader import dp, bot
from keyboards.inline.categories_inline import categorysuser, buy_btn
from utils.db_api.database import send_ex
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states.BuyProduct import BuyProduct1, BuyProduct2, BuyProduct3, BuyProduct4, BuyProduct5, BuyProduct6, BuyProduct7, BuyProduct8
from aiogram.dispatcher import FSMContext
from keyboards.default.categories import contact
from data.config import ADMINS
from keyboards.default.categories import categoryUser

@dp.message_handler(text='🛍Mahsulotlar')
async def test(msg: types.Message):
    await msg.answer("Kategoriya buyicha tanlang!!", reply_markup=categorysuser)



@dp.callback_query_handler(text='user1')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM ForFace")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy1product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback1(call):
    return call.data.startswith('buy1product_')


@dp.callback_query_handler(is_buyproduct_callback1, state=None)
async def buy_product(call: types.CallbackQuery, state: FSMContext):
    global product_id1
    product_id1 = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct1.name.set()


@dp.message_handler(state=BuyProduct1.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct1.next()

@dp.message_handler(content_types='contact', state=BuyProduct1.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct1.next()

@dp.message_handler(state=BuyProduct1.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM ForFace WHERE id={product_id1}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM ForFace WHERE id={product_id1}")
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')





























# user2 MAKIYAJ UCHUN MAHSULOTLARNI CHIQARIsh


@dp.message_handler(text='🛍Mahsulotlar')
async def test(msg: types.Message):
    await msg.answer("Kategoriya buyicha tanlang!!", reply_markup=categorysuser)



@dp.callback_query_handler(text='user2')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM makiyaj")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy2product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback2(call):
    return call.data.startswith('buy2product_')


@dp.callback_query_handler(is_buyproduct_callback2, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct2.name.set()




@dp.message_handler(state=BuyProduct2.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct2.next()

@dp.message_handler(content_types='contact', state=BuyProduct2.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct2.next()

@dp.message_handler(state=BuyProduct2.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM makiyaj WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM makiyaj WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')































# user3 IFORLAR UCHUN MAHSULOTLARNI CHIQARIsh

@dp.callback_query_handler(text='user3')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM iforlar")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy3product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback3(call):
    return call.data.startswith('buy3product_')


@dp.callback_query_handler(is_buyproduct_callback3, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct3.name.set()




@dp.message_handler(state=BuyProduct3.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct3.next()

@dp.message_handler(content_types='contact', state=BuyProduct3.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct3.next()

@dp.message_handler(state=BuyProduct3.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM iforlar WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM iforlar WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')



























# user4 TANA  UCHUN MAHSULOTLARNI CHIQARIsh


@dp.message_handler(text='🛍Mahsulotlar')
async def test(msg: types.Message):
    await msg.answer("Kategoriya buyicha tanlang!!", reply_markup=categorysuser)



@dp.callback_query_handler(text='user4')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM tana_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy4product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback4(call):
    return call.data.startswith('buy4product_')


@dp.callback_query_handler(is_buyproduct_callback4, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct4.name.set()




@dp.message_handler(state=BuyProduct4.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct4.next()

@dp.message_handler(content_types='contact', state=BuyProduct4.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct4.next()

@dp.message_handler(state=BuyProduct4.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM tana_uchun WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM tana_uchun WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')























# user5 SOCH  UCHUN MAHSULOTLARNI CHIQARIsh


@dp.callback_query_handler(text='user5')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM soch_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy5product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback5(call):
    return call.data.startswith('buy5product_')


@dp.callback_query_handler(is_buyproduct_callback5, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct5.name.set()




@dp.message_handler(state=BuyProduct5.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct5.next()

@dp.message_handler(content_types='contact', state=BuyProduct5.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct5.next()

@dp.message_handler(state=BuyProduct5.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM soch_uchun WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM soch_uchun WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')
































# user6 AKSESSURLAR  UCHUN MAHSULOTLARNI CHIQARISH



@dp.callback_query_handler(text='user6')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM aksessuarlar")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy6product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback6(call):
    return call.data.startswith('buy6product_')


@dp.callback_query_handler(is_buyproduct_callback6, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct6.name.set()




@dp.message_handler(state=BuyProduct6.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct6.next()

@dp.message_handler(content_types='contact', state=BuyProduct6.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct6.next()

@dp.message_handler(state=BuyProduct6.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM aksessuarlar WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM aksessuarlar WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')
















# user7 wellness   UCHUN MAHSULOTLARNI CHIQARISH


@dp.callback_query_handler(text='user7')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM wellness")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy7product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback7(call):
    return call.data.startswith('buy7product_')


@dp.callback_query_handler(is_buyproduct_callback7, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct7.name.set()




@dp.message_handler(state=BuyProduct7.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct7.next()

@dp.message_handler(content_types='contact', state=BuyProduct7.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct7.next()

@dp.message_handler(state=BuyProduct7.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM wellness WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM wellness WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')






















# user8 erkaklar_uchun   UCHUN MAHSULOTLARNI CHIQARISH


@dp.callback_query_handler(text='user8')
async def select(call: types.CallbackQuery):
    products = send_ex("SELECT * FROM erkaklar_uchun")
    if len(products) == 0:
        await call.answer("Ushbu Categoriyda hali mahsulot yo'q", show_alert=True)
    else:
        for i in products:
            buy_btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buy8product_' + str(i[0]))]
                ]
            )
            await bot.send_photo(call.from_user.id, str(i[2]), f"📄 Nomi:   <b>{i[1]}</b>\n💰 Narxi:   <b>{i[3]}so'm</b>\n📋 Mahsulot haqida ma'lumotlar:👇👇👇\n\n<b>{i[4]}</b>", reply_markup=buy_btn)


async def is_buyproduct_callback8(call):
    return call.data.startswith('buy8product_')


@dp.callback_query_handler(is_buyproduct_callback8, state=None)
async def buy_product(call: types.CallbackQuery):
    global product_id
    product_id = call.data.split('_')[1]
    await call.message.answer('Ajoyib, ismingiz nima edi....?', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct8.name.set()




@dp.message_handler(state=BuyProduct8.name)
async def add(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name':name}
    )
    await msg.answer('Endi menga telefon nomeringizni bering..\nPastdagi tugmani bosing!!', reply_markup=contact)
    await BuyProduct8.next()

@dp.message_handler(content_types='contact', state=BuyProduct8.phone)
async def ai(msg: types.Message, state: FSMContext):
    phone = msg.contact
    await state.update_data(
        {'phone':phone.phone_number}
        )
    await msg.answer('Dastavka xizmati kerakmi..?(ha/yoq)\n\n<b>⚠️Yetkazib berish faqatgina Samarqand Shahri ichida!!!</b>', reply_markup=types.ReplyKeyboardRemove())
    await BuyProduct8.next()

@dp.message_handler(state=BuyProduct8.dostavka)
async def dostavka(msg: types.Message, state: FSMContext):
    dostavka = msg.text

    if dostavka.lower() == 'yoq':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM erkaklar_uchun WHERE id={product_id}" )
        print(product)
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Yoq!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Buyurtmangiz tez orada yetkazib beriladi.')
        await state.finish()



    elif dostavka.lower() == 'ha':
        data = await state.get_data()
        name = data.get('name')
        phone = data.get('phone')
        product = send_ex(f"SELECT * FROM erkaklar_uchun WHERE id={product_id}")
        await bot.send_message(chat_id=ADMINS[0], text=f"<b>📩 Foydalanuvchi <a href='https://t.me/{msg.from_user.username}'>{name}</a> yangi mahsulot sotib oldi!</b>\n🛒 MAHSULOT:\n\n📛Nomi:   <b>{product[0][1]}</b>\n💵Narxi: <b> {product[0][3]}so'm</b>\n\n👥\nMijozning ismi <b> {name}</b>\nMijozning telefon raqami: <b> {phone}</b>\nDostavka:  Samarqand Shahar ichiga!!!")
        await bot.send_message(msg.chat.id, '😊Xaridingiz uchun rahmat! Mahsulotingiz Samarqand Shahri ichida yetkazib beriladi.', reply_markup=categoryUser)
        await state.finish()

    else:
        await msg.answer('Faqatgina "ha"  yoki  "yoq" deb javob bera olasiz!')





