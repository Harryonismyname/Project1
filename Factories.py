from Assembly import *


#=================================================================================#
#===================================================================Assemblies====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Assemblies take basic objects and assign them values to be used in-----------#
#----Factories--------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
class BodyPartAssembly:

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Fingers::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def indexFinger(self, name=""):
        return Finger(name=name + " Index Finger", grip=4, health=4)
        
    def middleFinger(self, name=""):
        return Finger(name=name + " Middle Finger", grip=3, health=3)

    def ringFinger(self, name=""):
        return Finger(name=name + " Ring Finger", grip=2, health=2)

    def littleFinger(self, name=""):
        return Finger(name=name + " Little Finger", grip=4, health=4)

    def thumb(self, name=""):
        return Finger(name=name + " Thumb", grip=5, health=5)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Toes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def bigToe(self, side="Left"):
        return Toe(name="{} Big Toe".format(side), health=5)

    def secondToe(self, side="Left"):
        return Toe(name="{} Second Toe".format(side), health=4)

    def thirdToe(self, side="Left"):
        return Toe(name="{} Third Toe".format(side), health=3)
    
    def fourthToe(self, side="Left"):
        return Toe(name="{} Fourth Toe".format(side), health=2)
    
    def littleToe(self, side="Left"):
        return Toe(name="{} Little Toe".format(side), health=1)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Arms::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def lowerArm(self, side="Left"):
        return ArmSegment(name="{} Lower Arm".format(side), health=10)

    def upperArm(self, side="Left"):
        return ArmSegment(name="{} Upper Arm".format(side), health=15)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def lowerLeg(self, side="Left"):
        return LegSegment(name="{} Lower Leg".format(side), health=10)

    def upperLeg(self, side="Left"):
        return LegSegment(name="{} Upper Leg".format(side), health=15)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Torso::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def upperBody(self):
        return Torso(name="Upper Body", health=50)

    def lowerBody(self):
        return Torso(name="Lower Body", health=50)

#=================================================================================#
#====================================================================Factories====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Factories take rescources from Assemblies and put them together to make------#
#----Larger objects---------------------------------------------------------------#
#---------------------------------------------------------------------------------#

class BodyFactory:

    def __init__(self):
        self.bpa = BodyPartAssembly()

    def twoPartTorso(self):
        upperTorso = self.bpa.upperBody()
        lowerTorso = self.bpa.lowerBody()
        Body(upperTorso, lowerTorso)

#=================================================================================#
#============================================================Appendage Factory====#
#=================================================================================#

class AppendageFactory:

    def __init__(self):
        self.bpa = BodyPartAssembly()
        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Hands::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def fiveFingerHand(self, side="Left"):
        fingerList = []
        f1 = self.bpa.thumb(name=side)
        f2 = self.bpa.indexFinger(name=side)
        f3 = self.bpa.middleFinger(name=side)
        f4 = self.bpa.ringFinger(name=side)
        f5 = self.bpa.littleFinger(name=side)

        fingerList.append(f1)
        fingerList.append(f2)
        fingerList.append(f3)
        fingerList.append(f4)
        fingerList.append(f5)
        return Hand(name="{} Hand".format(side), health=5, fingers=fingerList)
    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Feet::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def fiveToedFoot(self, side="Left"):
        toeList =[]
        t1 = self.bpa.bigToe(side=side)
        t2 = self.bpa.secondToe(side=side)
        t3 = self.bpa.thirdToe(side=side)
        t4 = self.bpa.fourthToe(side=side)
        t5 = self.bpa.littleToe(side=side)

        toeList.append(t1)
        toeList.append(t2)
        toeList.append(t3)
        toeList.append(t4)
        toeList.append(t5)
        return Foot(name="{} Foot".format(side), health=5, toes=toeList)

#=================================================================================#
#=================================================================Limb Factory====#
#=================================================================================#

class LimbFactory:

    def __init__(self):
        self.bpa = BodyPartAssembly()
        self.af = AppendageFactory()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Arms::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def twoPartArm(self, side="Left"):
        shoulder = Shoulder("{} Shoulder".format(side))
        upperArm = self.bpa.upperArm(side=side)
        lowerArm = self.bpa.lowerArm(side=side)
        hand = self.af.fiveFingerHand(side=side)
        return Arm(shoulder, hand, upperArm, lowerArm)
    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def twoPartLeg(self, side="Left"):
        hip = Hip("{} Hip".format(side))
        upperLeg = self.bpa.upperLeg(side=side)
        lowerLeg = self.bpa.lowerLeg(side=side)
        foot = self.af.fiveToedFoot()
        return Leg(hip, foot, upperLeg, lowerLeg)


#=================================================================================#
#===============================================================Entity Factory====#
#=================================================================================#

class EntityFactory:

    def __init__(self):
        self.lf = LimbFactory()
        self.bf =BodyFactory()
        self.bpa = BodyPartAssembly()

    def humanoid(self, name="Humanoid"):
        partsList = []
        head = Head(name="Head", health=20)
        neck = Neck(name="Neck", health=10)
        torso = self.bf.twoPartTorso()
        leftArm = self.lf.twoPartArm("Left")
        rightArm = self.lf.twoPartArm("Right")
        leftLeg = self.lf.twoPartLeg("Left")
        rightLeg = self.lf.twoPartLeg("Right")
        return Entity(name, head, neck, torso, leftArm, rightArm, leftLeg, rightLeg)




