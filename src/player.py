from abc import ABC, abstractmethod

class Player(ABC):
    _symbol: str
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getMove(self, events: list = None, board: object = None):
        pass
    
    
class test(Player):
    def __init__(self):
        self._symbol = "X"
    
    def getSymbol(self):
        return self._symbol
    
    def getMove(self):
        pass
    