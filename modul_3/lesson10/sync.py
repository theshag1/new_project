from psycopg2.extras import RealDictCursor

from oz import connection
import queries
from fortrello import TrelloManager


def sync_board(trello_username):  # islomovibrohimjon
    trello = TrelloManager(trello_username)
    boards = trello.get_boards()  # [{'id': '63ea22a4dd3aa382a077fb9f', 'nodeId': 'ari:cloud:trello::board/workspace/63ea22a4dd3aa382a077fb86/63ea22a4dd3aa382a077fb9f', 'name': 'P10', 'desc': '', 'descData': None, 'closed': False, 'dateClosed': None, 'idOrganization': '63ea22a4dd3aa382a077fb86', 'idEnterprise': None, 'limits': {'attachments': {'perBoard': {'status': 'ok', 'disableAt': 36000, 'warnAt': 28800}, 'perCard': {'status': 'ok', 'disableAt': 1000, 'warnAt': 800}}, 'boards': {'totalMembersPerBoard': {'status': 'ok', 'disableAt': 1600, 'warnAt': 1280}, 'totalAccessRequestsPerBoard': {'status': 'ok', 'disableAt': 4000, 'warnAt': 3200}}, 'cards': {'openPerBoard': {'status': 'ok', 'disableAt': 5000, 'warnAt': 4000}, 'openPerList': {'status': 'ok', 'disableAt': 5000, 'warnAt': 4000}, 'totalPerBoard': {'status': 'ok', 'disableAt': 2000000, 'warnAt': 1600000}, 'totalPerList': {'status': 'ok', 'disableAt': 1000000, 'warnAt': 800000}}, 'checklists': {'perBoard': {'status': 'ok', 'disableAt': 1800000, 'warnAt': 1440000}, 'perCard': {'status': 'ok', 'disableAt': 500, 'warnAt': 400}}, 'checkItems': {'perChecklist': {'status': 'ok', 'disableAt': 200, 'warnAt': 160}}, 'customFields': {'perBoard': {'status': 'ok', 'disableAt': 50, 'warnAt': 40}}, 'customFieldOptions': {'perField': {'status': 'ok', 'disableAt': 50, 'warnAt': 40}}, 'labels': {'perBoard': {'status': 'ok', 'disableAt': 1000, 'warnAt': 800}}, 'lists': {'openPerBoard': {'status': 'ok', 'disableAt': 500, 'warnAt': 400}, 'totalPerBoard': {'status': 'ok', 'disableAt': 3000, 'warnAt': 2400}}, 'stickers': {'perCard': {'status': 'ok', 'disableAt': 70, 'warnAt': 56}}, 'reactions': {'perAction': {'status': 'ok', 'disableAt': 900, 'warnAt': 720}, 'uniquePerAction': {'status': 'ok', 'disableAt': 17, 'warnAt': 14}}}, 'pinned': False, 'starred': False, 'url': 'https://trello.com/b/rAWuxf08/p10', 'prefs': {'permissionLevel': 'private', 'hideVotes': False, 'voting': 'disabled', 'comments': 'members', 'invitations': 'members', 'selfJoin': False, 'cardCovers': True, 'isTemplate': False, 'cardAging': 'regular', 'calendarFeedEnabled': False, 'hiddenPluginBoardButtons': [], 'switcherViews': [{'viewType': 'Board', 'enabled': True, '_id': '63ea22a4dd3aa382a077fba0', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba0'}, {'viewType': 'Table', 'enabled': True, '_id': '63ea22a4dd3aa382a077fba1', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba1'}, {'viewType': 'Calendar', 'enabled': False, '_id': '63ea22a4dd3aa382a077fba2', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba2'}, {'viewType': 'Dashboard', 'enabled': False, '_id': '63ea22a4dd3aa382a077fba3', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba3'}, {'viewType': 'Timeline', 'enabled': False, '_id': '63ea22a4dd3aa382a077fba4', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba4'}, {'viewType': 'Map', 'enabled': False, '_id': '63ea22a4dd3aa382a077fba5', 'typeName': 'SwitcherViews', 'id': '63ea22a4dd3aa382a077fba5'}], 'background': '63ea14a489b77288b9d89851', 'backgroundColor': None, 'backgroundImage': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/original/15fef5e25c20ace59280bfd8e925e0e7/photo-1675458349418-b6e8215f1d6b', 'backgroundImageScaled': [{'width': 67, 'height': 100, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/67x100/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 128, 'height': 192, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/128x192/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 320, 'height': 480, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/320x480/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 640, 'height': 960, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/640x960/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 683, 'height': 1024, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/683x1024/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 853, 'height': 1280, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/853x1280/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 1066, 'height': 1600, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/1066x1600/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 1280, 'height': 1920, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/1280x1920/dd4a866597818404cfebcd11cccc425b/photo-1675458349418-b6e8215f1d6b.jpg'}, {'width': 1365, 'height': 2048, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/original/15fef5e25c20ace59280bfd8e925e0e7/photo-1675458349418-b6e8215f1d6b'}], 'backgroundTile': False, 'backgroundBrightness': 'dark', 'backgroundBottomColor': '#868385', 'backgroundTopColor': '#aab3b9', 'canBePublic': True, 'canBeEnterprise': True, 'canBeOrg': True, 'canBePrivate': True, 'canInvite': True}, 'shortLink': 'rAWuxf08', 'subscribed': False, 'labelNames': {'green': '', 'yellow': '', 'orange': '', 'red': '', 'purple': '', 'blue': 'gui', 'sky': 'bot', 'lime': 'announcememts', 'pink': 'android', 'black': 'iOS', 'green_dark': 'frontent', 'yellow_dark': '', 'orange_dark': '', 'red_dark': 'error', 'purple_dark': '', 'blue_dark': '', 'sky_dark': '', 'lime_dark': '', 'pink_dark': '', 'black_dark': '', 'green_light': 'backend', 'yellow_light': '', 'orange_light': '', 'red_light': '', 'purple_light': '', 'blue_light': '', 'sky_light': '', 'lime_light': '', 'pink_light': '', 'black_light': ''}, 'powerUps': [], 'dateLastActivity': '2023-03-10T11:43:25.452Z', 'dateLastView': '2023-03-10T22:35:00.757Z', 'shortUrl': 'https://trello.com/b/rAWuxf08', 'idTags': [], 'datePluginDisable': None, 'creationMethod': 'automatic', 'ixUpdate': '715', 'templateGallery': None, 'enterpriseOwned': False, 'idBoardSource': None, 'premiumFeatures': ['additionalBoardBackgrounds', 'additionalStickers', 'customBoardBackgrounds', 'customEmoji', 'customStickers', 'plugins'], 'idMemberCreator': '63e9d509205aef8fd7069794', 'memberships': [{'idMember': '63e9d509205aef8fd7069794', 'memberType': 'admin', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22a4dd3aa382a077fbaa'}, {'idMember': '63ea2270d626f4ccafa6ff6b', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22df359fa4e94aa40ae2'}, {'idMember': '626566d47279b31f29f1121f', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22e1b64b232b58a2fb25'}, {'idMember': '63e389bbd86539e63e742e92', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22e56ab7721d33796db4'}, {'idMember': '63e37c6518095d6965e88428', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22ea128c070feaae6cc5'}, {'idMember': '63ea22281627e1830b03f4cf', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22ea924da00eb0ca0da2'}, {'idMember': '63ea225dc56d8690c50485f0', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22eb0f9909c7440de1a1'}, {'idMember': '63ea22372edd1230dbc83c07', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea22ee7aaa01a6d131abe8'}, {'idMember': '63ea22629c9669c3c0f0a83f', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea230db7a00ad3d4671cb3'}, {'idMember': '63ea227728ee0b875a66f2f5', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea23122c2a3ddcb9234cbc'}, {'idMember': '63ea22aa9d3776a08fb32bc4', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea232bbe1522d0bd1d7c4e'}, {'idMember': '63ea22f4ffbd3c26f2523e84', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea2335087f5a2e1c4b3736'}, {'idMember': '63ea2252ec8a5141c9ba640b', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea23410246fb79f5513270'}, {'idMember': '63ea22cf2803a40c1aec0ff6', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea235a72c335923a7f585e'}, {'idMember': '63ea226cab04b3d79fb6049e', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea236aad3a7db5b42d6882'}, {'idMember': '63ea241c656766291b405b56', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ea241e8a9f70bd81bd8cca'}, {'idMember': '63eca904fec862fc5de5d891', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63eca90675d9eefcca8f9f51'}, {'idMember': '63ee0da8181dba69698dafac', 'memberType': 'normal', 'unconfirmed': False, 'deactivated': False, 'id': '63ee0daa83cdc7ab3ac506b0'}]}]

    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        for board in boards:
            user = trello.get_member_id()
            id = user
            trello_board_id = board.get('id')  # 63ea22a4dd3aa382a077fb9f
            cur.execute(queries.UPSERT_BOARDS, (board.get('name'), trello_board_id))  # write boards database
            connection.commit()
            cur.execute(queries.select_board_by_trello_id, (trello_board_id,))  # 63ea22a4dd3aa382a077fb9f
            db_board = cur.fetchall()  # [RealDictRow([('id', 1), ('name', 'P10'), ('trello_id', '63ea22a4dd3aa382a077fb9f')])]

            sync_board_users([member.get('idMember') for member in boards[0].get('memberships')]
                             , db_board[0].get('id'))
        # sync_board_users([member.get('idMember') for member in boards[0].get('memberships')]
        #                  , db_board[0].get('id'))
        for db in db_board:
            sync_lists(trello, trello_board_id, db.get('id'))
        # print(sync_lists(trello, trello_board_id, db_board.get('id')))


