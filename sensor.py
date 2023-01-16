import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.thousand)

    def Get_Value(self,time):
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        