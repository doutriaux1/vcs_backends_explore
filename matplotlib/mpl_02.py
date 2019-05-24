import matplotlib.pyplot as plt
import cdms2

# prepare some data
f = cdms2.open("/Users/doutriaux1/miniconda3/envs/jupyter-vcdat/share/cdat/sample_data/clt.nc")
clt = f("clt")

fig = plt.figure() 
plt.pcolormesh(clt[0])

plt.savefig("plot_clt_mpl.png")
plt.show()