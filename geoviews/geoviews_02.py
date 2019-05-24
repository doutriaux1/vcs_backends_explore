import xarray as xr
import geoviews as gv
import geoviews.feature as gf
import xarray as xr
from cartopy import crs

gv.extension('bokeh', 'matplotlib')

# prepare some data

xarr = xr.open_dataset('/Users/doutriaux1/miniconda3/envs/jupyter-vcdat/share/cdat/sample_data/clt.nc', decode_times=False).load()
xarr = xarr["clt"][0]
kdims = ['longitude', 'latitude']
vdims = ['clt']
dataset = gv.Dataset(xarr, kdims=kdims, vdims=vdims)
# ensemble = dataset.to(gv.Image, ['longitude', 'latitude'])

# gv.output(ensemble.opts(cmap='viridis', colorbar=True, fig_size=200, backend='matplotlib') * gf.coastline(),
#           backend='matplotlib')
for backend in ["bokeh", "matplotlib"]:
    print("RENDERING WITH:", backend)
    img = gv.Image(dataset).opts(cmap="viridis", backend=backend) * gf.coastline()
    gv.save(img, filename="plot_clt_geoviews_{}.png".format(backend), backend=backend)