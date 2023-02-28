from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np
import matplotlib.pyplot as plt


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
        self.data = [0] * c.numberOfGenerations

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select(currentGeneration)

    def Spawn(self):
        self.children = {}
        for i in (self.parents.keys()):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for i in (self.children.keys()):
            self.children[i].Mutate()

    def Select(self, currentGeneration):
        for i in (self.parents.keys()):
            if(self.parents[i].fitness < self.children[i].fitness):
                self.parents[i] = self.children[i]

        maxF = 0
        for i in (self.parents.keys()):
            if(self.parents[i].fitness > maxF):
                maxF = self.parents[i].fitness
        
        self.data[currentGeneration] = maxF

    def Print(self):
        for i in (self.parents.keys()):
            print(str(self.parents[i].fitness) + ", " + str(self.children[i].fitness))

    def Show_Best(self):
        max = self.parents[0].fitness
        index = 0
        for i in (self.parents.keys()):
            if self.parents[i].fitness > max:
                max = self.parents[i].fitness
                index = i

        with open("file4.npy", "wb") as f:
            np.save(f,np.array(self.data))
        self.parents[index].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
