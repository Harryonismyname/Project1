from Assembly import *
from Factories import *
#=================================================================================#
#================================================================Body Wrappers====#
#=================================================================================#
#---------------------------------------------------------------------------------#
#----Body Wrappers are Limb and Appendage presets for the modular construction----#
#----of Entities------------------------------------------------------------------#
#---------------------------------------------------------------------------------#

me = LimbFactory()
myLeftLeg = me.twoPartLeg(side="Left")
myRightLeg = me.twoPartLeg(side="Right")
myLeftArm = me.twoPartArm(side="Left")
myRightArm = me.twoPartArm(side="Right")

myBody = [myLeftArm, myRightArm, myLeftLeg, myRightLeg]
for parts in myBody:
    if type(parts)==Leg:
        parts.showSegments()
    if type(parts)==Arm:
        parts.showSegments()