import vcs
import numpy
import cdms2
import MV2

# prepare some data
f = cdms2.open(vcs.sample_data+"/geos5-sample.nc")
clt = f("tmpu")
f = cdms2.open(vcs.sample_data+"/clt.nc")
clt = f("clt")


canvas = vcs.init()

dv3d = vcs.get3d_scalar("Hovmoller3D")
#dv3d.ToggleClipping = ( 40, 360, -28, 90 )
dv3d.ToggleVolumePlot = vcs.on
dv3d.VerticalScaling = 3.0
#dv3d.ToggleSurfacePlot = vcs.on 
#dv3d.IsosurfaceValue = 31.0
#dv3d.ScaleOpacity = [0.0, 1.0]
#dv3d.BasemapOpacity = 0.5
dv3d.Camera={ 'Position': (-421, -991, 879), 
              'ViewUp': (.29, 0.77, 0.68), 
              'FocalPoint': (146.7, 8.5, -18.6)  }
#dv3d.ScaleColormap = [ -46.0, 48.0 ] 
#dv3d.ScaleTransferFunction =  [ 12.0, 77.0 ]

canvas.plot( clt, dv3d )

canvas.png("plot_clt_3D_vcs.png")

canvas.interact()
