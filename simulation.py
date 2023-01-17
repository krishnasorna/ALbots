import pybullet as p
import constants as c
import pybullet_data
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero, c.zero, c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.thousand):
            p.stepSimulation()
            time.sleep(1/1000)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def __del__(self):
        p.disconnect()
    