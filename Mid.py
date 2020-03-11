from abc import ABC, abstractmethod
from High import *
displayLeft = 20
displayRigt = 20
displayWidth = displayLeft + displayRigt
displayCharacter = "_"


class BodyPart(INamer, IHealer, IDestroyer, IShower):
#------__init__-------------------------------------------------------------------#

    def __init__(self):
        self.__health = 0
        self.__name = ""
        self.__maxHealth = 0
#------INamer---------------------------------------------------------------------#

    def setName(self, value):
        self.__name = value

    def getName(self):
        return self.__name
#------IHealer--------------------------------------------------------------------#

    def setHealth(self, value):
        self.__health = value
    
    def setMaxHealth(self, value):
        self.__maxHealth = value

    def getHealth(self):
        return self.__health

    def getMaxHealth(self):
        return self.__maxHealth

    def heal(self, amount):
        self._BodyPart__health += amount
#------IDestroyer-----------------------------------------------------------------#

    def destroy(self):
        self._BodyPart__health = 0
#------IShower--------------------------------------------------------------------#

    def show(self):
        print(f"{self.getName()}".center(displayWidth, displayCharacter)
         + f"\nHealth:".ljust(displayLeft, displayCharacter) + f"{self.getHealth()}/{self.getMaxHealth()}".rjust(displayRigt, displayCharacter))
        return self.getName()

class Body(IAdder, IChecker, IShower):
#------__init__-------------------------------------------------------------------#

    def __init__(self):
        """
        Based on the number of Torso segments, list the segments in order from top to bottom
        """
        self.__segments = []
