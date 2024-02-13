


#%%

from matplotlib import pyplot as plt
import numpy as np

mu1 = [216.6962706,	193.9016337, 166.9858761, 160.1822813,124.9926781,
       100.629619, 93.93738762, 95.91985384, 137.5426482, 244.7375213, 
       327.8081706,	386.6513852]

mu2 = [303.9750053, 284.7800346, 253.2809369, 244.6974901, 212.1687609,	
       175.5710873, 144.900754, 137.5426482, 105.8463043, 102.5948768, 
       91.68323119, 126.9574269, 165.9439337, 210.6563047, 298.5491563,
       338.3538279
]




x1 = np.arange(0, 60, 5)
x2 = np.arange(0, 80, 5)

plt.figure()
plt.title('A= 3.24')
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
plt.plot(x1,mu1, color='red', marker ='.')
plt.plot(x2,mu2, color='blue', marker ='.')



# Fit a line (linear regression) to the data
coefficients = np.polyfit(x1[6:14], mu1[6:14], deg=1)
slope, intercept = coefficients
# Generate the fitted line using the obtained coefficients
fit_line = slope * x1 + intercept
# Plot the original data
plt.scatter(x1, mu1)
# Plot the fitted line
plt.plot(x1[6:14], fit_line [6:14], label=f'Fitted Line: y = {slope:.2f}x + {intercept:.2f}', color='black')
plt.legend()


print(f'Slope (m) of the fitted line: {slope}')
print(f'Intercept (c) of the fitted line: {intercept}')


# Fit a line (linear regression) to the data
coefficients = np.polyfit(x2[11:15], mu2[11:15], deg=1)
slope, intercept = coefficients
# Generate the fitted line using the obtained coefficients
fit_line = slope * x2 + intercept
# Plot the original data
plt.scatter(x2, mu2)
# Plot the fitted line
plt.plot(x2[11:15], fit_line [11:15], label=f'Fitted Line: y = {slope:.2f}x + {intercept:.2f}', color='green')
plt.legend()


print(f'Slope (m) of the fitted line: {slope}')
print(f'Intercept (c) of the fitted line: {intercept}')



plt.grid(True)
#plt.savefig('A/3.24/maxgraph.png')


pixelsize=5.86/20

v1=pixelsize*12.951027493028558
v2=pixelsize*11.189751183999986

print(v1)
print(v2)


