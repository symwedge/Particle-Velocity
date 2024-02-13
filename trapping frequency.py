
import imageio.v3 as iio
from matplotlib import pyplot as plt
import os
import numpy as np
import glob
from natsort import natsorted
import re
import matplotlib.ticker as ticker
import csv 
# from scipy.signal import find_peaks




lines = []
data=[]

savedir = "Trapping frequency/Images"
directories = natsorted(glob.glob(os.path.join("Trapping frequency/BW Images", '*')))
searchitem = re.compile(r'\d+\.\d+')


for directory in directories:
    filenames = natsorted(glob.glob(os.path.join(directory, '*.png'))) 
    im = iio.imread(filenames[0])
    # plt.imshow(im)

    plt.figure()
    stacked = np.zeros((0, im.shape[1]), int)
    
    for file in filenames:
        im = iio.imread(file)
        im = im[640:750, 700:1150]
        # plt.imshow(im)

        integral = im.sum(axis=0)
        #integral = integral / np.amax(integral)
        #integral = (integral - np.amin(integral) ) / ( np.amax(integral) - np.amin(integral))
        stacked = np.append(stacked, integral)

    stacked = stacked.reshape(len(filenames), im.shape[1])
    #stacked[stacked<0.65] = 0


    #plt.imshow(stacked, aspect='auto', vmin=0.5, vmax=1, interpolation='nearest', cmap='gray')
    #plt.imshow(stacked, aspect='auto', cmap='gray')
    plt.imshow(stacked, aspect='auto', cmap='viridis')
    plt.xlabel('Position (AU)', fontsize=12)
    plt.ylabel('Time (ms)', fontsize=12)
    plt.rc('xtick',labelsize=15)
    plt.rc('ytick',labelsize=15)
    plt.title(f'Fx={searchitem.findall(os.path.basename(directory))[0]} Hz ', fontsize=15)
    #plt.title(f'Width between the barriers={searchitem.findall(os.path.basename(directory))[0]} X $10^-$$^6$ m', fontsize=15)
    

    ax = plt.gca()
    ax.set_ylim([50, 0])
    ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(np.around(y*2, 2)))
    ax.yaxis.set_major_formatter(ticks_y)
    plt.draw()
    

    

    
    plt.savefig(f'{savedir}/Frequency_{searchitem.findall(os.path.basename(directory))[0]}.png', dpi=200)
    
    

    # data+=[(stacked.sum(axis=1))]
    # with open("F.csv", "w", newline="") as f:
    #     writer =csv.writer(f)
    #     writer.writerows(data)
        
    #     plt.figure()
    #     plt.plot(data[0])
    #     plt.xlabel("Time (ms)", fontsize=15)
    #     plt.ylabel("Number of atoms", fontsize=15)
    #     plt.rc('xtick',labelsize=10)
    #     plt.rc('ytick',labelsize=10)
    #     plt.title("0.4kHz", fontsize=20)
    #     plt.show()
    
    
# directories = natsorted(glob.glob(os.path.join("Frequency/Black and white images", '*')))
# directory = directories[0]
# filenames = natsorted(glob.glob(os.path.join(directory, '*.png')))
# file = filenames[10]
# im = iio.imread(file)
# im = im[580:740, 700:1100]
# plt.imshow(im)

# integral = im.sum(axis=0)
# plt.figure()
# plt.imshow(integral.reshape((1, 650)), aspect='auto')