from abc import ABC, abstractmethod

class Player(ABC):
    _symbol: str
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getMove(self, events: list = None, board: object = None):
        pass
    