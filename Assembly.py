
class BodyPart:

    def __init__(self, name="Part", health=1):
        self.name = name
        self.health = health

    def showHealth(self):
        print(self.name + " " + str(self.health))

    def destroy(self):
        self.health = 0.0

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
    def __init__(self, name='Shoulder', health=15):
        super().__init__(name=name, health=health)
#=================================================================================#
class ArmSegment(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self, name="Arm Segment", health=10):
        super().__init__(name, health)
#=================================================================================#
class Finger(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self, name="Finger", grip=0, health=1):
        super().__init__(name, health)
        self.grip = grip
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Hip(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self, name='Hip', health=15):
        super().__init__(name=name, health=health)
#=================================================================================#
class LegSegment(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self, name='Leg Segment', health=10):
        super().__init__(name=name, health=health)
#=================================================================================#
class Toe(BodyPart):
#---------------------------------------------------------------------------------#
    def __init__(self, name='Toe', health=1):
        super().__init__(name=name, health=health)    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Body Segments::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Torso(BodyPart):
    
    def __init__(self, name='Torso', health=50):
        super().__init__(name=name, health=health)
#=================================================================================#
#=======================================================Appendage Parent Class====#
#=================================================================================#
class Appendage(BodyPart):                                                        
#---------------------------------------------------------------------------------#
    def __init__(self, name="Appendage", health=5, extremeties=[]):
        """
        Appendages are Body Parts that contain a list of attached Body Parts
        and allow the assesment of the dependant Extremeties
        """
        super().__init__(name=name, health=health)                 
        self.extremeties=extremeties                               
#---------------------------------------------------------------------------------#
    def checkDigits(self):                 
        if self.health==0:                 
            for digits in self.extremeties:
                digits.destroy()         
#---------------------------------------------------------------------------------#
    def showAppendage(self):                 
        self.showHealth()
        for digits in self.extremeties:
            digits.showHealth()      
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::Appendage Sub-Classes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Hand(Appendage):                                                            
#---------------------------------------------------------------------------------#
    def __init__(self, name="Hand", health=5, fingers=[]):        
        super().__init__(name=name, health=health, extremeties=fingers) 
#=================================================================================#
class Foot(Appendage):                                                            #
#---------------------------------------------------------------------------------#
    def __init__(self, name='Foot', health=5, toes=[]):          
        super().__init__(name=name, health=health, extremeties=toes)
#=================================================================================#
#============================================================Limb Parent Class====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Limbs are objects that contain Body Parts and allow for the assignment-------#
#----of dependancies as well as the assesment of said dependancies----------------#
#---------------------------------------------------------------------------------#
class Limb:                           
    #---------------------------------------------------------------------------------#
    def __init__(self, joint, appendage, segments=()):
        """
        Limbs are objects that store Body Parts in order from joint to appendage.\n
        A Limb always has a joint and an appendage.\n
        The number of segments in a limb may vary, but they must be listed in order descending from joint to appendage.

        """
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
        self.joint.showHealth()
        for segment in self.segments:
            segment.showHealth()        
        self.appendage.showAppendage()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Limb Sub-Classes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Arm(Limb):                                                                  
#---------------------------------------------------------------------------------#    
    def __init__(self, shoulder, hand, *segments):
        """
        A Shoulder is any Shoulder() and serves as the starting point for the arm.\n
        A Hand is any Appendage() and serves and the ending point for the arm.\n
        For multi-segmented arms, each segment must be listed in order from Shoulder to Hand.
        """
        super().__init__(joint=shoulder, appendage=hand, segments=segments)
#=================================================================================#
class Leg(Limb):                                                                  
#---------------------------------------------------------------------------------#
    def __init__(self, hip, foot, *segments):
        """
        A Hip is any Hip() and serves as the starting point for the Leg.\n
        A Foot is any Appendage() and serves and the ending point for the Leg.\n
        For multi-segmented Legs, each segment must be listed in order from Hip to Foot.
        """
        super().__init__(joint=hip, appendage=foot, segments=segments)
#=================================================================================#
#=====================================================================Entities====#
#=================================================================================#
#----Entities are objects that contain Limbs, Appendages, and other Body Parts----#
#---------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
class Entity:

    def __init__(self, bodyParts=[]):
        self.bodyParts = bodyParts

    def showBody(self):
        for parts in self.bodyParts:
            if type(parts)==Appendage:
                parts.showAppendage()
            if type(parts)==Limb:
                parts.show
