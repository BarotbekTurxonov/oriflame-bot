from environs import Env
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5612353733:AAEWdzHLe8m90aqTxA9VkBQFpo7OVdfqWkM"  # Bot toekn
ADMINS = [5420955032, 5235865310]  # adminlar ro'yxati
GROUP_ID = -1001281424493

from langdetect import detect

print(detect("العربي"))
print("HELLO WORLD")










