import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)
y = (x ** 3) - 2 * x + 4
plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.title('Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()