#------IChecker-------------------------------------------------------------------#

    def check(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the torso is destroyed.
        """
        for x in range(0, len(self.__segments)-1):
            if self.__segments[x].getHealth()==0:
                for y in range(x, len(self.__segments)-1):
                    self.__segments[y].destroy()
#------IShower--------------------------------------------------------------------#

    def show(self):
        bodySegments = []
        for segments in self.__segments:
            bodySegments.append(segments.show())
        return bodySegments
#------IAdder---------------------------------------------------------------------#

    def add(self, other):
        self.__segments.append(other)

class Appendage(INamer, IHealer, IShower, IAdder, IChecker, IDestroyer):                                                        
#------__init__-------------------------------------------------------------------#
                              
    def __init__(self):
        """
        Appendages are Body Parts that contain a list of attached Body Parts
        and allow the assesment of the dependant Extremeties
        """
        self.__extremeties=[]    
        self.__name = ""
        self.__health = 0
        self.__maxHealth = 0
#------INamer---------------------------------------------------------------------#
    def setName(self, value):
        self.__name = value

    def getName(self):
        return self.__name
#------IHealer--------------------------------------------------------------------#

    def setHealth(self, value):
        self.__health = value

    def getHealth(self):
        return self.__health

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
        self.check()
#------IChecker-------------------------------------------------------------------#

    def check(self):                 
        if self.getHealth()==0:
            for digits in self.__extremeties:
                digits.destroy()         
#------IShower--------------------------------------------------------------------#
    def show(self):    
        self.showBase()
        self.showDigits()


    def showBase(self):
        print(f"{self.getName()}".center(displayWidth, "=")
         + f"\nHealth:".ljust(displayLeft, displayCharacter) + f"{self.getHealth()}/{self.getMaxHealth()}".rjust(displayRigt, displayCharacter))

    def showDigits(self):
        for digits in self.__extremeties:
            digits.show()
#---------------------------------------------------------------------------------#
    def add(self, other):
        
        if type(other)==list:
            self.__extremeties.extend(other)
        else:
            self.__extremeties.append(other)

    def getDigits(self):
        return self.__extremeties


class Limb(INamer, IAdder, IChecker, IDestroyer, IShower):                           
#------__init__-------------------------------------------------------------------#
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
#------INamer---------------------------------------------------------------------#

    def setName(self, value):
        self.__name = value

    def getName(self):
        return self.__name 
#------IAdder---------------------------------------------------------------------#
    def add(self, other):
        if type(other)==list:
            self.__segments.extend(other)
        else:
            self.__segments.append(other)

    def getSegments(self):
        return self.__segments
#------IChecker-------------------------------------------------------------------#
    def check(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the limb is destroyed.
        """
        if self.__joint.getHealth()==0:              
            for segment in self.__segments:
                segment.destroy()        
            self.__appendage.destroy()
        for x in range(0, len(self.segments)-1):
            if self.segments[x].health==0:
                for y in range(x, len(self.segments)-1):
                    segment[y].destroy()
                self.__appendage.destroy()
        if self.__appendage.getHealth()==0:
            self.__appendage.check()
#------IShower--------------------------------------------------------------------#
    def show(self):
        print(f"\n{self.getName()}:\n")
        self.showJoint()
        self.showSegments()
        self.showAppendage()

    def showBasic(self):
        print(f"\n{self.getName()}:\n")
        self.showJoint()
        self.showSegments()
        self.showBaseAppendage()

    def showJoint(self):
        self.__joint.show()

    def showSegments(self):
        for segment in self.__segments:
            segment.show()

    def showAppendage(self):
        self.__appendage.show()

    def showBaseAppendage(self):
        self.__appendage.showBase()

    def showDigits(self):
        self.__appendage.showDigits()
#------Appendage------------------------------------------------------------------#

    def setAppendage(self, appendage):
        self.__appendage = appendage

    def getAppendage(self):
        return self.__appendage

    def setDigits(self, digit):
        self.__appendage.add(digit)
    
    def getDigits(self):
        return self.__appendage.getDigits()
#------Joint----------------------------------------------------------------------#

    def setJoint(self, joint):
        self.__joint = joint

    def getJoint(self):
        return self.__joint

    def destroy(self):
        self.__joint.destroy()
        self.check()

class TwoSegmentLimb(Limb):
#------__init__-------------------------------------------------------------------#
    
    def __init__(self):
        self.__upperLimb = BodyPart()
        self.__lowerLimb = BodyPart()
        super().__init__()
#------Upper Limb-----------------------------------------------------------------#

    def setUpperLimb(self, uLimb):
        self.__upperLimb = uLimb

    def getUpperLimb(self):
        return self.__upperLimb

    def showUpperLimb(self):
        self.__upperLimb.show()
#------Lower Limb-----------------------------------------------------------------#

    def setLowerLimb(self, lLimb):
        self.__lowerLimb = lLimb

    def getLowerLimb(self):
        return self.__upperLimb
    
    def showLowerLimb(self):
        self.__lowerLimb.show()

class Entity(INamer, IShower, IAdder):
#------__init__-------------------------------------------------------------------#

    def __init__(self):
        """
        An Entity is an object that contains limbs, appendages, and other Body Parts\n
        to represent a creature instance.\n
        Entities should be Assembled from head to foot, matching that of the humanoid physiology
        """
        self.__name = ""
        self.__bodyParts = []
#------INamer---------------------------------------------------------------------#

    def setName(self, value):
        self.__name = value

    def getName(self):
        return self.__name 
#------IShower--------------------------------------------------------------------#

    def show(self):
        print(self.getName())
        for parts in self.__bodyParts:
            parts.show()
#------IAdder---------------------------------------------------------------------#

    def add(self, other):
        if type(other)==list:
            self.__bodyParts.extend(other)
        else:
            self.__bodyParts.append(other)

class Humanoid(Entity):
#------__init__-------------------------------------------------------------------#

    def __init__(self):
        self.__head = BodyPart()
        self.__neck = BodyPart()
        self.__torso = Body()
        self.__leftArm = Limb()
        self.__rightArm = Limb()
        self.__leftLeg = Limb()
        self.__rightLeg = Limb()
        super().__init__()
#------Head-----------------------------------------------------------------------#

    def setHead(self, head):
        self.__head = head

    def getHead(self):
        return self.__head

    def showHead(self):
        self.__head.show()
#------Neck-----------------------------------------------------------------------#

    def setNeck(self, neck):
        self.__neck = neck

    def getNeck(self):
        return self.__neck

    def showNeck(self):
        self.__neck.show()
#------Torso----------------------------------------------------------------------#

    def setTorso(self, torso):
        self.__torso = torso

    def getTorso(self, torso):
        return self.__torso

    def showTorso(self):
        self.__torso.show()
#------Left Arm-------------------------------------------------------------------#

    #-----Getters and Setters-----#
    def setLeftArm(self, lArm):
        self.__leftArm = lArm

    def getLeftArm(self):
        return self.__leftArm

    def getLeftShoulders(self):
        return self.__leftArm.getJoint()

    def setLeftShoulder(self, lShoulder):
        self.__leftArm.setJoint(lShoulder)

    def addLeftArmSegments(self, lSegment):
        self.__leftArm.add(lSegment)

    def getLeftArmSegments(self):
        return self.__leftArm.getSegments()

    def setLeftHand(self, lHand):
        self.__leftArm.setAppendage(lHand)

    def getLeftHand(self):
        return self.__leftArm.getAppendage()

    def getLeftFingers(self):
        return self.__leftArm.getDigits()

    def setLeftFingers(self, lFingers):
        self.__leftArm.setDigits(lFingers)
    #-----Showers-----#

    def showLeftArm(self):
        self.__leftArm.show()

    def showLeftArmBasic(self):
        self.__leftArm.showBasic()

    def showLeftArmJoint(self):
        self.__leftArm.showJoint()

    def showLeftArmSegments(self):
        self.__leftArm.showSegments()

    def showLeftHand(self):
        self.__leftArm.showAppendage()

    def showLeftArmDigits(self):
        self.__leftArm.showDigits()
#------Right Arm------------------------------------------------------------------#

    def setRightArm(self, rArm):
        self.__rightArm = rArm

    def getRightArm(self):
        return self.__rightArm

    def setRightShoulder(self, rShoulder):
        self.__rightArm.setJoint(rShoulder)

    def getRightShoulder(self):
        return self.__rightArm.getJoint()

    def addRightArmSegments(self, rSegment):
        self.__rightArm.add(rSegment)

    def getRightArmSegments(self):
        return self.__rightArm.getSegments()
    
    def setRightHand(self, rHand):
        self.__rightArm.setAppendage(rHand)

    def getRightHand(self):
        return self.__rightArm.getAppendage()

    def getRightFingers(self):
        return self.__rightArm.getDigits()
    
    def setRightFingers(self, rFingers):
        self.__rightArm.setDigits(rFingers)
    #-----Showers-----#

    def showRightArm(self):
        self.__rightArm.show()

    def showRightArmBasic(self):
        self.__rightArm.showBasic()

    def showRightArmSegments(self):
        self.__rightArm.showSegments()
    
    def showRightArmDigits(self):
        self.__rightArm.showDigits()
    
    def showRightHand(self):
        self.__rightArm.showAppendage()
#------Left Leg-------------------------------------------------------------------#

    def setLeftLeg(self, lLeg):
        self.__leftLeg = lLeg

    def getLeftLeg(self):
        return self.__leftLeg

    def getLeftHip(self):
        return self.__leftLeg.getJoint()

    def setLeftHip(self, lHip):
        self.__leftLeg.setJoint(lHip)

    def addLeftLegSegments(self, lSegments):
        self.__leftLeg.add(lSegments)

    def getLeftLegSegments(self):
        return self.__leftLeg.getSegments()

    def setLeftFoot(self, lFoot):
        self.__leftLeg.setAppendage(lFoot)

    def getLeftFoot(self):
        return self.__leftLeg.getAppendage()

    def getLeftToes(self):
        return self.__leftLeg.getDigits()

    def setLeftToes(self, lToes):
        self.__leftLeg.setDigits(lToes)
    
    #-----Showers-----#

    def showLeftLeg(self):
        self.__leftLeg.show()
    def showLeftLegBasic(self):
        self.__leftLeg.showBasic()

    def showLeftLegJoint(self):
        self.__leftLeg.showJoint()

    def showLeftLegSegments(self):
        self.__leftLeg.showSegments()
    
    def showLeftFoot(self):
        self.__leftLeg.showAppendage()
    
    def showLeftToes(self):
        self.__leftLeg.showDigits()
#------Right Leg------------------------------------------------------------------#

    def setRightLeg(self, rLeg):
        self.__rightLeg = rLeg

    def getRightLeg(self):
        return self.__rightLeg

    def setRightHip(self, rHip):
        self.__rightLeg.setJoint()

    def getRightHip(self):
        return self.__rightLeg.getJoint()

    def addRightLegSegments(self, rSegments):
        self.__rightLeg.add(rSegments)
    
    def getRightLegSegments(self):
        self.__rightLeg.getSegments()

    def setRightFoot(self, rFoot):
        self.__rightLeg.setAppendage(rFoot)

    def getRightFoot(self):
        return self.__rightLeg.getAppendage()

    def getRightToes(self):
        return self.__rightLeg.getDigits()

    def setRightToes(self, rToes):
        self.__rightLeg.setDigits(rToes)
    
    #-----Showers-----#

    def showRightLeg(self):
        self.__rightLeg.show()

    def showRightLegBasic(self):
        self.__rightLeg.showBasic()

    def showRightLegJoint(self):
        self.__rightLeg.showJoint()

    def showRightLegSegment(self):
        self.__rightLeg.showSegments()
    
    def showRightFoot(self):
        self.__rightLeg.showAppendage()

    def showRightToes(self):
        self.__rightLeg.showDigits()
