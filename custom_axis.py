import matplotlib.pyplot as plt
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plt.plot(nyc_temp, marker='o')
from pylab import axis
axis()
(0.0, 12.0, 53.0, 57.3)
axis(ymin=0)
(0.0, 12.0, 0, 57.5)
plt.xlabel("Month")
plt.ylabel("Temperature (°F)")
plt.show()
