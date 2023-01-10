import pyrosim.pyrosim as pyrosim

#pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])
#pyrosim.Send_Cube(name="Box2", pos=[1, 0, 1.5], size=[1, 1, 1])
# pos2 = 0
# for j in range(5):
#     pos1 = 0
#     for k in range(5):
#         size1 = 1/0.9
#         for i in range(10):
#             pyrosim.Send_Cube(name="Box", pos=[pos1, pos2, 0.5+i], size=[size1*0.9, size1*0.9, size1*0.9])
#             size1 = size1*0.9
#         pos1 = pos1+1
#     pos2 = pos2+1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-1.5, 1, 0.5], size=[1, 1, 1])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg",
                       child="Torso", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="Torso", pos=[0.5, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                       child="FrontLeg", type="revolute", position=[1, 0, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()


Create_World()
Create_Robot()