"""
a = ['63e9d509205aef8fd7069794', '63ea2270d626f4ccafa6ff6b',
 '626566d47279b31f29f1121f', '63e389bbd86539e63e742e92',
     '63e37c6518095d6965e88428', '63ea22281627e1830b03f4cf', '63ea225dc56d8690c50485f0', '63ea22372edd1230dbc83c07',
     '63ea22629c9669c3c0f0a83f', '63ea227728ee0b875a66f2f5',
      '63ea22aa9d3776a08fb32bc4', '63ea22f4ffbd3c26f2523e84',
     '63ea2252ec8a5141c9ba640b', '63ea22cf2803a40c1aec0ff6', '63ea226cab04b3d79fb6049e', '63ea241c656766291b405b56',
     '63eca904fec862fc5de5d891', '63ee0da8181dba69698dafac', '640f08452d638e6fd01cd000']
"""


def sync_board_users(board_member_ids, board_id):
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        for member_id in board_member_ids:
            cur.execute(queries.get_user_by_trello_id, (member_id,))
            user = cur.fetchone()
            if user:
                cur.execute(queries.UPSERT_BOARD_USERS, (board_id, user.get("id")))
                connection.commit()


def sync_lists(trello, tre_bord_id, board_id):
    board_lists = trello.get_lists_on_a_board(tre_bord_id)
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        for board_list in board_lists:
            cur.execute(
                queries.UPSERT_lists, (board_list.get('name'), board_list.get('id'), board_id,)

            )
            connection.commit()


