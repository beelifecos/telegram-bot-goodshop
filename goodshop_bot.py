from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = '7706460844:AAEPRsV7oYre2Vz0faOvx44UQOs3JNwNfBw'  # ← ЗАМЕНИТЕ на ваш актуальный токен

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

# Кнопка "Назад"
back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Назад в меню")]
    ],
    resize_keyboard=True
)

# /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Добро пожаловать в <b>Goodshop</b> — ваш надёжный партнёр по закупке косметики и различных товаров из Пусана 🇰🇷!\n\n"
        "📍 Наш склад находится в районе Техас-стрит (부산 중구 초량중로6번길 10) — это удобно для шипчандлеров и оптовиков.\n\n"
        "Выберите интересующий раздел ниже 👇",
        parse_mode="HTML",
        reply_markup=main_menu
    )

# Каталог
@dp.message(lambda msg: msg.text == "🛍 Каталог")
async def catalog_handler(message: Message):
    await message.answer(
        "🛍 <b>Каталог продукции Goodshop:</b>\n\n"
        "✅ <b>В наличии (на складе в Пусане):</b>\n"
        "👉 <a href='https://b2b.moysklad.ru/public/nY9BhNH4SMi9'>Открыть каталог</a>\n\n"
        "📦 <b>Под заказ (поставка в течение 1–2 недель):</b>\n"
        "👉 <a href='https://b2b.moysklad.ru/public/xYKr5ah2evme'>Смотреть товары под заказ</a>\n\n"
        "📝 <b>Как заказать:</b>\n"
        "! Заказ можно разместить прямо в прайсе, обязательно укажите ваш номер телефона для связи\n"
        "1. Напишите нам в WhatsApp (можно с фото или списком нужных товаров)\n"
        "2. Мы проверим наличие и вышлем цену и условия\n"
        "3. После подтверждения — упаковка и отправка, или самовывоз 📦\n\n"
        "📲 <a href='https://wa.me/821040483829'>Связаться в WhatsApp</a>\n\n"
        "🔔 Новинки и акции публикуются в нашем Telegram-канале:\n"
        "👉 <a href='https://t.me/+HBJZ3eA_cnhjMTI9'>Перейти в канал</a>\n\n"
        "🤖 Наш бот: @goodshop_busan_bot",
        parse_mode="HTML",
        reply_markup=back_menu
    )

# Как добраться
@dp.message(lambda msg: msg.text == "📦 Как добраться")
async def howtoget_handler(message: Message):
    await message.answer(
        "📍 <b>Как добраться до нас:</b>\n\n"
        "🏢 <b>Адрес (на корейском):</b> 부산광역시 중구 초량중로6번길 10 (영주동)\n"
        "📍 <b>Адрес (на английском):</b> 10, Choryangjung-ro 6beon-gil, Jung-gu, Busan, South Korea\n\n"
        "🚇 <b>На метро:</b>\n"
        "1. Доехать до станции <b>Busan Station (부산역)</b>, выход №7\n"
        "2. Пройти 200 метров прямо\n"
        "3. Повернуть направо на 초량중로6번길\n"
        "4. Пройти ~100 метров — здание справа 📦\n\n"
        "Если затрудняетесь найти — позвоните нам.\n\n"
        "🗺 <a href='https://maps.google.com/?q=부산광역시+중구+초량중로6번길+10'>Открыть в Google Maps</a>",
        parse_mode="HTML",
        reply_markup=back_menu
    )

# Контакты
@dp.message(lambda msg: msg.text == "📲 Контакты")
async def contact_handler(message: Message):
    await message.answer(
        "📞 <b>Контакты для связи:</b>\n\n"
        "📱 WhatsApp: <a href='https://wa.me/821040483829'>написать</a>\n"
        "📢 Telegram-канал: <a href='https://t.me/+HBJZ3eA_cnhjMTI9'>https://t.me/+HBJZ3eA_cnhjMTI9</a>\n"
        "🤖 Бот: @goodshop_busan_bot\n"
        "📸 Instagram: https://www.instagram.com/beelifecos/\n"
        "🎵 TikTok: https://www.tiktok.com/@beelifecoskorean?lang=ru-RU",
        parse_mode="HTML",
        reply_markup=back_menu
    )

# Как заказать
@dp.message(lambda msg: msg.text == "📝 Как заказать")
async def order_handler(message: Message):
    await message.answer(
        "📝 <b>Как оформить заказ:</b>\n\n"
        "1. Напишите нам в WhatsApp (можно с фото или списком нужных товаров)\n"
        "2. Мы проверим наличие и вышлем вам цену и условия\n"
        "3. После подтверждения — упаковка и отправка! Также вы можете приехать и забрать товар самостоятельно\n\n"
        "📲 <a href='https://wa.me/821040483829'>Связаться в WhatsApp</a>",
        parse_mode="HTML",
        reply_markup=back_menu
    )

# Соцсети
@dp.message(lambda msg: msg.text == "🌐 Соцсети")
async def social_handler(message: Message):
    await message.answer(
        "🌐 <b>Мы в соцсетях:</b>\n\n"
        "📸 Instagram: https://www.instagram.com/beelifecos/\n"
        "🎵 TikTok: https://www.tiktok.com/@beelifecoskorean\n"
        "📢 Telegram-канал: <a href='https://t.me/+HBJZ3eA_cnhjMTI9'>https://t.me/+HBJZ3eA_cnhjMTI9</a>\n"
        "🤖 Бот: @goodshop_busan_bot",
        parse_mode="HTML",
        reply_markup=back_menu
    )

# Назад
@dp.message(lambda msg: msg.text == "🔙 Назад в меню")
async def back_to_menu(message: Message):
    await message.answer("Вы вернулись в главное меню 👇", reply_markup=main_menu)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
