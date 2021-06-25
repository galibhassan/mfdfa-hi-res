import os
import numpy as np
import matplotlib.pyplot as plt

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

    
def getOutliersIndices(y, confidence=3):
    diff1 = np.diff(y)
    sigmaDiff = np.std(diff1)

    outliersGuess = diff1[np.abs(diff1)>confidence*sigmaDiff]
    inds = []
    for outlier in outliersGuess:
        argOutliersGuess = np.argwhere(diff1==outlier)
        for argOG in argOutliersGuess:
            inds.append(argOG)
    inds = np.array(inds).flatten()
    # print(inds)    

    indDiffs = np.diff(inds)

    argOutliers = []
    for i in range(len(indDiffs)):
        if (indDiffs[i]==1):
            argOutliers.append(inds[i+1])

    return argOutliers



def clean__FO__01_100ms():
    pass

def clean__UK01a_100ms(t_old, data__UK01a_100ms):
    # bad data in the interval t = 1950 to 2350
    a = 2350
    b = -1
    t = t_old[a:b]
    cleaned_freq_dev = data__UK01a_100ms[a:b]
    # plt.plot(t, cleaned_freq_dev, 'o', markersize=0.5, color='red')
    # saveImage('./images/temp/temp.png')
    return [cleaned_freq_dev]
    
    
    


def clean__DE_OL01_100ms():
    pass
def clean__US__TX01_100ms():
    pass
def clean__RUS01_100ms():
    pass
def clean__EST01_100ms():
    pass
def clean__IT_SI01_100ms(t_old, dataRaw):
    # Clean the abrupt jump
    scale = 1000000
    a1 = int(2.7*scale)
    a2 = int(2.8*scale)
    maxInd1 = np.argmax(dataRaw[a1:a2])    
    dataRaw[a1+maxInd1] = np.nan
    
    # clean the straight-lines
    b1= int(0.83*scale)
    b2= int(1.37*scale)
    c1= int(2.55*scale)
    c2= int(2.73*scale)
    
    cleaned_freq_dev = dataRaw
    
    # plt.plot(t_old[b2:c1], cleaned_freq_dev[b2:c1], 'o', markersize=0.5)
    # saveImage('./images/temp/temp1.png')
    
    chunk2 = cleaned_freq_dev[c2:-1]
    argOutliers = getOutliersIndices(chunk2)
    # print(argOutliers)
    
    
    plt.plot(t_old[c2:-1], cleaned_freq_dev[c2:-1], 'o', markersize=5, alpha=0.5, label='dirty')
    
    chunk2[argOutliers] = np.nan
    plt.plot(t_old[c2:-1], chunk2, 'o', markersize=0.5, alpha=0.5, label='clean')
    plt.legend()
    saveImage('./images/temp/temp2_1.png')
    
    
    # return [data_SI01_100ms]
    
    
    
def clean__ES__PM01a_100ms():
    pass
def clean__TUR__IS01_100ms():
    pass
def clean__UK02b_100ms():
    pass
def clean__PL01_100ms():
    pass
def clean__UK02a_100ms():
    pass
def clean__SE01_100ms():
    pass
def clean__DE__KA02_100ms():
    pass
def clean__PT_LI01_100ms():
    pass
def clean__US__UT01_100ms():
    pass
def clean__UK01_100ms():
    pass
def clean__FR01_100ms():
    pass
def clean__HR01_100ms(t_old, data_HR01_100ms):
    # bad data in the interval t = 2.42e6 to 2.69e6
    scale = 1000000
    init = 0
    final = -1
    a = int(2.42*scale)
    b = int(2.69*scale)
    
    t1 = t_old[init:a]
    t2 = t_old[b:final]
    cleaned_freq_dev__1 = data_HR01_100ms[init:a]
    cleaned_freq_dev__2 = data_HR01_100ms[b:final]
    
    # plt.plot(t1, cleaned_freq_dev__1, 'o', markersize=0.5, color='red')
    # saveImage('./images/temp/temp1.png')
    # plt.plot(t2, cleaned_freq_dev__2, 'o', markersize=0.5, color='blue')
    # saveImage('./images/temp/temp2.png')
    
    return [cleaned_freq_dev__1, cleaned_freq_dev__2]

