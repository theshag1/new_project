# User
select_all_user = 'select  * from users '
get_chat_id = 'select * from users where chat_id=%s'

get_board = '''
select name from boards where trello_id = %s
'''

get_list_for_user = '''
select name from lists where trello_id=%s

'''

write_user = '''
    insert into 
    users(chat_id, first_name, last_name, username)
    values (%s ,%s, %s,%s)
'''

update_user_trellochat_id = """
    update users
    set trello_username = %s , trello_id = %s
    where chat_id=%s
"""
UPSERT_BOARDS = """
    insert into boards(name, trello_id)
    values (%s, %s)
    on conflict (trello_id)
    do update set name=excluded.name 
"""

select_board_by_trello_id = 'select * from boards where trello_id =%s'

UPSERT_lists = """
insert into lists (name, trello_id, board_id) VALUES (%s , %s, %s)
on conflict (trello_id)
do update set name=excluded.name , board_id=excluded.board_id
"""

UPSERT_listss = '''
insert into lists (name, trello_id, board_id) VALUES (%s, %s, %s)
'''

get_user_by_trello_id = """
select * from users where trello_id=%s
"""

upsert_board_user = """
insert into boards_users(board_id, user_id) 
values (%s , %s)
on conflict (board_id, user_id)
do nothing
"""
get_user_by_board_id = '''select c.name as card_name  , url from cards_users cu 
                       inner join cards c on c.id = cu.card_id
                       inner join lists l on c.list_id = l.id
                       inner join boards b on b.id = l.board_id
                       where b.id = %s and cu.user_id=%s
'''
get_user_board = '''
                     select b.name as name , b.id as board_id  from boards_users bu
                     inner join boards b on bu.board_id = b.id
                      where bu.user_id  = %s

'''

# Board Users
UPSERT_BOARD_USERS = """
    insert into boards_users(board_id, user_id)
    values (%s, %s)
    on conflict (board_id, user_id)
    do nothing
"""
