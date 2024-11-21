from abc import ABC, abstractmethod

class Player(ABC):
    symbol: str
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getMove(self, events: list = None):
        pass