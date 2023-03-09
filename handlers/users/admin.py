from aiogram import types
from loader import dp, bot
from keyboards.inline.categories_inline import categorys, botShare
from states.AddProduct import AddProduct1
from aiogram.dispatcher import FSMContext
from utils.db_api.database import send_ex
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.categories_inline import categorysdelete
import asyncio
from states.new import EditCalatog
from data.config import GROUP_ID


@dp.message_handler(text="🛍Mahsulot qo'shish")
async def addpro(msg: types.Message):
    await msg.answer("Qaysi categoriya bo'yicha qo'shmoqchisiz? Tanlang!", reply_markup=categorys)



@dp.callback_query_handler(text='admin1', state=None)
async def qwewe(call: types.Message, state :FSMContext):
    await call.message.answer("<b>🔗 Yaxshi endi maxsulotni nomini kiriting...</b>", reply_markup=ReplyKeyboardRemove())
    await AddProduct1.product_name.set()
    # await cat.delete()


@dp.message_handler(state=AddProduct1.product_name)
async def add(msg : types.Message, state : FSMContext):
    productName = msg.text

    await state.update_data({
        "productName":productName
    })
    await msg.answer('<b>🖼 Endi menga mahsulotning rasmini yuboring..</b>')

    await AddProduct1.next()


@dp.message_handler(content_types='photo', state = AddProduct1.photo)
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
        await AddProduct1.next()
    else:
        await msg.answer('Ilitmos faqat rasm yuboring')


@dp.message_handler(state=AddProduct1.price)
async def test(msg: types.Message, state :FSMContext):
    price = msg.text
    if price.isdigit():
        await state.update_data({
            "price":price
        })
        await msg.answer("<b>ℹ️ Endi maxsulot haqida MALUMOT bering...</b>")
        await AddProduct1.next()
    else:
        await msg.answer("Narx faqat raqamlardan iborat bo'lishi kerak")


@dp.message_handler(state=AddProduct1.description)
async def desc(msg: types.Message, state:FSMContext):
    description = msg.text

    await state.update_data(
        {'description':description}
    )

    await msg.answer("Mahsulot qo'shildi va guruhda yuborildi!!")

    data = await state.get_data()
    name = data.get('productName')
    photo = data.get('photoID')
    price = data.get('price')
    desc = data.get('description')

    try:
        testproduct = send_ex("CREATE TABLE IF NOT EXISTS ForFace(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, photoID TEXT, price INTEGER, description TEXT)")
        addproduct = send_ex(f"INSERT INTO ForFace(name, photoID, price, description) VALUES('{name}', '{photo}', '{price}', '{desc}')")
    except Exception as err:
        print(err)
        print('ERROR :   ', err)

    inline_btn = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton('Guruhga yuborish', callback_data=f"send2gr1_{name}")]
    ])

    
    await bot.send_photo(chat_id=msg.chat.id, photo=str(photo), caption=f"📝 Mahsulot nomi:   <b>{name}</b>\n\n💰 Mahsulotimiz narxi:   <b>{price}</b>\n\nℹ️ Mahsulot haqida malumot: <b>{desc}</b>", reply_markup=inline_btn)
    await state.finish()



@dp.callback_query_handler(text_startswith='send2gr1_')
async def next_country(call:types.CallbackQuery):
    infolist = call.data.split('|')
    # product = send_ex("SELECT * FROM ForFace")
    product = send_ex("SELECT * FROM Forface ORDER BY id DESC LIMIT 1;")
    print(product)

    if len(product) == 0:
        await call.answer("Hech qanday mahsulot topilmadi!!", show_alert=True)
    else:
        print(infolist)
        await bot.send_photo(chat_id=GROUP_ID, photo=str(product[0][2]), caption=f"📝 Mahsulot nomi:\
        <b>{product[0][1]}</b>\n\n💰 Mahsulotimiz narxi:    <b>{product[0][3]}</b>\n\nℹ️ Mahsulot haqida malumot:    <b>    {product[0][4]}</b>\
            \n\n🛒 Mahsulotni sotib olish uchun <a href='https://t.me/ShirinaOriflamee_bot'>Shirina</a> botga kiring!!!", reply_markup=botShare)
        await call.answer("MAHSULOT GURUHGA YUBORILDI!!!", show_alert=True)
















@dp.message_handler(text='🔵 Statistika')
async def sts(msg: types.Message):
    users = send_ex("SELECT * FROM users")
    await msg.answer(f'Statistika buyicha barcha obunachilar soni:  {len(users)}')





@dp.message_handler(text="✏️ Katalogni o'zgartirish")
async def tqwer(msg: types.Message):
    await msg.answer('O\'zgartirmoqchi bo\'lgan katalogni kiriting...')
    await EditCalatog.name.set()




@dp.message_handler(state=EditCalatog.name)
async def edit(msg: types.Message, state : FSMContext):
    catalog = msg.text
    try:
        c = send_ex("CREATE TABLE IF NOT EXISTS catalog(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        c1 = send_ex(f"INSERT INTO catalog(name) VALUES('{catalog}')")
        await msg.answer("Katalog o'zgardi!")

        await state.finish()
    except Exception as err:
        print(err)
        await msg.answer("Katalog o'zgarmadi!")
        await state.finish()
        






@dp.message_handler(text="🔗Katalogni ko'rish")
async def catat(msg: types.Message):
    cat = send_ex("SELECT * FROM catalog ORDER BY ROWID DESC LIMIT 1")
    if cat:
        await msg.answer(f"Hozirgi katalog:   {cat[0][1]}")
    else:
        await msg.answer("Katalog topilmadi!")





