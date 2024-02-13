
import numpy as np
import matplotlib.pyplot as plt


y= [0.00671,
0.00741,
0.007,
0.00716,
0.00851,
0.00862]

x= [0.324,
0.405,
0.485,
0.566,
0.647,
0.728]

plt.plot(x,y, 'o', color='black')

y_error = [0.00048,
0.00077,
0.00077,
0.00072,
0.00053,
0.00041]
plt.errorbar(x, y, yerr = y_error, fmt='o',ecolor = 'black',color='red', lw=2)

line1, = plt.plot(x,y, color='black', lw=5, label='Data')
plt.title("C", fontsize=40)
plt.xlabel("A/$K_{B}$ ($\mu$K)", fontsize=30)
plt.ylabel("$V_{r}$ (m/s)", fontsize=30)
plt.rc('xtick',labelsize=50)
plt.rc('ytick',labelsize=50)
plt.ylim(0.005,0.01)
plt.xlim(0.22,0.85)


# Define the constants
x = np.linspace(0.3, 0.8, 1000)  
k = 1.3806505e-23
m = 87 * 1.66053886e-27
pi = np.pi


expression = np.sqrt(0.5 * x * 1e-6 * k / m + (0.62 * 2 * pi * 28 * 50 * 1e-6) ** 2)

# Plot the expression
plt.plot(x, expression)

line2, = plt.plot(x,expression, color='red', lw=5, label='Theory')
leg = plt.legend(loc='upper left', prop={'size': 50})
plt.grid(True)
plt.show()

#%%


import numpy as np
import matplotlib.pyplot as plt


y= [0.00542,
0.00542,
0.00734,
0.0075,
0.00851,
0.00808,
0.00911,
0.0105,
0.01094,
0.01683]

x= [12.8,
16.5,
20,
23.4,
28,
29.3,
38,
41.9,
51.1,
60.4]

plt.plot(x,y, 'o', color='black')

y_error = [0.000685,
0.000627,
0.0009,
0.0007547,
0.00053,
0.0008,
0.000765,
0.00137,
0.00115,
0.00114]
plt.errorbar(x, y, yerr = y_error, fmt='o',ecolor = 'black',color='grey', lw=2)

line1, = plt.plot(x,y, color='black', lw=5, label='Data')
plt.title("C", fontsize=40)
plt.xlabel("A/$K_{B}$ ($\mu$K)", fontsize=30)
plt.ylabel("$V_{r}$ (m/s)", fontsize=30)
plt.rc('xtick',labelsize=50)
plt.rc('ytick',labelsize=50)
# plt.ylim(0.003,0.02)
# # plt.xlim(0.22,0.85)


# Define the constants
x = np.linspace(10, 65, 1000)  
k = 1.3806505e-23
m = 87 * 1.66053886e-27
pi = np.pi


expression = np.sqrt(0.5 * 0.647 * 1e-6 * k / m + (0.62 * 2 * pi * x * 50 * 1e-6) ** 2)

# Plot the expression
plt.plot(x, expression)

line2, = plt.plot(x,expression, color='red', lw=5, label='Theory')
leg = plt.legend(loc='upper left', prop={'size': 50})
plt.grid(True)
plt.show()













