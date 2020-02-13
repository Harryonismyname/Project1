from Workspace1 import (BodyPart, Finger, Hand, ArmSegment, Arm)

class FingerFactory:

    def indexFinger(self):
        return Finger(name="Index Finger", grip=4, health=4)
        
    def middleFinger(self):
        return Finger(name="Middle Finger", grip=3, health=3)

    def ringFinger(self):
        return Finger(name="Ring Finger", grip=2, health=2)

    def littleFinger(self):
        return Finger(name="Little Finger", grip=4, health=4)

    def thumb(self):
        return Finger(name="Thumb", grip=5, health=5)

class HandFactory:

    def fiveFingerHand(self, name="Hand"):
        ff = FingerFactory()
        ffh = Hand(name=name)
        ffh.addPart(ff.thumb())
        ffh.addPart(ff.indexFinger())
        ffh.addPart(ff.middleFinger())
        ffh.addPart(ff.ringFinger())
        ffh.addPart(ff.littleFinger())
        ffh.checkGrip()
        return ffh

class ArmSegementAssembly:

    def lowerArm(self):
        return ArmSegment(name="Lower Arm", health=10)

    def upperArm(self):
        return ArmSegment(name="Upper Arm", health=15)


class ArmFactory:

    def twoPartArm(self):
        asa = ArmSegementAssembly()
        hf = HandFactory()
        
        upperArm = asa.upperArm()
        lowerArm = asa.lowerArm()
        hand = hf.fiveFingerHand()
        upperArm.addPart(lowerArm)
        lowerArm.addPart(hand)
        
        
        return upperArm, lowerArm, hand

me = ArmFactory()
myArm = me.twoPartArm()
for parts in myArm:
    print(parts.name)