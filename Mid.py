
class BodyPart:

    __health = 0
    __name = ""
    __maxHealth = 0

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

    def heal(self, amount=self.maxHealth):
        self.health += amount
        if self.health >= self.maxHealth:
            self.health = self.maxHealth


    def destroy(self):
        self.__health = 0

    def show(self):
        print(f"Name: {self.__name}:\nHealth: {self.__health}/{self.__maxHealth}")

#=================================================================================#
#===================================================================Body Parts====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Individual Body Parts with unique values used in the modular construction----#
#----of Limbs and Appendages------------------------------------------------------#
#---------------------------------------------------------------------------------#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Arms::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Shoulder(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Shoulder")
        self.setHealth(15)
        self.setMaxHealth(15)
#=================================================================================#
class ArmSegment(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Arm Segment")
        self.setHealth(10)
        self.setMaxHealth(10)
#=================================================================================#
class Finger(BodyPart):
    __grip = 0
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Finger")
        self.setHealth(1)
        self.setMaxHealth(1)
        
    def setGrip(self, value):
        __grip = value
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Hip(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Hip")
        self.setHealth(15)
        self.setMaxHealth(15)
#=================================================================================#
class LegSegment(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Leg Segment")
        self.setHealth(10)
        self.setMaxHealth(10)
#=================================================================================#
class Toe(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.setName("Toe")
        self.setHealth(1)
        self.setMaxHealth(1)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Body Segments::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Torso(BodyPart):
    
    def __init__(self):
        self.setName("Torso")
        self.setHealth(50)
        self.setMaxHealth(50)

class Neck(BodyPart):

    def __init__(self):
        self.setName("Neck")
        self.setHealth(10)
        self.setMaxHealth(10)

class Head(BodyPart):

    def __init__(self):
        self.setName("Head")
        self.setHealth(20)
        self.setMaxHealth(20)
#=================================================================================#
#=======================================================Appendage Parent Class====#
#=================================================================================#
class Appendage(BodyPart):                                                        
#---------------------------------------------------------------------------------#
    __extremeties=[]                              
    def __init__(self):
        """
        Appendages are Body Parts that contain a list of attached Body Parts
        and allow the assesment of the dependant Extremeties
        """
        self.setName("Appendage")
        self.setHealth(5)
        self.setMaxHealth(5)
#---------------------------------------------------------------------------------#
    def checkDigits(self):                 
        if self.health==0:                 
            for digits in self.extremeties:
                digits.destroy()         
#---------------------------------------------------------------------------------#
    def showAppendage(self):  
        print("")               
        self.show()
        for digits in self.extremeties:
            digits.show()      
#---------------------------------------------------------------------------------#
    def addExtremeties(self, other):
        self.extremeties.append(other)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::Appendage Sub-Classes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Hand(Appendage):                                                            
#---------------------------------------------------------------------------------#
    def __init__(self):        
        self.setName("Hand")
        self.setHealth(5)
        self.setMaxHealth(5)
#=================================================================================#
class Foot(Appendage):                                                            #
#---------------------------------------------------------------------------------#
    def __init__(self):          
        self.setName("Foot")
        self.setHealth(5)
        self.setMaxHealth(5)
#=================================================================================#
#============================================================Limb Parent Class====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Limbs are objects that contain Body Parts and allow for the assignment-------#
#----of dependancies as well as the assesment of said dependancies----------------#
#---------------------------------------------------------------------------------#
class Limb:                           
    #---------------------------------------------------------------------------------#
    def __init__(self, name, joint, appendage, segments=()):
        """
        Limbs are objects that store Body Parts in order from joint to appendage.\n
        A Limb always has a joint and an appendage.\n
        The number of segments in a limb may vary, but they must be listed in order descending from joint to appendage.

        """
        self.name = name
        self.segments = segments
        self.joint = joint
        self.appendage = appendage
#---------------------------------------------------------------------------------#
    def checkSegment(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the limb is destroyed.
        """
        if self.joint.health==0:              
            for segment in self.segments:
                segment.destroy()        
            self.appendage.destroy()
            self.appendage.checkDigits()
        for x in range(0, len(self.segments)-1):
            if self.segments[x].health==0:
                for y in range(x, len(self.segments)-1):
                    segment[y].destroy()
                self.appendage.destroy()
                self.appendage.checkDigits()
        if self.appendage.health==0:
            self.appendage.checkDigits()
#---------------------------------------------------------------------------------#
    def showSegments(self):
        print(f"\n{self.name}:")
        self.joint.showHealth()
        for segment in self.segments:
            segment.showHealth()        
        self.appendage.showAppendage()
#---------------------------------------------------------------------------------#
    def recieveDamage(self, damage, target):
        self.joint.health -= damage 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Limb Sub-Classes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Arm(Limb):                                                                  
#---------------------------------------------------------------------------------#    
    def __init__(self, name, shoulder, hand, *segments):
        """
        A Shoulder is any Shoulder() and serves as the starting point for the arm.\n
        A Hand is any Appendage() and serves and the ending point for the arm.\n
        For multi-segmented arms, each segment must be listed in order from Shoulder to Hand.
        """
        super().__init__(name=name, joint=shoulder, appendage=hand, segments=segments)
#=================================================================================#
class Leg(Limb):                                                                  
#---------------------------------------------------------------------------------#
    def __init__(self, name, hip, foot, *segments):
        """
        A Hip is any Hip() and serves as the starting point for the Leg.\n
        A Foot is any Appendage() and serves and the ending point for the Leg.\n
        For multi-segmented Legs, each segment must be listed in order from Hip to Foot.
        """
        super().__init__(name=name, joint=hip, appendage=foot, segments=segments)


class Body:

    def __init__(self, *segments):
        """
        Based on the number of Torso segments, list the segments in order from top to bottom
        """
        self.segments = segments

    def checkSegment(self):
        """
        Checks each segment's .health value to verify it is greater than 0.\n
        If Health is less than 0, the rest of the torso is destroyed.
        """
        for x in range(0, len(self.segments)-1):
            if self.segments[x].health==0:
                for y in range(x, len(self.segments)-1):
                    self.segments[y].destroy()

    def showBody(self):
        for segments in self.segments:
            segments.showHealth()
#=================================================================================#
#=====================================================================Entities====#
#=================================================================================#
#----Entities are objects that contain Limbs, Appendages, and other Body Parts----#
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
class Entity:

    def __init__(self, name="Entity", *bodyParts):
        """
        An Entity is an object that contains limbs, appendages, and other Body Parts\n
        to represent a creature instance.\n
        Entities should be Assembled from head to foot, matching that of the humanoid physiology
        """
        self.name = name
        self.bodyParts = bodyParts

    def show(self):
        print(self.name)
        for parts in self.bodyParts:
            if issubclass(type(parts), Limb):
                parts.showSegments()
            if issubclass(type(parts), BodyPart):
                parts.showHealth()
            if type(parts)==Body:
                parts.showBody()

    def kill(self):
        for parts in self.bodyParts:
            if issubclass(type(parts), Limb):
                parts.destroy()