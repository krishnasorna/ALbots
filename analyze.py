import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg")
matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

