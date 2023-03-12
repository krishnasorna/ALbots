import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import pybullet_data
import pybullet as p
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = (numpy.random.rand(7, 6)*2) - 1
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        self.coloringbook = {}
        self.coloring_book_reverse = {}

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
        pyrosim.Send_Cube(name="Torso", pos=[6, 0, 0.3], size=[0.5, 0.5, 0.5])
        pyrosim.End()
        self.Create_Body()
        self.Create_Brain()

    def Random_size(self):
        return [random.uniform(0.3, 1), random.uniform(0.3, 1), random.uniform(0.3, 1)]

    def Determine_sensor(self):
        num = random.randint(0, 1)
        if num == 0:
            return ['    <color rgba="0.0 0.0 1.0 1.0"/>', 'Blue']
        else:
            return ['    <color rgba="0.0 1.0 0.0 1.0"/>', 'Green']
        
    def Evolve_Number_Links(self):
        for i in range(c.numberOfGenerations):
            num_links = i*c.populationSize
            if num_links > 100:
                num_links = num_links%c.populationSize
        return num_links

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        colormain = self.Determine_sensor()
        color1 = self.Determine_sensor()
        torso_dims = [random.uniform(0.5, 1.5), random.uniform(
            1.5, 2.5), random.uniform(0.25, 1.5)]
        torso_posn = [0, 0, 3]
        pyrosim.Send_Cube(
            name="Main", pos=torso_posn, size=torso_dims, nameC=colormain[1], colorful=colormain[0])

        leg1_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb1", parent="Main", child="Limb1", type="revolute", position=[torso_dims[0]/2, torso_dims[1]/3, 3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb1", pos=[leg1_dims[0]/2, 0, -leg1_dims[2]/2], size=leg1_dims, nameC=color1[1], colorful=color1[0])

        color2 = self.Determine_sensor()
        leg2_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb2", parent="Main", child="Limb2", type="revolute", position=[torso_dims[0]/2, -torso_dims[1]/3, 3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb2", pos=[leg2_dims[0]/2, 0, -leg2_dims[2]/2], size=leg2_dims, nameC=color2[1], colorful=color2[0])

        color3 = self.Determine_sensor()
        leg3_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb3", parent="Main", child="Limb3", type="revolute", position=[-torso_dims[0]/2, torso_dims[1]/3, 3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb3", pos=[-leg3_dims[0]/2, 0, -leg3_dims[2]/2], size=leg3_dims, nameC=color3[1], colorful=color3[0])

        color4 = self.Determine_sensor()
        leg4_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb4", parent="Main", child="Limb4", type="revolute", position=[-torso_dims[0]/2, -torso_dims[1]/3, 3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb4", pos=[-leg4_dims[0]/2, 0, -leg4_dims[2]/2], size=leg4_dims, nameC=color4[1], colorful=color4[0])

        color5 = self.Determine_sensor()
        leg5_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb5", parent="Main", child="Limb5", type="revolute", position=[-torso_dims[0]/2, 0, 3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb5", pos=[-leg5_dims[0]/2, 0, leg5_dims[2]/2], size=leg5_dims, nameC=color5[1], colorful=color5[0])

        color6 = self.Determine_sensor()
        leg6_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb6", parent="Main", child="Limb6", type="revolute", position=[torso_dims[0]/2, 0, 3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb6", pos=[leg6_dims[0]/2, 0, leg6_dims[2]/2], size=leg6_dims, nameC=color6[1], colorful=color6[0])

        color7 = self.Determine_sensor()
        leg7_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb7", parent="Main", child="Limb7", type="revolute", position=[0, 0, 3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb7", pos=[0, 0, leg7_dims[2]/2], size=leg7_dims, nameC=color7[1], colorful=color7[0])

        color8 = self.Determine_sensor()
        leg8_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb8", parent="Main", child="Limb8", type="revolute", position=[0, -torso_dims[1]/2, 3])
        pyrosim.Send_Cube(
            name="Limb8", pos=[0, -leg8_dims[1]/2, 0], size=leg8_dims,  nameC=color8[1], colorful=color8[0])

        color9 = self.Determine_sensor()
        leg9_dims = self.Random_size()
        pyrosim.Send_Joint(
            name="Main_Limb9", parent="Main", child="Limb9", type="revolute", position=[0, torso_dims[1]/2, 3])
        pyrosim.Send_Cube(
            name="Limb9", pos=[0, leg8_dims[1]/2, 0], size=leg9_dims, nameC=color9[1], colorful=color9[0])

        self.coloring_book = {"Main": colormain[1], "Limb1": color1[1], "Limb2": color2[1], "Limb3": color3[1],
                              "Limb4": color4[1], "Limb5": color5[1], "Limb6": color6[1], "Limb7": color7[1], "Limb8": color8[1], "Limb9": color9[1]}
        self.coloring_book_reverse = {colormain[1]: "Main", color1[1]: "Limb1", color2[1]: "Limb2", color3[1]: "Limb3",
                                      color4[1]: "Limb4", color5[1]: "Limb5", color6[1]: "Limb6", color7[1]: "Limb7", color8[1]: "Limb8", color9[1]: "Limb9"}
        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        green = 0
        blue = 0
        for key, value in self.coloring_book.items():
            if value == 'Green':
                green += 1
            else:
                blue += 1

        greenJoints = [None]*green
        blueJoints = [None]*blue
        index1 = 0
        index2 = 0
        for key, value in self.coloring_book_reverse.items():
            if key == 'Green':
                greenJoints[index1] = value
                index1 += 1
            else:
                blueJoints[index2] = value
                index2 += 1

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Main")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Limb1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Limb2")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Limb3")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="Limb4")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="Limb5")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="Limb6")

        pyrosim.Send_Motor_Neuron(name=8, jointName="Main_Limb1")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Main_Limb2")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Main_Limb3")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Main_Limb4")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Main_Limb5")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Main_Limb6")

        for currentRow in range(7):
            for currentColumn in range(6):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn +
                                     7, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, len(self.weights)-1)
        column = random.randint(0, len(self.weights[0])-1)
        self.weights[row, column] = (random.random() * 2) - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
