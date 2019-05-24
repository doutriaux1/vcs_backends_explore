from bokeh.plotting import figure
# from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.io import export_png
import numpy

# prepare some data
x = numpy.arange(360)  # in degrees
s = numpy.sin(x/180.*numpy.pi)
c = numpy.cos(x/180.*numpy.pi)


# output to static HTML file
#output_file("sine_bokeh.html")

# a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, s, line_width=2, line_color="blue")
p.line(x, c, line_width=2, line_color="red")

# remove sidebar
p.toolbar.logo = None
p.toolbar_location = None

export_png(p, filename="plot_sine_cosine_bokeh.png")

# show the results
p.toolbar.logo = "normal"
p.toolbar_location = "right"
show(p)
