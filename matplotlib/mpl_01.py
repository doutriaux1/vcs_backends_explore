import matplotlib.pyplot as plt
import numpy

# prepare some data
x = numpy.arange(360)  # in degrees
s = numpy.sin(x/180.*numpy.pi)
c = numpy.cos(x/180.*numpy.pi)

fig = plt.figure() 
plt.plot(x, s, color='blue', linewidth=2)
plt.plot(x, c, color='red', linewidth=2)

plt.savefig("plot_sine_cosine_mpl.png")
plt.show()