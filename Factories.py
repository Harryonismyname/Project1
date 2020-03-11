from Mid import *


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

    def indexFinger(self, side=""):
        indFinger = BodyPart()
        indFinger.setName(f"{side} Index Finger")
        indFinger.setMaxHealth(4)
        indFinger.setHealth(4)
        return indFinger
        
    def middleFinger(self, side=""):
        midFinger = BodyPart()
        midFinger.setName(f"{side} Middle Finger")
        midFinger.setMaxHealth(3)
        midFinger.setHealth(3)
        return midFinger

    def ringFinger(self, side=""):
       rinFinger = BodyPart()
       rinFinger.setName(f"{side} Ring Finger")
       rinFinger.setHealth(2)
       rinFinger.setMaxHealth(2)
       return rinFinger

    def littleFinger(self, side=""):
        litFinger = BodyPart()
        litFinger.setName(f"{side} Little Finger")
        litFinger.setHealth(4)
        litFinger.setMaxHealth(4)
        return litFinger

    def thumb(self, side=""):
        thum = BodyPart()
        thum.setName(f"{side} Thumb")
        thum.setHealth(5)
        thum.setMaxHealth(5)
        return thum

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Toes::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def bigToe(self, side="Left"):
        bt = BodyPart()
        bt.setName(f"{side} Big Toe")
        bt.setHealth(5)
        bt.setMaxHealth(5)
        return bt

    def secondToe(self, side="Left"):
        st = BodyPart()
        st.setName(f"{side} Second Toe")
        st.setHealth(4)
        st.setMaxHealth(4)
        return st

    def thirdToe(self, side="Left"):
        tt = BodyPart()
        tt.setName(f"{side} Third Toe")
        tt.setHealth(3)
        tt.setMaxHealth(3)
        return tt
    
    def fourthToe(self, side="Left"):
        ft = BodyPart()
        ft.setName(f"{side} Fourth Toe")
        ft.setHealth(2)
        ft.setMaxHealth(2)
        return ft
    
    def littleToe(self, side="Left"):
        lt = BodyPart()
        lt.setName(f"{side} Little Toe")
        lt.setHealth(1)
        lt.setMaxHealth(1)
        return lt

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Arms::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def shoulder(self, side="Left"):
        shldr = BodyPart()
        shldr.setName(f"{side} Shoulder")
        shldr.setHealth(15)
        shldr.setMaxHealth(15)
        return shldr

    def hip(self, side="Left"):
        hip = BodyPart()
        hip.setName(f"{side} Hip")
        hip.setHealth(15)
        hip.setMaxHealth(15)
        return hip

    def neck(self):
        neck = BodyPart()
        neck.setName("Neck")
        neck.setHealth(10)
        neck.setMaxHealth(10)
        return neck


    def head(self):
        head = BodyPart()
        head.setName("Head")
        head.setHealth(20)
        head.setMaxHealth(20)
        return head

    def lowerArm(self, side="Left"):
        la = BodyPart()
        la.setName(f"{side} Lower Arm")
        la.setHealth(10)
        la.setMaxHealth(10)
        return la

    def upperArm(self, side="Left"):
        ua = BodyPart()
        ua.setName(f"{side} Upper Arm")
        ua.setHealth(15)
        ua.setMaxHealth(15)
        return ua

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def lowerLeg(self, side="Left"):
        ll = BodyPart()
        ll.setName(f"{side} Lower Leg")
        ll.setHealth(10)
        ll.setMaxHealth(10)
        return ll

    def upperLeg(self, side="Left"):
        ul = BodyPart()
        ul.setName(f"{side} Upper Leg")
        ul.setHealth(15)
        ul.setMaxHealth(15)
        return ul

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Torso::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def upperBody(self):
        ub = BodyPart()
        ub.setName("Upper Body")
        ub.setHealth(50)
        ub.setMaxHealth(50)
        return ub

    def lowerBody(self):
        lb = BodyPart()
        lb.setName("Lower Body")
        lb.setHealth(50)
        lb.setMaxHealth(50)
        return lb

