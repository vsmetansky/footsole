import random, math

class Game: 
    def __init__(self, host, guest):
        self.host = host
        self.guest = guest
        self.score = {
            self.host: math.floor(host.strength * random.uniform(0, 1)),
            self.guest: math.floor(guest.strength * random.uniform(0, 1))
        }

    def __eq__(self, other): 
        if isinstance(other, self.__class__):
            return self.host == other.host and self.guest == other.guest and self.score == other.score 
        return False

    def __ne__(self, other):
        return self.host != other.host or self.guest != other.guest or self.score != other.score