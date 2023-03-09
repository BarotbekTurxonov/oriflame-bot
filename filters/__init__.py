from aiogram import Dispatcher

from loader import dp
from .private import PrivateChatFilter
from .guruh import MyGroupFilter


if __name__ == "filters":
    dp.filters_factory.bind(MyGroupFilter)
    dp.filters_factory.bind(PrivateChatFilter)
