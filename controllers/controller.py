from view.input import Input
from view.output import Output
from view.paths import paths, crud_paths
from models.team import Team
from models.game import Game

#class that defines app route (page)
class Route:
    def __init__(self, route_builder):
        self.path = route_builder.path
        self.menu = route_builder.menu
        self.parent = route_builder.parent
        self.children = route_builder.children
        for c in self.children:
            c.parent = self
    #
    def _find_child_by_path(self, path):
        return next((c for c in self.children if path == c.path), None)
    #returns user to previous route
    def _get_back(self):
        if hasattr(self, 'data') and self.data is not None:
            self.data = None
        return True
    #writes data to file and returns user to previous route
    def _save_and_get_back(self):
        if self.path == crud_paths.get('add'):
            self.data_type.add(self.data)
        elif self.path == crud_paths.get('rem'):
            self.data_type.remove(self.data)
        elif self.path == crud_paths.get('upd'):
            self.data_type.update(self.data)
        elif self.path == crud_paths.get('add_team'):
            self.parent.data_type.addTeam(self.parent.data, self.data)
        elif self.path == crud_paths.get('add_game'):
            self.parent.data.games.append(self.data.__dict__)
        return True
    #displays next route 
    def _handle_next_route(self, next_route):
        next_route.display()
        return False
    #displays current route 
    def display(self):
        while True:
            Output.clear_screen()
            self.display_data()
            self.invoke_cud_menu()
            if self.invoke_main_menu():
                break
    #displays main menu 
    def invoke_main_menu(self):
        Output.display_list(self.menu)
        next_route_path = Input.get_input()
        if next_route_path == paths.get('back'):
            return self._get_back()
        elif next_route_path == crud_paths.get('save'):
            return self._save_and_get_back()
        next_route = self._find_child_by_path(next_route_path)
        if next_route:
            return self._handle_next_route(next_route)
    #displays create\update\delete menu 
    def invoke_cud_menu(self):
        pass
    #displays data in json
    def display_data(self):
        pass


class DataRoute(Route):
    def __init__(self, route_builder):
        Route.__init__(self, route_builder)
        self.data_type = route_builder.data_type

    def display_data(self):
        data = None
        if self.path == crud_paths.get('show_all'):
            data = self.data_type.getAll()
        else:
            data_name = Input.get_input('Enter object\'s name (id):')
            data = self.data_type.getByName(data_name)
        Output.display_json(data)

#route 
class CudRoute(Route):
    def __init__(self, route_builder):
        Route.__init__(self, route_builder)
        self.data_type = route_builder.data_type
        self.data = route_builder.data

    def invoke_cud_menu(self):
        if self.path == crud_paths.get('add') or self.path == crud_paths.get('upd'):
            name = Input.get_input('Item\'s name:')
            if name != '' and self.path == crud_paths.get('add'):
                self.data = self.data_type(name)
            elif self.path == crud_paths.get('upd'):
                self.data = self.data_type.getByName(name)

        elif self.path == crud_paths.get('rem'):
            self.data = Input.get_input('Name of item to remove:')
        elif self.path == crud_paths.get('add_team'):
            name = Input.get_input('Team\'s name:')
            strength = int(Input.get_input('Team\'s strength:'))
            self.data = Team(name, strength)
        elif self.path == crud_paths.get('add_game'):
            host = Input.get_input('Host team:')
            guest = Input.get_input('Host team:')
            hostGoals = int(Input.get_input('Host score:'))
            guestGoals = int(Input.get_input('Guest score:'))
            self.data = Game(
                host, guest, {'hostGoals': hostGoals, 'guestGoals': guestGoals})


class RouteBuilder:
    def __init__(self):
        self.path = paths.get('default')
        self.menu = []
        self.children = []
        self.parent = None
        self.data_type = None
        self.data = None

    def set_path(self, path):
        self.path = path
        return self

    def set_children(self, children):
        self.children = children
        return self

    def set_menu(self, menu):
        self.menu = menu
        return self

    def set_parent(self, parent):
        self.parent = parent
        return self

    def set_data_type(self, data_type):
        self.data_type = data_type
        return self

    def set_data(self, data):
        self.data = data
        return self


class App:
    def __init__(self, main_page):
        if main_page.parent is None:
            self.main_page = main_page
        else:
            self.main_page = None

    def start(self):
        if self.main_page is not None:
            self.main_page.display()
