import numpy as np
import matplotlib.pyplot as plt

loadfile = 'ant_error.dat'
savefile = 'ant_error.png'

array_error = np.loadtxt(loadfile)

plt.plot(range(len(array_error)), array_error)
plt.xlabel("iteration")
plt.ylabel("error")
plt.savefig(savefile)
