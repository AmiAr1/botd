# from aiogram import types, Dispatcher
# from config import bot, ADMIN
# from handlers import extra
# import random
#
#
# async def game(message: types.Message):
#     if message.text.startswith('game'):
#         if message.chat.type != 'private':
#             if message.from_user.id == ADMIN:
#                 emg = ['🎯', '🎳', '🎰', '🎲', '⚽', '🏀']
#                 r_emg = random.choice(emg)
#                 await bot.send_dice(message.chat.id, emoji=r_emg)
#             else:
#                 await message.answer('ты не повелитель!!!!!!!')
#
#         else:
#             await message.answer('это работает только в чатах')
#     else:
#         await extra.register_handlers_extra()
#
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(game, commands=['game'])
