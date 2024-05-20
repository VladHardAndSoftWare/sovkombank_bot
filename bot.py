import os

from dotenv import load_dotenv

# filters
from tgbot.filters.admin_filter import AdminFilter
from telebot import custom_filters

# handlers
# from tgbot.handlers.admin import admin
from tgbot.handlers.user import any_user
from tgbot.handlers.test_DB_handler_CREATE import test_DB_handler_func_CREATE
from tgbot.handlers.test_DB_handler_READ import test_DB_handler_func_READ
from tgbot.handlers.test_DB_handler_UPDATE import test_DB_handler_func_UPDATE
from tgbot.handlers.test_DB_handler_DELETE import test_DB_handler_func_DELETE
from tgbot.handlers import client_inspection as ci
from tgbot.handlers import client_cabinet as cc
from tgbot.handlers.register_example import start_ex, name_get, ready_for_answer
from tgbot.states.inspection_state import inspection, autoinspection, cabinet, admin
from tgbot.handlers.test_DB_handler_IMAGE import test_DB_handler_func_IMAGE
from tgbot.handlers import admin_cabinet as ac


# states
from tgbot.states.register_state import Register

# States storage
from telebot.storage import StateMemoryStorage

# utils
# from tgbot.utils.database import Database

# telebot
from telebot import TeleBot

# db = Database()

load_dotenv()
TOKEN = os.environ['TELEGRAM_TOKEN']

os.makedirs('images', exist_ok=True)
os.makedirs('images_masks', exist_ok=True)

state_storage = StateMemoryStorage()
# I recommend increasing num_threads
bot = TeleBot(TOKEN, num_threads=5, state_storage=state_storage)



def register_handlers():
    # bot.register_message_handler(admin_user, commands=['start_reg'], admin=True, pass_bot=True)
    bot.register_message_handler(ac.admin_1_handler, commands=['start_admin_1_handler'], pass_bot=True)
    bot.register_message_handler(any_user, commands=['start_reg'], admin=False, pass_bot=True)
    bot.register_message_handler(test_DB_handler_func_CREATE, commands=['test_DB_CREATE'], pass_bot=True)
    bot.register_message_handler(test_DB_handler_func_READ, commands=['test_DB_READ'], pass_bot=True)
    bot.register_message_handler(test_DB_handler_func_UPDATE, commands=['test_DB_UPDATE'], pass_bot=True)
    bot.register_message_handler(test_DB_handler_func_DELETE, commands=['test_DB_DELETE'], pass_bot=True)
    bot.register_message_handler(start_ex, commands=['register'], pass_bot=True)
    bot.register_message_handler(name_get, state=Register.name, pass_bot=True)
    bot.register_message_handler(ready_for_answer, state=Register.surname, pass_bot=True)
    bot.register_message_handler(ci.debug, commands=['debug'], pass_bot=True)
   
    
    # bot.register_message_handler(test_DB_handler_func_IMAGE, content_types=['photo'], admin=False, pass_bot=True)
    
register_handlers()

def client_cabinet():
    bot.register_message_handler(cc.welcome_cabinet, commands=['start'], pass_bot=True)
    bot.register_message_handler(cc.body_cabinet,  state=cabinet.body, pass_bot=True)
    bot.register_message_handler(cc.choise_object,  state=cabinet.choise_object, pass_bot=True)
    bot.register_message_handler(cc.automodel,  state=cabinet.automodel, pass_bot=True)
    bot.register_message_handler(cc.autonumber,  state=cabinet.autonumber, pass_bot=True)
    bot.register_message_handler(cc.autospec,  state=cabinet.autospec, pass_bot=True)
    bot.register_message_handler(cc.res,  state=cabinet.res, pass_bot=True)
    
client_cabinet()

def client_inspection():
    bot.register_message_handler(ci.start_inspection, state=cabinet.start_inspection, pass_bot=True)
    bot.register_message_handler(ci.body_inspection,  state=inspection.body, pass_bot=True)
    # bot.register_message_handler(ci.task1_1, state=autoinspection.task1_1, pass_bot=True)
    bot.register_message_handler(ci.task1_answer, state=autoinspection.task1_answer, pass_bot=True)
    bot.register_message_handler(ci.task2_1, state=autoinspection.task2_1, pass_bot=True)
    bot.register_message_handler(ci.task2_2, state=autoinspection.task2_2, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_3, state=autoinspection.task2_3, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_4, state=autoinspection.task2_4, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_5, state=autoinspection.task2_5, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_6, state=autoinspection.task2_6, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_7, state=autoinspection.task2_7, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_8, state=autoinspection.task2_8, content_types=['photo'], pass_bot=True)
    bot.register_message_handler(ci.task2_answer, state=autoinspection.task2_answer, pass_bot=True)
    bot.register_message_handler(ci.task3_1, state=autoinspection.task3_1, pass_bot=True)
    bot.register_message_handler(ci.task3_answer, state=autoinspection.task3_answer, pass_bot=True)
    bot.register_message_handler(ci.waiting, state=inspection.waiting, pass_bot=True)
    
client_inspection()

def admin_cabinet():
    bot.register_message_handler(ac.admin_start, commands=['start_admin'], pass_bot=True)
    bot.register_message_handler(ac.list_orders,  state=admin.list_orders, pass_bot=True)
    bot.register_message_handler(ac.order_data,  state=admin.order_data, pass_bot=True)
    bot.register_message_handler(ac.change_status,  state=admin.change_status, pass_bot=True)
    
admin_cabinet()

# custom filters
bot.add_custom_filter(AdminFilter())
bot.add_custom_filter(custom_filters.StateFilter(bot))

def run():
    bot.infinity_polling()

run()
