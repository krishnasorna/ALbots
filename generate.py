import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
#pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])
#pyrosim.Send_Cube(name="Box2", pos=[1, 0, 1.5], size=[1, 1, 1])

size1 = 1/0.9
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5+i], size=[size1*0.9, size1*0.9, size1*0.9])
    size1 = size1*0.9

pyrosim.End()

