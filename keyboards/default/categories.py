from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


categoryUser = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🛍Mahsulotlar"),
        ],
        [
            KeyboardButton(text = "🔵 Biz ijtimoiy tarmoqlarda"),
            KeyboardButton(text = "📞 Biz bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True
)


categoryAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🛍Mahsulot qo'shish"),
            KeyboardButton(text = "🛍Mahsulot o'chirish"),
            
        ],
        [
            KeyboardButton(text = "🔵 Statistika"),
            KeyboardButton(text = "✏️ Katalogni o'zgartirish"),

        ],
        [
            KeyboardButton("🔗Katalogni ko'rish")
        ],
    ],
    resize_keyboard=True
)


contact = ReplyKeyboardMarkup(
    keyboard=[
    [
    KeyboardButton('📞 Telefon nomer', request_contact=True)
    ]
    ], resize_keyboard=True
)
