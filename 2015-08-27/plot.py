import matplotlib.pyplot as plt

x_axis = range(1,129)
speedup = [1 / (0.1 + 0.9 / p) for p in range(1,129)]
plt.plot(x_axis,speedup,label='ideal speedup',linewidth=8)
plt.xlabel('number of cores')
plt.ylabel('ideal speedup')
plt.legend()
plt.show()
