import vcs
import numpy
import cdms2
import MV2

# prepare some data
x = numpy.arange(360)  # in degrees
s = MV2.sin(x/180.*numpy.pi)
c = MV2.cos(x/180.*numpy.pi)

x = cdms2.createAxis(x)  # in degrees
s.setAxis(0,x)
c.setAxis(0,x)


canvas = vcs.init()

canvas.yxvsx(s, linewidth=2, linecolor="blue", markersize=0)
canvas.yxvsx(c, linewidth=2, linecolor="red", markersize=0)

canvas.png("plot_sine_cosine_vcs.png")
canvas.interact()
