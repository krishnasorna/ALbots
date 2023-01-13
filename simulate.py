import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import time
import pybullet_data

amplitudeF = numpy.pi/4
amplitudeB = numpy.pi/4
frequencyF = 5
phaseOffsetF = 0
frequencyB = 5.6
phaseOffsetB = numpy.pi/4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

xAnglesF = numpy.linspace(phaseOffsetF, 2*frequencyF *
                          numpy.pi + phaseOffsetF, 1000)
targetAnglesF = amplitudeF * numpy.sin(xAnglesF)

xAnglesB = numpy.linspace(phaseOffsetB, 2*frequencyB *
                          numpy.pi + phaseOffsetB, 1000)
targetAnglesB = amplitudeB * numpy.sin(xAnglesB)

numpy.save('data/targetAnglesValuesFront.npy', targetAnglesF)
numpy.save('data/targetAnglesValuesBack.npy', targetAnglesB)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    min = -math.pi/2
    max = math.pi/2
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesB[i],
        maxForce=60)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesF[i],
        maxForce=60)

    time.sleep(1/10000)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
