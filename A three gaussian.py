import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from PIL import Image
import os

# Replace 'your_image.png' with the path to your PNG image
image_path = 'A/5.66/BW Images/15.53.14.png'

image = Image.open(image_path)

# Convert the image to a NumPy array
image_data = np.array(image)
#plt.imshow(image)

# Use NumPy slicing to extract the desired region
region_data = image_data[580:700, 720:1150]
region_data[region_data>230] = np.mean(region_data)

# Choose a colormap (replace 'viridis' with the colormap you prefer)
cmap_name = 'viridis'
cmap = plt.get_cmap(cmap_name)

# Normalize the image data to be in the range [0, 1]
normalized_data = (region_data - region_data.min()) / (region_data.max() - region_data.min())

# Apply the colormap to the normalized data
colourmapped_data = cmap(normalized_data)


# Display the original region and the colormap side by side
#fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# # Original region
# ax[0].imshow(region_data, cmap='gray')  # Displaying in grayscale for comparison
# ax[0].set_title('Original Region')

# Colormap of the region
plt.imshow(colourmapped_data)
plt.title('A= 5.66, (30-35 ms)')

plt.savefig('A/5.66/sections/30-35 ms')
plt.show()

#%%

def gaussian(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

def two_gaussians(x, mu1, sigma1, A1, mu2, sigma2, A2,offset):
    return gaussian(x, mu1, sigma1, A1) + gaussian(x, mu2, sigma2, A2) +offset
from scipy.optimize import curve_fit
plt.figure(2)
newdata = np.sum(normalized_data,axis=0)/len(normalized_data)
plt.plot(newdata)
xscale = np.linspace(0,429,430)
popt,pcov = curve_fit(two_gaussians, xscale, newdata,p0=[150, 2, 1, 250, 1, 1, 1] )

    
print("Fitted Parameters:")
print("mu1 =", popt[0])
print("sigma1 =", popt[1])
print("A1 =", popt[2])
print("mu2 =", popt[3])
print("sigma2 =", popt[4])
print("A2 =", popt[5])
print("offset", popt[6])

print("Fitted Parameters:")
print(popt[0])
print(popt[1])
print(popt[2])
print(popt[3])
print(popt[4])
print(popt[5])




# # Label the peaks with popt values
# for i in range(3):
#     Mu_label = f'Mu {i+1}: {popt[i*3]:.2f}'
#     Sigma_label = f'Sigma {i+1}: {popt[i*3+1]:.2f}'
#     Amplitude_label = f'Amplitude {i+1}: {popt[i*3+2]:.2f}'
    
#     label_text = f'{Mu_label}\n{Sigma_label}\n{Amplitude_label}'
#     plt.text(popt[i*3], 0.85*np.amin(newdata), label_text, color='red', ha='center')
#     plt.vlines(popt[i*3], ymin = 1.05*np.amin(newdata), ymax= popt[i*3+2]+popt[9], color="black", linestyles="dashed")

# plt.legend()

plt.title('Gaussian fit: A=5.66 (30-35 ms)')


plt.grid(True)
plt.ylim([0.8*np.amin(newdata), 1.1*np.amax(newdata)])
plt.plot(xscale, two_gaussians(xscale,*popt), color="red")
figure =plt.gcf()
figure.set_size_inches(12, 8)
plt.savefig('A/5.66/Gauss fits/30-35 ms', dpi=200)



#%%

def gaussian(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

def three_gaussians(x, mu1, sigma1, A1, mu2, sigma2, A2,offset):
    return gaussian(x, mu1, sigma1, A1) + gaussian(x, mu2, sigma2, A2) +offset
from scipy.optimize import curve_fit
plt.figure(3)
plt.imshow(colourmapped_data)
newdata = np.sum(normalized_data,axis=0)/len(normalized_data)
# plt.plot(newdata)
xscale = np.linspace(0,429,430)
popt,pcov = curve_fit(three_gaussians, xscale, newdata,p0=[150, 2, 1, 250, 5, 1, 1])


plt.title('Gaussian fit: A=5.66, (30-35 ms)')

plt.plot(xscale, 80-100*three_gaussians(xscale,*popt), color="red")

plt.savefig('A/5.66/Gauss colourmaps/30-35 ms')









