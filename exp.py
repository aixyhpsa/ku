import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x= np.arange(-3, 3, 0.01)
y1= np.exp(x)
plt.figure(1)
plt.subplot(111)
plt.plot(x, y1)
plt.plot(-x,y1)

plt.show()