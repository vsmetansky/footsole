from view.input import Input
from view.output import Output
from models.team import Team


class Page:
    def __init__(self, children, menu, input_menu, code='', parent=None, data_type=None):
        self.code = code
        self.parent = parent
        self.menu = menu
        self.input_menu = input_menu
        self.data_type = data_type
        self.children = children
        for c in self.children:
            c.parent = self

    def _find_child_by_code(self, code):
        return next((c for c in self.children if code == c.code), None)

    def _get_data(self, item_name):
        try:
            if item_name == '':
                return data_type.getAll()
            else:
                return data_type.getByName(item_name)
        except:
            return None

    def _get_user_data(self):
        if self.data_type is not None:
            input_data = {s: Input.get_input(s) for s in self.input_menu}
            new_item = self.data_type()
            for attr, value in input_data:
                setattr(new_item, attr, value)
            return new_item

    def _parent_add_item(self, parent_item, item):
        if isinstance(item, Team):
            parent_item.teams.append(item)
        else:
            parent_item.games.append(item)

    def show(self, parent_item=None, item_name=''):
        while True:
            Output.clear_screen()
            Output.show_json(self._get_data(item_name))
            new_item = self._get_user_data()
            Output.show_menu(self.menu)
            code = Input.get_input()
            if code == "<" and self.parent is not None:
                break
            elif code == "$":
                self._parent_add_item(parent_item, new_item)
                break
            nextPage = self._find_child_by_code(code)
            if nextPage:
                nextPage.show()


class App:
    def __init__(self, main_page):
        if main_page.parent is None:
            self.main_page = main_page
        else:
            self.main_page = None

    def start(self):
        if self.main_page is not None:
            self.main_page.show()
