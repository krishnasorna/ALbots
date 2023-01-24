import numpy
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:

    def __init__(self):
        self.weights = (numpy.random.rand(3, 2)*2) - 1

    def Evaluate(self):
        self.Create_World()
        os.system("python3 simulate.py")
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World(self):
        self.Create_Body()
        self.Create_Brain()

    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-1.5, 1, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
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
        self.weights[random.randint(-1, 1)]
