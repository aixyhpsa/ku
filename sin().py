import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x = np.arange(-5.0, 5.0, 0.01)
y1 = np.sin(x)
plt.figure(1)
plt.subplot(111)
plt.plot(x, y1)
plt.show()