#=================================================================================#
#====================================================================Factories====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Factories take rescources from Assemblies and put them together to make------#
#----Larger objects---------------------------------------------------------------#
#---------------------------------------------------------------------------------#

class BodyFactory:
    
    bpa = BodyPartAssembly()

    def twoPartTorso(self):
        tpt = Body()
        upperTorso = self.bpa.upperBody()
        lowerTorso = self.bpa.lowerBody()
        tpt.add(upperTorso)
        tpt.add(lowerTorso)
        return tpt

#=================================================================================#
#============================================================Appendage Factory====#
#=================================================================================#

class AppendageFactory:

    bpa = BodyPartAssembly()
        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Hands::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def fiveFingerHand(self, side="Left"):
        ffh = Appendage()
        ffh.setName(f"{side} Hand")
        ffh.setHealth(5)
        ffh.setMaxHealth(5)
        ffh.add([self.bpa.thumb(side=side), self.bpa.indexFinger(side=side), 
                    self.bpa.middleFinger(side=side), self.bpa.ringFinger(side=side),
                    self.bpa.littleFinger(side=side)])
        return ffh
    

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Feet::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def fiveToedFoot(self, side="Left"):
        ftf = Appendage()
        ftf.setName(f"{side} Foot")
        ftf.setHealth(5)
        ftf.setMaxHealth(5)
        ftf.add([self.bpa.bigToe(side=side), self.bpa.secondToe(side=side),
                self.bpa.thirdToe(side=side), self.bpa.fourthToe(side=side),
                self.bpa.littleToe(side=side)])
        return ftf

#=================================================================================#
#=================================================================Limb Factory====#
#=================================================================================#

class LimbFactory:
    bpa = BodyPartAssembly()
    af = AppendageFactory()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Arms::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def twoPartArm(self, side="Left"):
        tpa = Limb()
        tpa.setName(f"{side} Arm")
        tpa.setJoint(self.bpa.shoulder(side=side))
        tpa.setAppendage(self.af.fiveFingerHand(side=side))
        tpa.add([self.bpa.upperArm(side=side), self.bpa.lowerArm(side=side)])
        return tpa
    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::Legs::::#
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

    def twoPartLeg(self, side="Left"):
        tpl = TwoSegmentLimb()
        tpl.setName(f"{side} Leg")
        tpl.setJoint(self.bpa.hip(side=side))
        tpl.setAppendage(self.af.fiveToedFoot(side=side))
        upperLeg = self.bpa.upperLeg(side=side)
        lowerLeg = self.bpa.lowerLeg(side=side)
        tpl.add([upperLeg, lowerLeg])
        tpl.setUpperLimb(upperLeg)
        tpl.setLowerLimb(lowerLeg)
        return tpl


#=================================================================================#
#===============================================================Entity Factory====#
#=================================================================================#

class EntityFactory:

    lf = LimbFactory()
    bf =BodyFactory()
    bpa = BodyPartAssembly()

    def humanoid(self, name="Humanoid"):
        entity = Humanoid()
        entity.setName(name)
        
        head = self.bpa.head()
        entity.add(head) # Adding Head
        entity.setHead(head)
        
        neck = self.bpa.neck()
        entity.add(neck) # Adding Neck
        entity.setNeck(neck)

        torso = self.bf.twoPartTorso()
        entity.add(torso) # Adding Torso
        entity.setTorso(torso)

        leftArm = self.lf.twoPartArm("Left")
        entity.add(leftArm) # Adding Left Arm
        entity.setLeftArm(leftArm)

        rightArm = self.lf.twoPartArm("Right")
        entity.add(rightArm) # Adding Right Arm
        entity.setRightArm(rightArm)

        leftLeg = self.lf.twoPartLeg("Left")
        entity.add(leftLeg) # Adding Left Leg
        entity.setLeftLeg(leftLeg)

        rightLeg = self.lf.twoPartLeg("Right")
        entity.add(rightLeg) # Adding Right Leg
        entity.setRightLeg(rightLeg)

        
        return entity
"""



"""