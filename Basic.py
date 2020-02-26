from Mid import *


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
    
#---------------------------------------------------------------------------------#
    def __init__(self):
        self.__grip = 0
        self.setName("Finger")
        self.setHealth(1)
        self.setMaxHealth(1)
        
    def setGrip(self, value):
        self.__grip = value
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
