import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAnglesValuesF = numpy.load("data/targetAnglesValuesFront.npy")
targetAnglesValuesB = numpy.load("data/targetAnglesValuesBack.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth=5)
# matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

matplotlib.pyplot.plot(targetAnglesValuesF, label="frontLeg", linewidth=5)
matplotlib.pyplot.plot(targetAnglesValuesB, label="backLeg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
