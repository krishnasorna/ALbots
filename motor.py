import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeF

        if self.jointName == "Torso_FrontLeg":
            self.frequency = c.frequencyF
        else:
            self.frequency = c.frequencyB
        self.offset = c.phaseOffsetF

        self.xAnglesF = numpy.linspace(
            self.offset, 2*self.frequency * numpy.pi + self.offset, c.thousand)
        self.motorValues = self.amplitude * numpy.sin(self.xAnglesF)

    def Set_Value(self, robotId, time):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
        targetPosition=self.motorValues[time], maxForce=60)

    def Save_Values(self):
        numpy.save('data/motorValues.npy', self.motorValues)
