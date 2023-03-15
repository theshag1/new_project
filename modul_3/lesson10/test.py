from trello import TrelloClient
from trello.exceptions import ResourceUnavailable

client = TrelloClient(
    api_key='<your_api_key>',
    api_secret='<your_api_secret>',
    token='<your_oauth_token>',
    token_secret='<your_oauth_token_secret>'
)

try:
    board = client.get_board('<your_board_id>')
    lists = board.list_lists()
    for l in lists:
        print(l.name)
except ResourceUnavailable as e:
    print('Trello APIdan xatolik:', e)
