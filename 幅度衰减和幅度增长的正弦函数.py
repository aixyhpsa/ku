import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x= np.arange(-40, 40, 0.01)
y1= np.sin(x)*np.exp(x*0.02)
y2= np.sin(x)*np.exp(x*-0.02)
plt.figure(1)

plt.subplot(221)
plt.plot(x, y1)

plt.subplot(222)
plt.plot(x,y2)

plt.show()