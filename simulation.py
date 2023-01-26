import pybullet as p
import constants as c
import pybullet_data
from world import WORLD
from robot import ROBOT
import time


class SIMULATION:

    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if (self.directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero, c.zero, c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.thousand):
            p.stepSimulation()
            if (self.directOrGUI == "GUI"):
                time.sleep(1/100000)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
