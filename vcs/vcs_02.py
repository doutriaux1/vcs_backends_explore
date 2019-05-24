import vcs
import numpy
import cdms2
import MV2

# prepare some data
f = cdms2.open(vcs.sample_data+"/clt.nc")
clt = f("clt")


canvas = vcs.init()
canvas.plot(clt)
canvas.png("plot_clt_vcs.png")

canvas.interact()
