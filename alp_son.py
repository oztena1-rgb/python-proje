Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import os
>>> import matplotlib.pyplot as plt
>>> x = [1, 2, 3]
>>> y = [2, 4, 6]
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x000001BEE3724C20>]
>>> plt.savefig(r"C:\Users\Hp\alp.png")
>>> desktop = os.path.join(os.path.expanduser("~"), "Desktop")
>>> plt.savefig(os.path.join(desktop,"alp.png"))