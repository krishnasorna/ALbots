import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = (numpy.random.rand(3, 2)*2) - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI +
                  " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.4)
        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness"+str(self.myID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Test", pos=[1, 0, 0], size=[1, 1, 1], colorful = '    <color rgba="0 0 0 1.0"/>')
        
        pyrosim.End()
        self.Create_Body()
        self.Create_Brain()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0], size=[1, .1, .1], nameC = "Green",colorful = '    <color rgba="0 255 0 1.0"/>')
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute", position=[-0.5, 0, 0])
        pyrosim.Send_Cube(name="BackLeg", pos=[0.3, 0, 0], size=[.4, .7, .1], nameC = "Blue", colorful = '    <color rgba="0 0 255 1.0"/>')
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                            child="FrontLeg", type="revolute", position=[0.5, 0, 0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.3, 0, 0], size=[0.3, 0.3, 0.7], nameC = "Green", colorful = '    <color rgba="0 255 0 1.0"/>')
        # pyrosim.Send_Joint(name="FrontLeg_Leg1", parent="FrontLeg",
        #                    child="Leg1", type="revolute", position=[1, 0, 0])
        # pyrosim.Send_Cube(name="Leg1", pos=[0.8, 0, 0], size=[0.3, 0.2, .5], nameC = "Blue", colorful = '    <color rgba="0 0 255 1.0"/>')

        # pyrosim.Send_Joint(name="Leg1_Leg2", parent="Leg1",
        #                    child="Leg2", type="revolute", position=[-1, 0, 0])
        # pyrosim.Send_Cube(name="Leg2", pos=[1, 0, 0], size=[0.4, 0.1, .8], nameC = "Green", colorful = '    <color rgba="0 255 0 1.0"/>')

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn +
                                     3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, len(self.weights)-1)
        column = random.randint(0, len(self.weights[0])-1)
        self.weights[row, column] = (random.random() * 2) - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
