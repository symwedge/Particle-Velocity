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

savedir = "test/"
directories = natsorted(glob.glob(os.path.join("Omega/BW images", '*')))

i=0
for directory in directories:
    
    filenames = natsorted(glob.glob(os.path.join(directory, '*.png'))) 
    
    im = iio.imread(filenames[0])
    # plt.imshow(im)
    
    plt.figure()
    stacked = np.zeros((0, im.shape[1]), int)
    
    for file in filenames:
        im = iio.imread(file)
        im = im[500:700, 720:1150]
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
    plt.title('Tr', fontsize=15)
    #plt.title(f'A={searchitem.findall(os.path.basename(directory))[0]}', fontsize=15)
    #plt.colorbar()

    ax = plt.gca()
    ax.set_ylim([20, 0])
    ticks_y = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(np.around(y*5, 2)))
    ax.yaxis.set_major_formatter(ticks_y)
    
    np.savetxt(savedir+str(i)+".csv", stacked, delimiter=',')
    i+=1
    
    
    