Assignment 8 CS396

Special Thanks:
This Github is for CS396 course at Northwestern University. Random 3D creatures that wiggle and move in a simulation. Code was created by following Ludobots, an online course found at https://www.reddit.com/r/ludobots/. Ludobots makes use of the PyroSim modeling interface; the repository can be found at https://github.com/jbongard/pyrosim.git.

Instructions:
To run the program, click run "search.py" to see the randomly evolved 3Dcreatures in action.

Youtube Link:
---------------------------------------------------------------------------------------------------------------------------------
------------------------------------------- INSERT YT LINK ----------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

Diagram:
![Diagram](https://user-images.githubusercontent.com/91999196/221746891-dc8d0646-2ace-42b9-8963-2e6e1b71d8ac.jpg)

Fitness Curves:
<img width="489" alt="Ludobots Fitness" src="https://user-images.githubusercontent.com/91999196/221749065-6553e671-09a1-4e0b-acbe-784180ab813b.png">

Explanations:
To create a random evolved 3D creature, the code starts by making a main cube that serves as the torse which is started at (1.5, 0, 1.5), with the 1.5 units in the z-axis to serve as a base point as the creature can evolve longer legs. The torso is a random size with random dimensions so that it is not small or large enough for the creature to evolve.

As the torso is created, the code randomly evolved a number of many limb cubes which yield the best fitness. This is decided based on a pre determined fitness function, and this creature will best adapt as many legs or limbs as it should. The number of cubes are decided and the code creates joints at random locations along torso within a range of values. The links are also positioned in a smooth connection points to not disrupt the motion of the creature and evolution. Sensor placement is found by a best probability to make the creature move and earn a good fitness value. If the sensors are green then it has a motor to allow the creature to walk, otherwise it is a sensor to seek the best fitness.

The mutations involved for this creature is pre determined and specific based on the fitness fucntions. The goal of the robot is to use locomotion to go near the grey cube in the world. The random creature first starts off by jittering around and has a low fitness value, but over the 100 generations of mutations of both the brain and the body. This duality of changes is random but also very powerfully chosen as whichever brain and body reaches the cube "survives". Thus the random evolution is selectionary and is going to always prefer the fitness value that is high. As seen in the diagram of the fitness curves, over time the value of the y axis, fitness, goes significantly high.

The reason we used different seeds is to place various populations and differing advantages. This allows us to see how quickly these robots evolve based on the different starting positions. Over 100 generations, these robots evolve to find the fitness that best suits the population and survives over the other children and parent robots.
