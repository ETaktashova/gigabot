from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# роли
roles_list_kb = InlineKeyboardMarkup(row_width=1)
r1 = InlineKeyboardButton(text='Программист', callback_data='Программист')
r2 = InlineKeyboardButton(text='Юрист', callback_data='Юрист')
r3 = InlineKeyboardButton(text='Экономист', callback_data='Экономист')
r4 = InlineKeyboardButton(text='Менеджер по продажам', callback_data='Менеджер по продажам')
r5 = InlineKeyboardButton(text='HR-специалист', callback_data='HR-специалист')
r6 = InlineKeyboardButton(text='Ученик', callback_data='Ученик')
r7 = InlineKeyboardButton(text='Филолог', callback_data='Филолог')
r8 = InlineKeyboardButton(text='Тренер', callback_data='Тренер') 
roles_list_kb.add(r1, r2 , r3, r4, r5, r6, r7)
roles_list = ['Программист','Юрист','Экономист','Менеджер по продажам','HR-специалист','Ученик','Филолог', 'Тренер']

# гигачат старт и ссылка
gigachat_urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Сайт Гигачата', url='https://developers.sber.ru/link/freeapi')
gigachat_urlkb.add(urlButton)



