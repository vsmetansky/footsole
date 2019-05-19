class Team:
    # strength: an int from 1 to 10 that specifies team strength

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength if 1 <= strength <= 10 else 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.strength == other.strength
        return False

    def __ne__(self, other):
        return self.name != other.name or self.strength != other.strength