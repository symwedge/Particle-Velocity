from matplotlib import pyplot as plt
import numpy as np

y=(201.5128486, 192.8270524, 181.5154972, 168.5648451, 164.7062714, 155.6563085, 148.7678389, 137.4285223, 129.1921395,	
   120.1977829, 112.9736443, 103.7829793, 97.76235773, 88.43142083, 84.55481903, 79.05115189, 76.26590308, 74.55267063,	
   81.74695535, 138.7502959, 111.2232225)

x=np.arange(0,105,5)

# Define two regions to be shaded
region1_start, region1_end = 90,95
region2_start, region2_end = 90,95

# Shade the regions
plt.fill_between(x, y, where=(x >= region1_start) & (x <= region1_end), color='yellow', alpha=0.3)
plt.fill_between(x, y, where=(x >= region2_start) & (x <= region2_end), color='green', alpha=0.3)

# Add labels and a legend
plt.title("Omega = 0.126 Hz", fontsize=20)
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
# Plot the main line
plt.plot(x, y)
    
# Fit a line (linear regression) to the data
coefficients = np.polyfit(x[18:20], y[18:20], deg=1)
slope, intercept = coefficients

# Generate the fitted line using the obtained coefficients
fit_line = slope * x + intercept

# Plot the original data
plt.scatter(x, y)

# Plot the fitted line
plt.plot(x[18:20], fit_line [18:20], label=f'Fitted Line: y = {slope:.2f}x + {intercept:.2f}', color='red')

# plt.xlim(50,85)
# plt.ylim(0.12, 0.2)

# Add labels and a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# Display the coefficients of the fitted line (slope and intercept)
print(f'Slope (m) of the fitted line: {slope}')
print(f'Intercept (c) of the fitted line: {intercept}')

plt.savefig('Omega/0.126/maxgraph.png')

#%%

import numpy as np
from matplotlib import pyplot as plt 


# data from 0.126

mu1 = [122.9218677, 117.5925025, 90, 85, 86.08869983, 84.69650959, 77.43771903, 75.91418082, 129.1921395]

mu2 = [201.5128486, 192.8270524, 181.5154972, 168.5648451, 164.7062714, 155.6563085, 148.7678389,
       137.4285223, 129.1921395, 120.1977829, 112.9736443, 103.7829793, 97.76235773, 88.43142083, 
       84.55481903, 79.05115189, 76.26590308, 74.55267063, 81.74695535, 138.7502959, 111.2232225]

mu3 = [291.0370188, 279.7727058, 272.4425847, 259.8975046, 249.6787014, 241.6732657, 235.0251041,
       222.2843724, 218.2650582, 203.3507506, 197.020179, 190.6921298, 182.6678173, 167.8206942, 
       162.9611419, 153.1672006, 146.3082947, 139.6247511, 137.2645619, 138.7502959]

x1 = np.arange(0, 45, 5)
x2 = np.arange(0, 105, 5)
x3 = np.arange (0, 100, 5)


plt.figure()
plt.title('Omega=0.126 Hz')
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
plt.plot(x1, mu1, color='green', marker ='.')
plt.plot(x2, mu2, color='red', marker ='.')
plt.plot(x3, mu3, color='blue', marker ='.')
plt.grid(True)

plt.savefig('Omega/0.126/threelines.png')

#%%
plt.figure()
plt.title('Omega=0.126 Hz')
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
plt.plot(x2, mu2, color='red', marker ='.')
plt.plot(x3, mu3, color='blue', marker ='.')

#gradient 1
coefficients = np.polyfit(x2[18:20], mu2[18:20], deg=1)
slope, intercept = coefficients
fit_line = slope * x2 + intercept
plt.scatter(x2, mu2)
plt.plot(x2[18:20], fit_line [18:20], label=f'Fitted Line: y = {slope:.2f}x + {intercept:.2f}', color='black')
plt.legend()


plt.grid(True)

plt.savefig('Omega/0.126/maxgraph2.png')

#%%
plt.figure()
plt.title('Omega=0.126 Hz')
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
plt.plot(mu1, x1, color='green', marker ='.')
plt.plot(mu2, x2, color='red', marker ='.')
plt.plot(mu3, x3, color='blue',  marker ='.')
plt.grid(True)


plt.savefig('Omega/0.126/timethreelines.png')

#%%
plt.figure()
plt.title('Omega=0.126 Hz')
plt.ylabel('Maximum value (AU)', fontsize=15)
plt.xlabel('Timeframe (ms)', fontsize=15)
plt.plot(mu2, x2, color='red', marker ='.')
plt.plot(mu3, x3, color='blue',  marker ='.')
plt.grid(True)

plt.savefig('Omega/0.126/timetwolines.png')



