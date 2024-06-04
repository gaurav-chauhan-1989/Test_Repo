
from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class geometry(shape):
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre

    def printarea(self):
        return 0

class geo(geometry):
    def printarea(self):
        return self.len*self.bre

obj=geo(5,4)
print(obj.printarea())
