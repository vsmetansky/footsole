import json

from models.game import Game

DATA_PATH = './data/leagues.json'


class League:
    def __init__(self, name, teams=[], games=[]):
        self.teams = teams
        self.name = name
        self.games = games

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.name == other.name:
            return self.teams == other.teams and self.games == other.games
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.name != other.name or self.teams != other.teams or self.games != other.games
        return True
    #returns all of the leagues
    @staticmethod
    def getAll():
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    #returns league with specified name
    @staticmethod
    def getByName(name):
        with open(DATA_PATH, 'r') as f:
            leagues = json.load(f)
            targetLeague = next(
                (x for x in leagues if x.get('name') == name), None)
            return targetLeague
    #adds given league to leagues array and writes it to file
    @staticmethod
    def add(league):
        with open(DATA_PATH, 'r') as f:
            leagues = json.load(f)
            nameMatch = next(
                (x for x in leagues if x.get('name') == league.name), None)
            if nameMatch is None:
                leagues.append(league.__dict__)
        with open(DATA_PATH, 'w') as f:
            json.dump(leagues, f)
    #removes league by name 
    @staticmethod
    def remove(name):
        with open(DATA_PATH, 'r') as f:
            leagues = json.load(f)
            targetLeague = next(
                (x for x in leagues if x.get('name') == name), None)
            leagues.remove(targetLeague)
        with open(DATA_PATH, 'w') as f:
            json.dump(leagues, f)
    #updates league 
    @staticmethod
    def update(league):
        with open(DATA_PATH, 'w') as f:
            leagues = json.load(f)
            leagueIndex = leagues.index(league)
            leagues[leagueIndex] = league
        with open(DATA_PATH, 'w') as f:
            json.dump(leagues, f)
    #adds team to specified league
    @staticmethod
    def addTeam(league, team):
        nameMatch = next(
            (x for x in league.teams if x.get('name') == team.name), None)
        if nameMatch is None:
            league.teams.append(team.__dict__)