Final Project CS 396

Special Thanks:

This Github is for CS396 course at Northwestern University. Code was created by following Ludobots, an online course found at https://www.reddit.com/r/ludobots/. Ludobots makes use of the PyroSim modeling interface; the repository can be found at https://github.com/jbongard/pyrosim.git. Fitness is based on how close a Ludobot can reach a cube in the simulation. This project could not have been done without the help of Professor Sam Kriegman and T.A. Donna Hooshmand. Thank you both very much for introducing me to this course and helping me every step of the way! 

Instructions:

To run the program, click run "search.py" to see the randomly evolved 3Dcreatures in action. These 3D robots are evolved from a population size of 50 and have been evolved over 100 generations. This is subject to change by the user if need be simply by changing the constants of numberOfGenerations and populationSize in the constants.py file. To see the robots with the best fitness, open the file in the directory called "file*.npy", where * represents the random seed that evolution began over. There is a range of 5 random seeds which all contain very different creatures and evolutionary processes.

Teaser GIF:

![Final Gif](https://user-images.githubusercontent.com/91999196/224565699-6b78f853-2d9c-4aa6-a227-6ec339379573.gif)

Final Video:
INSERT HERE

Simulation Arena:

Here is a figure of the simulation's arena in which the Ludobot resides. This is to help visualize how the robot interacts with its surroundings.

<img width="600" alt="Screen Shot 2023-03-12 at 2 27 13 PM" src="https://user-images.githubusercontent.com/91999196/224568273-11394805-84ff-43a9-bd70-7e329eb59702.png">

Genotype-Phenotype:

<img width="624" alt="Screen Shot 2023-03-12 at 2 21 21 PM" src="https://user-images.githubusercontent.com/91999196/224567930-e948b084-78fc-4430-ab9f-1a9029515bda.png">

As seen above, different genotypes encoded different phenotypes of a robot. This is found in nature as well which is what makes Ludobots such an amazing invention. We are able to have various Ludobots based on evolution that changes not only their phenotypes but their genetic makeup. This is wild to imagine as we have the power to experiment in real time but with speeded up results.

Fitness Curves:

<img width="489" alt="Ludobots Fitness" src="https://user-images.githubusercontent.com/91999196/221749065-6553e671-09a1-4e0b-acbe-784180ab813b.png">

Parallel Hill Climbing:

<img width="844" alt="Screen Shot 2023-03-12 at 3 01 43 PM" src="https://user-images.githubusercontent.com/91999196/224570233-15d85ab3-5f16-4366-bd91-725410cbab5e.png">

Mutation Diagram:

<img width="690" alt="Screen Shot 2023-03-12 at 3 01 52 PM" src="https://user-images.githubusercontent.com/91999196/224570253-c9ec4dc9-f1be-4a07-a5c9-ec6ca9ffb976.png">

Explanation of Evolution:

To create a random evolved 3D creature, the code starts by making a main cube that serves as the torse which is started at (1.5, 0, 1.5), with the 1.5 units in the z-axis to serve as a base point as the creature can evolve longer legs. The torso is a random size with random dimensions so that it is not small or large enough for the creature to evolve.

As the torso is created, the code randomly evolved a number of many limb cubes which yield the best fitness. This is decided based on a pre determined fitness function, and this creature will best adapt as many legs or limbs as it should. The number of cubes are decided and the code creates joints at random locations along torso within a range of values. The links are also positioned in a smooth connection points to not disrupt the motion of the creature and evolution. Sensor placement is found by a best probability to make the creature move and earn a good fitness value. If the sensors are green then it has a motor to allow the creature to walk, otherwise it is a sensor to seek the best fitness.

The mutations involved for this creature is pre determined and specific based on the fitness functions. The goal of the robot is to use locomotion to go near the grey cube in the world. The random creature first starts off by jittering around and has a low fitness value, but over the 100 generations of mutations of both the brain and the body. This duality of changes is random but also very powerfully chosen as whichever brain and body reaches the cube "survives". Thus the random evolution is selectionary and is going to always prefer the fitness value that is high. As seen in the diagram of the fitness curves, over time the value of the y axis, fitness, goes significantly high.

The reason we used different seeds is to place various populations and differing advantages. This allows us to see how quickly these robots evolve based on the different starting positions. Over 100 generations, these robots evolve to find the fitness that best suits the population and survives over the other children and parent robots.

Results:

This course has taught me much more than I have ever expected and shaped a new understanding of how evolution works. I am greatful to realize I can utilize the purity of evolution and simulate that very concept via Ludobots. I have learned to create an evolutionary algorithm that performs parallel hill climbing to find the best parent/offspring mutations. The concept of evolving a robot to follow instructions has unlimited uses. My robots have been told to evolve bodies and brains to go move closer to a cube that is set far away from them. They utilize a fitness function that decides whether they are making valid choices to survive or not. Each parent has an offspring and those two Ludobots are compared to one another until one of them is able to reproduce another Ludobot. Each successive Ludobot gets better and better at satisfying the fitness function since only the best ones move on to reproduce. This is pure evolution even in nature and we are simulating just that in simulation.

I have found that the best Ludobots are the ones that aren't necessarily bigger in size but more stable. Stability plays a big factor in locomotionn and the evoloved ludobots all have some sort of stabilizing source. Such as a ligament that helps propel them forward but also makes sure not too fly off and fall over. The random Ludobots are usually the ones who do not have stability and sort of stay stationary or even move away from the cube since they have not formed a body to help them move towards the cube. The lineages have been formed to be stable Ludobots that can propel towards the cube without falling over. There have been over trial and error some Ludobots that have evolved to be too stable and not have enough motor strength to go close to the cube. This is where these robots were "stuck" in evolution. Thus it was imperative to find good robots that have both stability and motor strength. These robots had to make a decision on what type of body to form as well as how much motor strength to pursue. Over time, evolution has helped them create the best body types and find a great source of motor locomotion. 


