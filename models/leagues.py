import json

DATA_PATH = './data/leagues.json'
DATA_FILE = open(DATA_PATH, 'rw')


class Leagues:
        

    @staticmethod
    def add(league):
        data = json.load(DATA_FILE)
        data.leagues.append(league)
        data.nextId += 1
        json.dump(data, DATA_FILE)

    @staticmethod
    def update(league, index):
        data = json.load(DATA_FILE)
        data.leagues[index] = league
        json.dump(data, DATA_FILE)

    @staticmethod
    def remove(index):
        data = json.load(DATA_FILE)
        data.leagues.pop(index)
        json.dump(data, DATA_FILE)

    @staticmethod
    def remove(league):
        data = json.load(DATA_FILE)
        data.leagues.remove(league)
        json.dump(data, DATA_FILE)
