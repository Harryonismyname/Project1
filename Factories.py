from Assembly import *


#=================================================================================#
#===================================================================Assemblies====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Assemblies take basic objects and assing them values to be used in-----------#
#----Factories--------------------------------------------------------------------#
#---------------------------------------------------------------------------------#
class FingerAssembly:

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

class ToeAssembly:

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

class LimbSegementAssembly:

    def lowerArm(self, side="Left"):
        return ArmSegment(name="{} Lower Arm".format(side), health=10)

    def upperArm(self, side="Left"):
        return ArmSegment(name="{} Upper Arm".format(side), health=15)

    def lowerLeg(self, side="Left"):
        return LegSegment(name="{} Lower Leg".format(side), health=10)

    def upperLeg(self, side="Left"):
        return LegSegment(name="{} Upper Leg".format(side), health=15)

#=================================================================================#
#====================================================================Factories====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Factories take rescources from Assemblies and put them together to make------#
#----Larger objects---------------------------------------------------------------#
#---------------------------------------------------------------------------------#

class AppendageFactory:

    def __init__(self):
        self.fa = FingerAssembly()
        self.ta = ToeAssembly()
        
    def fiveFingerHand(self, side="Left"):
        fingerList = []
        f1 = self.fa.thumb(name=side)
        f2 = self.fa.indexFinger(name=side)
        f3 = self.fa.middleFinger(name=side)
        f4 = self.fa.ringFinger(name=side)
        f5 = self.fa.littleFinger(name=side)

        fingerList.append(f1)
        fingerList.append(f2)
        fingerList.append(f3)
        fingerList.append(f4)
        fingerList.append(f5)
        return Hand(name="{} Hand".format(side), health=5, fingers=fingerList)
    
    def fiveToedFoot(self, side="Left"):
        toeList =[]
        t1 = self.ta.bigToe(side=side)
        t2 = self.ta.secondToe(side=side)
        t3 = self.ta.thirdToe(side=side)
        t4 = self.ta.fourthToe(side=side)
        t5 = self.ta.littleToe(side=side)

        toeList.append(t1)
        toeList.append(t2)
        toeList.append(t3)
        toeList.append(t4)
        toeList.append(t5)
        return Foot(name="{} Foot".format(side), health=5, toes=toeList)

class LimbFactory:

    def __init__(self):
        self.lsa = LimbSegementAssembly()
        self.af = AppendageFactory()

    def twoPartArm(self, side="Left"):
        shoulder = Shoulder("{} Shoulder".format(side))
        upperArm = self.lsa.upperArm(side=side)
        lowerArm = self.lsa.lowerArm(side=side)
        hand = self.af.fiveFingerHand(side=side)
        return Arm(shoulder, hand, upperArm, lowerArm)
    
    def twoPartLeg(self, side="Left"):
        hip = Hip("{} Hip".format(side))
        upperLeg = self.lsa.upperLeg(side=side)
        lowerLeg = self.lsa.lowerLeg(side=side)
        foot = self.af.fiveToedFoot()
        return Leg(hip, foot, upperLeg, lowerLeg)



