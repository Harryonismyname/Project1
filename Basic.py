from Factories import *









class Human:

    def __init__(self):
        self.leftArm = BodyPart(name="Left Arm", health=25)
        self.rightArm = BodyPart(name="Right Arm", health=25)
        self.leftLeg = BodyPart(name="Left Leg", health=30)
        self.rightLeg = BodyPart(name="Right Leg", health=30)
        self.torso = BodyPart(name="Torso", health=50)
        self.head = BodyPart(name="Head", health=20)
        self.totalHealth = (self.leftArm.health + self.rightArm.health + self.leftLeg.health + self.rightLeg.health + self.torso.health + self.head.health) / 6


