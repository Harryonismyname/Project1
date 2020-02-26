from abc import ABC, abstractmethod
from High import *

class BodyPart(INamer, IHealer, IDestroyer, IShower):

    def __init__(self):
        self.__health = 0
        self.__name = ""
        self.__maxHealth = 0

    def setName(self, value):
        self.__name = value

    def setHealth(self, value):
        self.__health = value
    
    def setMaxHealth(self, value):
        self.__maxHealth = value

    def getHealth(self):
        return self.__health

    def getName(self):
        return self.__name

    def getMaxHealth(self):
        return self.__maxHealth

    def heal(self, amount):
        self._BodyPart__health += amount

    def destroy(self):
        self._BodyPart__health = 0

    def show(self):
        print(f"{self._BodyPart__name}:\nHealth {self._BodyPart__health}/{self._BodyPart__maxHealth}")


#=================================================================================#
#=======================================================Appendage Parent Class====#
#=================================================================================#
class Appendage(INamer, IHealer, IShower, IAdder, IChecker, IDestroyer):                                                        
#---------------------------------------------------------------------------------#
                              
    def __init__(self):
        """
        Appendages are Body Parts that contain a list of attached Body Parts
        and allow the assesment of the dependant Extremeties
        """
        self.__extremeties=[]    
        self.__name = ""
        self.__health = 0
        self.__maxHealth = 0
#---------------------------------------------------------------------------------#
    def setName(self, value):
        self.__name = value

    def getName(self):
        return self.__name

    def setHealth(self, value):
        self.__health = value

    def getHealth(self):
        return self.__health()

    def setMaxHealth(self, value):
        self.__maxHealth = value
        
    def getMaxHealth(self):
        return self.__maxHealth

    def getTotalHealth(self):
        self.__totalHeath = 0
        for digits in self.__extremeties:
            self.__totalHealth += digits.getHealth()
        self.__totalHeath += self.__health
        return self.__totalHeath

    def destroy(self):
        self.__health = 0

    def check(self):                 
        if self.__health==0:
            for digits in self.__extremeties:
                digits.destroy()         
#---------------------------------------------------------------------------------#
    def show(self):    
        print(f"{self.__name}:\nHealth: {self.__health}/{self.__maxHealth}")
        for digits in self.__extremeties:
            digits.show()      
#---------------------------------------------------------------------------------#
    def add(self, other):
        self.__extremeties.append(other)

#=================================================================================#
#============================================================Limb Parent Class====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Limbs are objects that contain Body Parts and allow for the assignment-------#
#----of dependancies as well as the assesment of said dependancies----------------#
#---------------------------------------------------------------------------------#
class Limb(INamer, IAdder, IChecker, IHealer, IDestroyer, IShower):                           
#--__init__-----------------------------------------------------------------------#
    def __init__(self):
        """
        Limbs are objects that store Body Parts in order from joint to appendage.\n
        A Limb always has a joint and an appendage.\n
        The number of segments in a limb may vary, but they must be listed in order descending from joint to appendage.
        """
        self.__name = ""
        self.__segments = []
        self.__joint = BodyPart()
        self.__appendage = Appendage()
#--check--------------------------------------------------------------------------#
    def check(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the limb is destroyed.
        """
        if self.__joint.getHealth()==0:              
            for segment in self.__segments:
                segment.destroy()        
            self.__appendage.destroy()
            self.appendage.checkDigits()
        for x in range(0, len(self.segments)-1):
            if self.segments[x].health==0:
                for y in range(x, len(self.segments)-1):
                    segment[y].destroy()
                self.__appendage.destroy()
                self.__appendage.check()
        if self.__appendage.getHealth()==0:
            self.__appendage.check()
#--show---------------------------------------------------------------------------#
    def show(self):
        print(f"\n{self.__name}:")
        self.__joint.show()
        for segment in self.__segments:
            segment.show()        
        self.__appendage.show()
#--add----------------------------------------------------------------------------#
    def add(self, other):
        self.__segments.append(other)




class Body(IAdder, IChecker, IShower):

    def __init__(self):
        """
        Based on the number of Torso segments, list the segments in order from top to bottom
        """
        self.__segments = []

    def check(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the torso is destroyed.
        """
        for x in range(0, len(self.__segments)-1):
            if self.__segments[x].getHealth()==0:
                for y in range(x, len(self.__segments)-1):
                    self.__segments[y].destroy()

    def show(self):
        for segments in self.__segments:
            segments.showHealth()

    def add(self, other):
        self.__segments.append(other)
#=================================================================================#
#=====================================================================Entities====#
#=================================================================================#
#----Entities are objects that contain Limbs, Appendages, and other Body Parts----#
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
class Entity(INamer, IShower, IAdder):

    def __init__(self):
        """
        An Entity is an object that contains limbs, appendages, and other Body Parts\n
        to represent a creature instance.\n
        Entities should be Assembled from head to foot, matching that of the humanoid physiology
        """
        self.__name = ""
        self.__bodyParts = []

    def show(self):
        print(self.__name)
        for parts in self.__bodyParts:
            parts.show()

    def add(self, other):
        self.__bodyParts.append(other)