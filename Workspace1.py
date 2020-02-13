
class BodyPart:

    def __init__(self, name="Part", health=1):
        self.name = name
        self.health = health
        self.connectedParts = []
        self.totalHealth = self.health

    def checkHealth(self):
        for part in self.connectedParts:
            self.totalHealth += part.health
        if self.health == 0:
            self.destroy()
        else:
            pass
    
    def showHealth(self):
        print(self.name + " " + str(self.health))
        for part in self.connectedParts:
            print(part.name + " " + str(part.health))

    def destroy(self):
        self.health = 0.0
        self.connectedParts.clear

    def addPart(self, part):
        self.connectedParts.append(part)

















class Finger(BodyPart):

    def __init__(self, name="Finger", grip=0, health=1):
        super().__init__(name, health)
        self.grip = grip

class Hand(BodyPart):

    def __init__(self, name="Hand", health=5):
        self.totalGrip = 1
        super().__init__(name=name, health=health)

    def checkGrip(self):
        for fingers in self.connectedParts:
            self.totalGrip += fingers.grip
        return self.totalGrip

class ArmSegment(BodyPart):

    def __init__(self, name="Arm Segment", health=10):
        super().__init__(name, health)

class Human:

    def __init__(self):
        self.leftArm
        self.arms
        self.legs
        self.torso
        self.head