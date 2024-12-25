import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import message, KeyboardButton, ReplyKeyboardMarkup, ContentType
import random
import requests
import pyttsx3
import subprocess


logging.basicConfig(level=logging.INFO)
bot = Bot(token='7730703433:AAHa0VCdYatc8kGn3OmbG767tpOdrVO-Z7Q')
dp = Dispatcher()

btn_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Horror")],
        [KeyboardButton(text = "Action")],
        [KeyboardButton(text = "Humor")],
        [KeyboardButton(text = "Fantasy")],
    ],
    resize_keyboard=True
)

engine = pyttsx3.init()

engine.setProperty("rate",150)
engine.setProperty("volume",0.9)\

engine.say("December of 12th, 2024")

engine.runAndWait()

@dp.message(Command("start"))
async def cmd_name(message: message):
    await message.answer("Hey, I am Sample Text bot")

@dp.message(Command("info"))
async def cmd_name(message: message):
    await message.answer("Here's a few comands: \n /start \n /info \n /name \n /test \n /button \n /special_button \n /films")

@dp.message(Command("name"))
async def cmd_name(message: message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Hello, <b> {args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer("Oh oh, looks like there is an error. Type your name after comand")

@dp.message(Command("test"))
async def cmd_name(message: message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")

@dp.message(Command("button"))
async def cmd_start(message: message):
    kb = [
        [types.KeyboardButton(text="English")],
        [types.KeyboardButton(text="Spanish")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Wich button is to press?", reply_markup=keyboard)

@dp.message(lambda message: message.text == "English")
async def first_btn(message: message):
    await message.reply("Who ever moves, is GAY")

@dp.message(lambda message: message.text == "Spanish")
async def second_btn(message: message):
    await message.reply("Quien se mueve, es GAY")

@dp.message(Command("special_button"))
async def cmd_special_buttons(message: types.message):
    kb = [
        [types.KeyboardButton(text="Phone number", request_contact=True)],
        [types.KeyboardButton(text="Quiz", request_poll=types.KeyboardButtonPollType(type='quiz'))]
    ]
    keyboard = types.ReplyKeyboardMarkup(keybord=kb)
    await message.reply("Wich button is to press?", replay_markup=keyboard)

@dp.message(F.contact_type == "animation")
async def echo_gif(message: message):
    await message.reply_animation(message.animation.file_id)    

@dp.message(lambda message: message.text == "Quiz")
async def send_quiz(message: types.message):
    question = "Wich Ocean is the biggest in the world?"
    options = ["Atlantic","Indian","Pacific","Arctic"]
    correct_option_id = 3

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_option_id,
        is_anonymous=False
    )



horror = ["https://www.kinopoisk.ru/film/64187/","https://www.kinopoisk.ru/film/8134/","https://www.kinopoisk.ru/film/453397/"]
action = ["https://www.kinopoisk.ru/film/389/","https://www.kinopoisk.ru/film/462360/","https://www.kinopoisk.ru/film/1267348/"]
fantasy = ["https://www.kinopoisk.ru/film/409424/","https://www.kinopoisk.ru/film/251733/","https://www.kinopoisk.ru/film/444/"]
humor = ["https://www.kinopoisk.ru/film/8124/","https://www.kinopoisk.ru/film/42664/","https://www.kinopoisk.ru/film/6039/"]

@dp.message(Command("films"))
async def cmd_name(message: message):
    await message.answer("Chouse the genre", reply_markup=btn_keyboard)

@dp.message(lambda message: message.text == "Horror")
async def show_horror(message: message):
    await message.reply("Have a good time watching your movie, " + random.choice(horror))

@dp.message(lambda message: message.text == "Action")
async def show_action(message: message):
    await message.reply("Have a good time watching your movie, " + random.choice(action))

@dp.message(lambda message: message.text == "Humor")
async def show_fantastic(message: message):
    await message.reply("Have a good time watching your movie, " + random.choice(fantasy))

@dp.message(lambda message: message.text == "Fantasy")
async def show_humor(message: message):
    await message.reply("Have a good time watching your movie, " + random.choice(humor))

@dp.message(Command("game"))
async def launch_game(message: message):
    def run_game():
        try:
            subprocess.Popen(r"C:\Program Files (x86)\Microsoft Studios\Minecraft Education Edition\Minecraft.Windows.exe")
            return "Game on"
        except FileNotFoundError:
            return "Game is not found"
    
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)

    await message.reply(response)

@dp.message(Command("weather"))
async def start_command(messeage: message):
    await message.answer("Wich city?")

@dp.message(F.text)
async def get_weather(message:types.message):
    city = message.text
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
        weather_date = requests.get(url).json()

        temperature = weather_date["main"]["temp"]
        temperature_feels = weather_date["main"]["feels_like"]
        wind_speed = weather_date['wind']['speed']
        cloud_cover = weather_date['weather'][0]['description']
        humidity = weather_date['main']['humidity']

        await message.answer(f"Temperature: (temperature)\n"
                            f"Fells like: (temperature_feels)\n"
                            f"Wind: (wind_speed) M/S \n"
                            f"Cloud: (cloud_cover) \n"
                            f"Humidity: (humidity)%")
        pass
    except KeyError:
        await message.answer("There is no city like that")  

@dp.message(Command("kys"))
async def cmd_name(message: message):
    await message.answer("no u")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

