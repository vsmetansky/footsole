class Event: 
    def __init__(self):
        self.__handlers = []
    def addHandler(self, handler):
        self.__handlers.append(handler)
    def fire(self):
        [h.handle() for h in self.__handlers]
        