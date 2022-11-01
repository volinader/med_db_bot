import psycopg2

#tg_bot
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters
from telegram.utils.request import Request
from urllib.parse import urlencode

#connect to db
def database_responde(answer):
    conn = None
    cursor = None
    ask = answer
    result_base = []
    try:

        conn = psycopg2.connect(
                host="postgres_db",
            database="med_db",
            user="root",
            password="example",
            port="5432")

        cursor = conn.cursor()
        #respond to db
        cursor.execute(f"SELECT name, additional_info FROM class_mkb WHERE code = '{ask}'")
        for i in cursor.fetchall():
            result_base.append(i)
        conn.commit()
    except Exception as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
    return result_base

#tg bot
API_key = '' #put your api token
def message_handler(update, context):
    answer = update.message.text
    feedback_from_base = database_responde(answer)
    print(answer)
    which_code = f'Respond for code {answer} is: \n {str(feedback_from_base)}'
    update.message.reply_text(which_code)

def main():
    req=Request(connect_timeout=0.5)
    t_bot=Bot(request=req, token=API_key)
    updater=Updater(bot=t_bot, use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()