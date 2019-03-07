class League:
    def __init__(self):
        self._teams = self._games = []
    
    def __init__(self, teams):
        self._teams = teams
        self._games = []
    
    @property
    def teams(self) {
        return self._teams
    }

    @teams.setter
    def teams(self, team):
        self._teams.append(team)
    
    @teams.deleter
    def teams(self, team):
        self._teams.remove(team)

    