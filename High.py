from abc import ABC, abstractmethod
class IHealer(ABC):

    @abstractmethod
    def getHealth(self):
        pass

    @abstractmethod
    def getMaxHealth(self):
        pass

    @abstractmethod
    def setHealth(self, value):
        pass

    @abstractmethod
    def setMaxHealth(self, value):
        pass


class INamer(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, value):
        pass

class IDestroyer(ABC):

    @abstractmethod
    def destroy(self):
        pass

class IShower(ABC):

    @abstractmethod
    def show(self):
        pass
    
class IAdder(ABC):

    @abstractmethod
    def add(self, other):
        pass

class IChecker(ABC):

    @abstractmethod
    def check(self):
        pass