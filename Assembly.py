
class BodyPart:

    def __init__(self, name="Part", health=1):
        self.name = name
        self.health = health

    def showHealth(self):
        print(self.name + " " + str(self.health))

    def destroy(self):
        self.health = 0.0


#=================================================================================#
#=======================================================Appendage Parent Class====#
#=================================================================================#
class Appendage(BodyPart):                                                        
#---------------------------------------------------------------------------------#
    def __init__(self, name="Appendage", health=5, extremeties=[]):
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
class Limb:                                                                       
#---------------------------------------------------------------------------------#
    def checkSegment(self, master, slave):
        if master.health==0:              
            slave.destroy()           
#---------------------------------------------------------------------------------#
    def showSegment(self, segment):
        segment.showHealth()        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Limb Sub-Classes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
class Arm(Limb):                                                                  
#---------------------------------------------------------------------------------#    
    def __init__(self, shoulder, hand):
        self.shoulder = shoulder                     
        self.hand = hand                             
#=================================================================================#
class Leg(Limb):                                                                  
#---------------------------------------------------------------------------------#
    def __init__(self, hip, foot):
        self.hip = hip                     
        self.foot = foot                   
#=================================================================================#
#===================================================================Body Parts====#
#=================================================================================#
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
#====Body Wrappers=======================================================#
class TwoSegmentArm(Arm):

    def __init__(self, shoulder, upperArm, lowerArm, hand):
        super().__init__(shoulder=shoulder, hand=hand)
        self.upperArm = upperArm
        self.lowerArm = lowerArm
    
    def showArm(self):
        self.showSegment(self.shoulder)
        self.showSegment(self.upperArm)
        self.showSegment(self.lowerArm)
        self.hand.showAppendage()

    def checkArm(self):
        self.checkSegment(self.shoulder, self.upperArm)
        self.checkSegment(self.upperArm, self.lowerArm)
        self.checkSegment(self.lowerArm, self.hand)
        self.hand.checkDigits()

class TwoSegmentLeg(Leg):

    def __init__(self, hip, foot, upperLeg, lowerLeg):
        super().__init__(hip=hip, foot=foot)
        self.upperLeg=upperLeg
        self.lowerLeg=lowerLeg

    def showLeg(self):
        self.showSegment(self.hip)
        self.showSegment(self.upperLeg)
        self.showSegment(self.lowerLeg)
        self.foot.showAppendage()

    def checkLeg(self):
        self.checkSegment(self.hip, self.upperLeg)
        self.checkSegment(self.upperLeg, self.lowerLeg)
        self.checkSegment(self.lowerLeg, self.foot)
        self.foot.checkToes()
