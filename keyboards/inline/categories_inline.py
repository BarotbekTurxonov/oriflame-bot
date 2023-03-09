from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

categorys = InlineKeyboardMarkup(
    inline_keyboard=[        
        [InlineKeyboardButton('Yuz uchun', callback_data='admin1')],
        [InlineKeyboardButton('Makiyaj', callback_data='admin2')],
        [InlineKeyboardButton('Iforlar', callback_data='admin3')],
        [InlineKeyboardButton('Tana uchun', callback_data='admin4')],
        [InlineKeyboardButton('Sochlar uchun', callback_data='admin5')],
        [InlineKeyboardButton('Aksessuarlar', callback_data='admin6')],
        [InlineKeyboardButton('Wellness', callback_data='admin7')],
        [InlineKeyboardButton('Erkaklar uchun', callback_data='admin8')],

    ]
)


share = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Guruhga yuborish 👥', callback_data='share2Group')],
    ]
)


categorysuser = InlineKeyboardMarkup(
    inline_keyboard=[        
        [InlineKeyboardButton('Yuz uchun', callback_data='user1')],
        [InlineKeyboardButton('Makiyaj', callback_data='user2')],
        [InlineKeyboardButton('Iforlar', callback_data='user3')],
        [InlineKeyboardButton('Tana uchun', callback_data='user4')],
        [InlineKeyboardButton('Sochlar uchun', callback_data='user5')],
        [InlineKeyboardButton('Akessuarlar', callback_data='user6')],
        [InlineKeyboardButton('Wellness', callback_data='user7')],
        [InlineKeyboardButton('Erkaklar uchun', callback_data='user8')],
    ]
)



buy_btn =  InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton('📥 Buyurtma berish', callback_data='buyproduct')]
    ]
)






categorysdelete = InlineKeyboardMarkup(
    inline_keyboard=[        
        [InlineKeyboardButton('Yuz uchun', callback_data='del1')],
        [InlineKeyboardButton('Makiyaj', callback_data='del2')],
        [InlineKeyboardButton('Iforlar', callback_data='del3')],
        [InlineKeyboardButton('Tana uchun', callback_data='del4')],
        [InlineKeyboardButton('Sochlar uchun', callback_data='del5')],
        [InlineKeyboardButton('Akessuarlar', callback_data='del6')],
        [InlineKeyboardButton('Wellness', callback_data='del7')],
        [InlineKeyboardButton('Erkaklar uchun', callback_data='del8')],
    ]
)











botShare = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton("Botga Kirish🔗", url='https://t.me/shirinaOriflamee_bot')]
    ]
)
























