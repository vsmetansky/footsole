MAIN_MENU = [
    '[a]dmin',
    '[c]lient'
]

ADMIN_MENU = [
    '[a]dd league',
    '[u]pdate league',
    '[l]eagues display',
    '[b]y name display',
    '[<]back'
]

CLIENT_MENU = [
    '[l]eagues display',
    '[b]y name display',
    '[<]back'
]

LEAGUE_INPUT = [
    'name'
]

TEAM_INPUT = [
    'name',
    'strength'
]

GAME_INPUT = [
    'host',
    'guest',
    'host_goals',
    'guest_goals'
]

ADD_LEAGUE_MENU = [
    '[t]eam add',
    '[m]atch add',
    '[$]save',
    '[<]back'
]

CREATE_MENU = [
    '[$]save',
    '[<]back'
]

ITEM_MENU = [
    '[<]back'
]


def main():
    # self, children, menu, input_menu, code='', parent=None, data_type=None
    leagues_page = Page([], ITEM_MENU, [], 'l', None, League)
    client_page = Page([leagues_page], CLIENT_MENU, [], 'c')
    admin_page = Page([], ADMIN_MENU, [], 'a')
    main_page = Page([admin_page, client_page], MAIN_MENU, [])
    app = App(main_page)
    app.start()


if __name__ == "__main__":
    from models.league import League    
    from controllers.controller import Page
    from controllers.controller import App
    main()
