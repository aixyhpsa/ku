import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x= np.arange(-5, 5, 0.01)
y1= np.cos(x)
y2=np.cos(2*x)
y3=np.cos(3*x)
plt.figure(1)

plt.subplot(221)
plt.plot(x, y1)

plt.subplot(222)
plt.plot(x,y2)

plt.subplot(223)
plt.plot(x,y3)

plt.show()