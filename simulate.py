import sys 
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

from simulation import SIMULATION
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
