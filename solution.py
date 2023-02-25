import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = (numpy.random.rand(3, 3)*2) - 1
        self.weights = self.weights * 2 - 1
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
        pyrosim.Send_Cube(
            name="Torso", pos=[-2, 0, 0.3], size=[0.5, 0.5, 0.5])

        pyrosim.End()
        self.Create_Body()
        self.Create_Brain()

    def Determine_sensor(self):
        num = random.randint(0, 1)
        if num == 0:
            return ['    <color rgba="0.0 0.0 1.0 1.0"/>', 'Blue']
        else:
            return ['    <color rgba="0.0 1.0 0.0 1.0"/>', 'Green']

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")
        colormain = self.Determine_sensor()
        pyrosim.Send_Cube(name="Main", pos=[1.5, 0, 1.5], size=[
                          1, 1, 1], nameC=colormain[1], colorful=colormain[0])

        color1 = self.Determine_sensor()
        pyrosim.Send_Joint(
            name="Main_Limb1", parent="Main", child="Limb1", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(
            name="Limb1", pos=[0.5, 0, -0.5], size=[1, 0.5, 1], nameC=color1[1], colorful=color1[0])

        color2 = self.Determine_sensor()
        pyrosim.Send_Joint(
            name="Main_Limb2", parent="Main", child="Limb2", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(
            name="Limb2", pos=[-0.5, 0, -0.5], size=[1, 0.5, 1], nameC=color2[1], colorful=color2[0])

        pyrosim.Send_Joint(
            name="Main_Arm1", parent="Main", child="Arm1", type="revolute", position=[1.5, 0.5, 1.5])
        pyrosim.Send_Cube(
            name="Arm1", pos=[0, 0.5, 0], size=[0.5, 1, 0.1], nameC=color1[1], colorful=color1[0])

        pyrosim.Send_Joint(
            name="Main_Arm2", parent="Main", child="Arm2", type="revolute", position=[1.5, -0.5, 1.5])
        pyrosim.Send_Cube(
            name="Arm2", pos=[0, -0.5, 0], size=[0.5, 1, 0.1], nameC=color2[1], colorful=color2[0])

        pyrosim.Send_Joint(
            name="Arm1_Up1", parent="Arm1", child="Up1", type="revolute", position=[0, 1, 0])
        pyrosim.Send_Cube(
            name="Up1", pos=[0, 0, 0.5], size=[0.5, 0.1, 1.5], nameC=color2[1], colorful=color2[0])

        pyrosim.Send_Joint(
            name="Arm1_Up2", parent="Arm1", child="Up2", type="revolute", position=[0, -2, 0])
        pyrosim.Send_Cube(
            name="Up2", pos=[0, 0, 0.5], size=[0.5, 0.1, 1.5], nameC=color2[1], colorful=color2[0])

        pyrosim.Send_Joint(
            name="Main_TopHat", parent="Main", child="TopHat", type="revolute", position=[1.5, 0, 2])
        pyrosim.Send_Cube(
            name="TopHat", pos=[0, 0, 0.5], size=[0.1, 0.1, 1], nameC=color1[1], colorful=color1[0])

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Main")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Limb1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Limb2")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="Limb3")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="Limb4")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Main_Limb1")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Main_Limb2")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Main_TopHat")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="Main_Limb3")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Main_Limb4")

        for currentRow in range(3):
            for currentColumn in range(3):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn +
                                     3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, len(self.weights)-1)
        column = random.randint(0, len(self.weights[0])-1)
        self.weights[row, column] = (random.random() * 2) - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
