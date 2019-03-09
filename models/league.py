import json

class League:
    def __init__(self, name):
        self.__teams = self.__games = []
        self.name = name

    def __init__(self, name, teams):
        self.__teams = teams
        self__name = name
        self.__games = []

    def playGame(self, team1, team2):
        index1 = self.__teams.index(team1)
        index2 = self.__teams.index(team2)
        # if index1 != index2:
        #     self._games.append(Game(team1, team2))
    
    def addTeam(self, team):
        self.__teams.append(team)