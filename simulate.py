# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import numpy
# import math
# import random
# import time
# import constants as c
# import pybullet_data

# amplitudeF = c.amplitudeF
# amplitudeB = c.amplitudeB
# frequencyF = c.frequencyF
# phaseOffsetF = c.phaseOffsetF
# frequencyB = c.frequencyB
# phaseOffsetB = c.phaseOffsetB

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(c.zero, c.zero, c.gravity)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.thousand )
# frontLegSensorValues = numpy.zeros(c.thousand )

# xAnglesF = numpy.linspace(phaseOffsetF, 2*frequencyF *
#                           numpy.pi + phaseOffsetF, c.thousand )
# targetAnglesF = amplitudeF * numpy.sin(xAnglesF)

# xAnglesB = numpy.linspace(phaseOffsetB, 2*frequencyB *
#                           numpy.pi + phaseOffsetB, c.thousand )
# targetAnglesB = amplitudeB * numpy.sin(xAnglesB)

# numpy.save('data/targetAnglesValuesFront.npy', targetAnglesF)
# numpy.save('data/targetAnglesValuesBack.npy', targetAnglesB)

# for i in range(c.thousand):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
#         "FrontLeg")

#     min = -math.pi/2
#     max = math.pi/2
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName="Torso_BackLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesB[i],
#         maxForce=60)

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName="Torso_FrontLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=targetAnglesF[i],
#         maxForce=60)

#     time.sleep(1/10000)

# numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
# p.disconnect()

from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()