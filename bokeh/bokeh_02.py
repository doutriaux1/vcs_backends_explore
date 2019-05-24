from bokeh.plotting import figure
# from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.io import export_png
import cdms2

# prepare some data
f = cdms2.open("/Users/doutriaux1/miniconda3/envs/jupyter-vcdat/share/cdat/sample_data/clt.nc")
clt = f("clt")

# output to static HTML file
#output_file("sine_bokeh.html")

# a new plot with a title and axis labels
p = figure(title="simple line example") #,x_range=(clt.getAxis(-1)[0], clt.getAxis), y_range=(0, 2))

# add a line renderer with legend and line thickness
p.image(image=[clt[0]], x=0, y=0, dw=clt.shape[-1], dh=clt.shape[-2], palette="Viridis256")

# remove sidebar
p.toolbar.logo = None
p.toolbar_location = None

export_png(p, filename="plot_clt_bokeh.png")

# show the results
p.toolbar.logo = "normal"
p.toolbar_location = "right"
show(p)
