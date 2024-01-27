import os
from dotenv import load_dotenv
import logging
import keyboards as kb
import promts
from aiogram import Bot, Dispatcher, types, executor
from gig_api import gigachat_response
from history import add_to_history

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
assert BOT_TOKEN is not None, "BOT_TOKEN is None"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
current_role = promts.base_prompt


@dp.message_handler(commands=['start','help'])
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.username}!\n"
        "Я бот, который посылает запросы в Гигачат от Сбера\n"
        "Чтобы изучить данный сервис, ты можешь перейти по ссылке ниже\n"
        "Также для получения дополнительного функционала можешь посмотреть раздел 'Меню'."
    )
    await message.answer('Ссылка на Гигачат:',reply_markup=kb.gigachat_urlkb)
    
@dp.message_handler(commands='chooserole')
async def role_handler(message: types.Message):
    await message.answer(
        text='Мои роли перечислены в списке ниже. \n'
             'Можешь выбрать любую. ',
        reply_markup=kb.roles_list_kb
    )

@dp.callback_query_handler(lambda callback: True)
async def callback_role(callback: types.CallbackQuery):
    for role in kb.roles_list:
        if callback.data == role:
            global current_role
            current_role = role
            await callback.answer(text=f'Вы выбрали роль {role}')


@dp.message_handler()
async def message_handler(message: types.Message):
    global current_role
    # Добавление сообщения пользователя в историю - 1
    add_to_history('user', message.text)
    response = gigachat_response(message.text, current_role)
    # Добавление ответа GigaChat в историю -
    add_to_history('assistant', response)
    # print(chat_history)
    await message.answer(response) 
            

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates= True)