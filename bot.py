
import logging
import os
import random
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "@admin")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

MOTIVATION_LIST = [
    "🔋 Не здавайся. Великі справи потребують часу!",
    "🔥 Кожен день — новий шанс!",
    "💪 Успіх — це 1% таланту і 99% наполегливості.",
    "🚀 Все можливо, варто лише спробувати!",
    "🧠 Навіть найменший крок — це крок вперед.",
    "✨ Ти сильніший, ніж думаєш."
]

@dp.message_handler(commands=['start', 'help'])
async def send_help(message: types.Message):
    help_text = ("""
        🛠 <b>G5 Helper Pro — команди:</b>
        /help — показати всі команди
        /all [текст] — тег усіх у чаті + текст
        /request — тег адміністратора + того, хто просить
        /motivation — випадкова мотиваційна цитата
    """)
    await message.reply(help_text, parse_mode="HTML")

@dp.message_handler(commands=['all'])
async def tag_all(message: types.Message):
    args = message.get_args()
    if not args:
        await message.reply ("""❌ Команда /all потребує тексту. Наприклад:
`/all Зустріч о 20:00!`""", parse_mode="Markdown")
        return
    text = f"🔔 Увага всім! {args}"
    await message.reply(text)

@dp.message_handler(commands=['request'])
async def request_check(message: types.Message):
    user_tag = message.from_user.username or message.from_user.first_name
    await message.reply(f"""📬 {OWNER_USERNAME}
🔔 @{user_tag} відправив(-ла) pull request на GitHub .""")

@dp.message_handler(commands=['motivation'])
async def send_motivation(message: types.Message):
    quote = random.choice(MOTIVATION_LIST)
    await message.reply(quote)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
