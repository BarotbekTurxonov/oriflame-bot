from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

MY_GROUPS = [-1001831195516]


# class MyGroupFilter(BoundFilter):
#     async def check(self, message: types.Message) -> bool:
#         return message.chat.type in (types.ChatType.GROUP, types.ChatType.SUPERGROUP) and message.chat.id in MY_GROUPS




class MyGroupFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.GROUP or message.chat.type == types.ChatType.SUPERGROUP




from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()