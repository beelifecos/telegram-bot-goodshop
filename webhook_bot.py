from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import os
import asyncio

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")  # токен через env переменную

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура главного меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог"), KeyboardButton(text="📦 Как добраться")],
        [KeyboardButton(text="📲 Контакты"), KeyboardButton(text="📝 Как заказать")],
        [KeyboardButton(text="🌐 Соцсети")]
    ],
    resize_keyboard=True
)

back_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🔙 Назад в меню")]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Добро пожаловать в <b>Goodshop</b> — ваш надёжный партнёр по закупке косметики и различных товаров из Пусана 🇰🇷!\n\n"
        "📍 Наш склад находится в районе Техас-стрит (부산 중구 초량중로6번길 10) — это удобно для шипчандлеров и оптовиков.\n\n"
        "Выберите интересующий раздел ниже 👇",
        parse_mode="HTML",
        reply_markup=main_menu
    )

# Все остальные хендлеры точно такие же, как у тебя (копируй сюда)

@dp.message(lambda msg: msg.text == "🔙 Назад в меню")
async def back_to_menu(message: Message):
    await message.answer("Вы вернулись в главное меню 👇", reply_markup=main_menu)

# Обработка webhook
async def handle_update(request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.process_update(update)
        return web.Response(text="OK")
    except Exception as e:
        print(f"Error: {e}")
        return web.Response(status=500)

async def on_startup(app):
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/webhook"
    await bot.set_webhook(webhook_url)
    print(f"Webhook set to: {webhook_url}")

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.close()

app = web.Application()
app.router.add_post('/webhook', handle_update)
app.router.add_get('/healthz', lambda request: web.Response(text="OK"))

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == "__main__":
    web.run_app(app, port=8000)
