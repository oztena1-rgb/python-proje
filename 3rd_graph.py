Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import matplotlib.pyplot as plt
>>> nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4,57.3]
>>> years = range(2000, 2013)
>>> plt.plot(years, nyc_temp, marker='o')
[<matplotlib.lines.Line2D object at 0x0000020084384C20>]
>>> plt.show()
