
class BodyPart:

    def __init__(self, name="Part", health=1):
        self.name = name
        self.health = health
        self.maxHealth = self.health

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        print(f"{self.name} took {damage} damage!")

    def heal(self, amount=self.maxHealth):
        self.health += amount
        if self.health >= self.maxHealth:
            self.health = self.maxHealth

    def showHealth(self):
        print(f"{self.name} : {self.health}")

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

class Neck(BodyPart):

    def __init__(self, name='Neck', health=10):
        super().__init__(name=name, health=health)

class Head(BodyPart):

    def __init__(self, name="Head", health=20):
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
        print("")               
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