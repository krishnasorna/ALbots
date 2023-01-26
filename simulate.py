import sys 
directOrGUI = sys.argv[1]

from simulation import SIMULATION
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
