class Game: 
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.__score = dict()

    @property 
    def score(self):
        return self.__score