from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    def Evolve(self):
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        self.Evaluate(self.parents)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        # self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in (self.parents.keys()):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for i in (self.children.keys()):
            self.children[i].Mutate()

    def Select(self):
        if(self.parent.fitness < self.child.fitness):
            self.parent = self.child

    def Print(self):
        for i in (self.parents.keys()):
            print("" + str(self.parents[i].fitness) + ", " + str(self.children[i].fitness))


    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
            print(solutions[i].fitness)