import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def saveImage(imagePath):
    plt.savefig(
        imagePath,
        facecolor="w",
        edgecolor="w",
        orientation="portrait",
        format=None,
        dpi=300,
        transparent=False,
        bbox_inches=None,
        pad_inches=0.1,
        metadata=None,
    )
    plt.clf()


fileNames = os.listdir('../../data_cleaned')
filePath = '../../data_cleaned'
for datasetName in fileNames:
    
# datasetName = fileNames[3]
    data = np.load(f'{filePath}/{datasetName}')
    f_data = data[~np.isnan(data)]

    nBins = 1000
    histY, binEdges = np.histogram(f_data , bins=nBins, density=True)
    xDataHistNP = binEdges[0:-1]
    plt.plot(xDataHistNP, histY, 'o', ms=1, label='np.histogram')

    # fitting with rv.fit()
    locFit, scaleFit = norm.fit(f_data, loc=0)
    densityFit_STAT = norm.pdf(xDataHistNP, loc=locFit, scale=scaleFit)
    plt.plot(xDataHistNP, densityFit_STAT, '-', linewidth=1, label='norm.fit()')
    plt.legend()
    plt.grid(True)
    plt.title(f'''{datasetName}
    dataPoints={len(f_data)}''')


    saveImage(f'./images/fittingTest/{datasetName}.png')
