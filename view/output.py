from os import system, name
import json


class Output:
    @staticmethod
    def display_list(menu_items):
        if menu_items is not None:
            [print(i) for i in menu_items]

    @staticmethod
    def display_json(data):
        if data is not None:
            print(json.dumps(data, indent=4))

    @staticmethod
    def clear_screen():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
