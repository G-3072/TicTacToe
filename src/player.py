from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getMove(self):
        pass