import csv
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from transformers import *
from oz import connection




def chek_chat_id_(chat):
    with connection.cursor() as cur2:
        cur2.execute(f"select chat_id  from users where chat_id='{chat}'")
        check = cur2.fetchall()
        return check





def get_member_tasks_message(cards):
    msg = ""
    for index , card in enumerate(cards):
        msg+=f"{index+1}. <a href=\'{card.get('url')}\'>{cards.get('card_name')}</a>\n"
    return msg
