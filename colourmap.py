# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:22:52 2023

@author: cm846
"""
import imageio.v3 as iio
from matplotlib import pyplot as plt
import os
import numpy as np
import glob
from natsort import natsorted
import re
import matplotlib.ticker as ticker
import csv

data=[]

savedir = "fermi acceleration new\Barrier sizes/Images"
directories = natsorted(glob.glob(os.path.join("fermi acceleration new\Barrier sizes/Black and White Images", '*')))
searchitem = re.compile(r'\d+\.\d+')

for directory in directories:
    filenames = natsorted(glob.glob(os.path.join(directory, '*.png'))) 
    im = iio.imread(filenames[0])
    # plt.imshow(im)

    plt.figure()
    stacked = np.zeros((0, im.shape[1]), int)
    
    for file in filenames:
        im = iio.imread(file)
        im = im[850:950, 1050:1500]
        # plt.imshow(im)

        integral = im.sum(axis=0)
        #integral = integral / np.amax(integral)
        #integral = (integral - np.amin(integral) ) / ( np.amax(integral) - np.amin(integral))
        stacked = np.append(stacked, integral)

    stacked = stacked.reshape(len(filenames), im.shape[1])
    #stacked[stacked < 0.9] = 0


    #plt.imshow(stacked, aspect='auto', cmap='gray')
    plt.imshow(stacked, aspect='auto', cmap='viridis')
    plt.xlabel('Position (AU', fontsize=10)
    plt.ylabel('Time (AU)', fontsize=10)
    plt.rc('xtick',labelsize=15)
    plt.rc('ytick',labelsize=15)
    plt.title(f'Barrier Size={searchitem.findall(os.path.basename(directory))[0]} px', fontsize=15)
    #plt.colorbar()

    ax = plt.gca()
    ax.set_ylim([60, 0])
    ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(np.around(y*0.5, 0)))
    ax.yaxis.set_major_formatter(ticks_y)
    plt.draw()
    
    
    
    ycoords = []
    xcoords = []
    slopes = []


    plt.plot(xcoords, ycoords, color='red')
    for nr, i in enumerate(xcoords):
        plt.text(xcoords[nr], ycoords[nr], [xcoords[nr], ycoords[nr]*5])

    
    plt.savefig(f'{savedir}/Barrier size_{searchitem.findall(os.path.basename(directory))[0]}.png', dpi=200)
    #np.savetxt(f'{savedir}/text/A_{searchitem.findall(os.path.basename(directory))[0]}.txt', stacked)
    np.savetxt(f'{savedir}/csv/Barrier size_{searchitem.findall(os.path.basename(directory))[0]}.csv', stacked, delimiter=',')
    
    data+=[(stacked.sum(axis=1))]
    with open("A.csv", "w", newline="") as f:
        writer =csv.writer(f)
        writer.writerows(data)


# directories = natsorted(glob.glob(os.path.join("Phi/Black and white images", '*')))
# directory = directories[0]
# filenames = natsorted(glob.glob(os.path.join(directory, '*.png')))

#%%
file = filenames[10]
im = iio.imread(file)
im = im[850:90, 1150:1700]
plt.imshow(im)

# integral = im.sum(axis=0)
# plt.figure()
# plt.imshow(integral.reshape((1, 650)), aspect='auto')