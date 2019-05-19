import json

from .game import Game

DATA_PATH = './data/leagues.json'
DATA_FILE = open(DATA_PATH, 'rw')


class League:
    def __init__(self, name, teams=set()):
        self.teams = teams
        self.name = name
        self.games = set() #each team has to play 2 games (being a host and a guest) with all of the others

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.name == other.name:
            return self.teams == other.teams and self.games == other.games
        return False

    def __ne__(self, other): 
        return self.name != other.name or self.teams != other.teams or self.games != other.games

    @staticmethod
    def getAll():
        try:
            return json.load(DATA_FILE)
        except:
            print('Goddammit')
        return []

    @staticmethod
    def add(league):
        try:
            leagues = json.load(DATA_FILE)
            leagues.append(league)
            json.dump(leagues, DATA_FILE)
        except:
            print('Goddammit')

    @staticmethod
    def remove(league):
        try:
            leagues = json.load(DATA_FILE)
            leagues.remove(league)
            json.dump(leagues, DATA_FILE)
        except:
            print('Goddammit')
    
    @staticmethod
    def getByName(name):
        try:
            leagues = json.load(DATA_FILE)
            targetLeague = next((x for x in leagues if x.name != name), None)
            return targetLeague
        except:
            print('Goddammit')
        return None
    # @staticmethod
    # def update(league, index):
    #     data = json.load(DATA_FILE)
    #     data.leagues[index] = league
    #     json.dump(data, DATA_FILE)

    # @staticmethod
    # def remove(league):
    #     data = json.load(DATA_FILE)
    #     data.leagues.remove(league)
    #     json.dump(data, DATA_FILE)
    # def __init__(self, name, teams):
    #     self.__teams = teams
    #     self__name = name
    #     self.__games = []

    # def playGame(self, team1, team2):
    #     index1 = self.__teams.index(team1)
    #     index2 = self.__teams.index(team2)
    #     if index1 != index2:
    #         self._games.append(Game(team1, team2))

    # def addTeam(self, team):
    #     self.__teams.append(team)
