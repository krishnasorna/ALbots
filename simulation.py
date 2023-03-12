import pybullet as p
import constants as c
import pybullet_data
from world import WORLD
from robot import ROBOT
import time


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if (self.directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.zero, c.zero, c.gravity)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(c.thousand):
            p.stepSimulation()
            if (self.directOrGUI == "GUI"):
                time.sleep(1/500)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    
    def Get_Evolution(self):
        for i in range(c.populationSize):
            if self.robot.Get_Fitness()>c.numberOfGenerations*i:
                return 0
            else:
                return self.robot.Get_Fitness()
