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



def clean__FO__01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]

def clean__UK01a_100ms(t_old, dataRaw):
    # bad data in the interval t = 1950 to 2350
    scale = 1000000
    init = 2350
    a1 = int(2.83*scale)
    a2 = int(2.895*scale)
    
    dataTrimmed1 = dataRaw[init:a1]
    
    argOutliers = getOutliersIndices(dataTrimmed1)
    dataTrimmed1[argOutliers] = np.nan
    
    return [dataTrimmed1]

def clean__DE_OL01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]

def clean__US__TX01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    
    scale = 1000000
    a1 = int(1.2*scale)
    a2 = int(4.5*scale)
    b1 = int(5.125*scale)
    b2 = int(5.275*scale)
    
    dataTrimmed1 = dataRaw[0:a1]
    dataDeleted12 = dataRaw[a1:a2]
    dataTrimmed2 = dataRaw[a2:b1]
    dataDeleted23 = dataRaw[b1:b2]
    dataTrimmed3 = dataRaw[b2:-1]

    plt.subplot(2,1,1)
    plt.title("US__TX_100ms deleted")
    plt.plot(t_old[a1:a2], dataDeleted12, 'o', label='deleted 1', markersize=0.5)
    plt.subplot(2,1,2)
    plt.plot(t_old[b1:b2], dataDeleted23, 'o', label='deleted 2', markersize=0.5)
    plt.legend()
    saveImage(f'./images/temp/US__TX01_100ms.png')
    
    return [dataTrimmed1, dataTrimmed2, dataTrimmed3]
    
def clean__RUS01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    # plt.plot(t_old, dataRaw, 'o', label='dirty')
    dataRaw[argOutliers] = np.nan
    # plt.plot(t_old, dataRaw, 'o', markersize=.5, label='clean')
    # plt.legend()
    # plt.title("RUS01_100ms")
    # saveImage('./images/temp/rus_1.png')
    return [dataRaw]
    
    
def clean__EST01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]
    
def clean__IT_SI01_100ms(t_old, dataRaw):
    
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    
    scale = 1000000
    a1 = int(0.83*scale)
    a2 = int(1.37*scale)
    b1 = int(2.55*scale)
    b2 = int(2.73*scale)
    
    dataTrimmed1 = dataRaw[0:a1]
    dataDeleted12 = dataRaw[a1:a2]
    dataTrimmed2 = dataRaw[a2:b1]
    dataDeleted23 = dataRaw[b1:b2]
    dataTrimmed3 = dataRaw[b2:-1]

    plt.subplot(2,1,1)
    plt.title("IT_SI01_100ms deleted")
    plt.plot(t_old[a1:a2], dataDeleted12, 'o', label='deleted 1', markersize=0.5)
    plt.subplot(2,1,2)
    plt.plot(t_old[b1:b2], dataDeleted23, 'o', label='deleted 2', markersize=0.5)
    plt.legend()
    saveImage(f'./images/temp/IT_SI01_100ms.png')
    
    return [dataTrimmed1, dataTrimmed2, dataTrimmed3]
    
def clean__ES__PM01a_100ms():
    pass # data not available

def clean__TUR__IS01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]

def clean__UK02b_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    scale = 10000000
    a1 = int(0.73*scale)
    a2 = int(1.02*scale)
    
    dataTrimmed1 = dataRaw[0:a1]
    dataDeleted12 = dataRaw[a1:a2]
    dataTrimmed2 = dataRaw[a2:-1]
    plt.plot(t_old[a1:a2], dataRaw[a1:a2], 'o', ms=0.1)
    plt.grid(True)
    plt.title('UK02b_100ms__deleted')
    saveImage(f'./images/temp/UK02b_100ms__deleted.png')
    return [dataTrimmed1, dataTrimmed2]
    
def clean__PL01_100ms(t_old, dataRaw):
    scale = 1000000
    a = int(0.6*scale)
    b = -1
    dataTrimmed = dataRaw[a:b]
    
    argOutliers = getOutliersIndices(dataTrimmed)
    dataTrimmed[argOutliers] = np.nan
    
    return [dataTrimmed]
    
    
def clean__UK02a_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]
    
def clean__SE01_100ms(t_old, dataRaw):
    # scale = 1000000
    # a = int(0.44*scale)
    # b = int(0.47*scale)
    # b = -1
    # dataTrimmed = dataRaw[a:b]
    # plt.plot(t_old[a:b], dataRaw[a:b], 'o', markersize=0.5)
    # plt.title('SE01_100ms')
    # saveImage(f'./images/temp/SE01_1__{a}_to_{b}.png')
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    
    return [dataRaw]
    
def clean__DE__KA02_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]

def clean__PT_LI01_100ms(t_old, dataRaw):
    scale = 10000000
    a1 = int(1.36*scale)
    a2 = int(1.45*scale)
    b1 = int(1.884*scale)
    b2 = int(1.913*scale)
    
    dataTrimmed1 = dataRaw[0:a1]
    dataDeleted12 = dataRaw[a1:a2]
    dataTrimmed2 = dataRaw[a2:b1]
    dataDeleted23 = dataRaw[b1:b2]
    dataTrimmed3 = dataRaw[b2:-1]

    plt.subplot(2,1,1)
    plt.title("PT_LI01_100ms deleted")
    plt.plot(t_old[a1:a2], dataDeleted12, 'o', label='deleted 1', markersize=0.5)
    plt.subplot(2,1,2)
    plt.plot(t_old[b1:b2], dataDeleted23, 'o', label='deleted 2', markersize=0.5)
    plt.legend()
    saveImage('./images/temp/PT_LI01_100ms_deleted.png')
    
    argOutliers1 = getOutliersIndices(dataTrimmed1)
    dataTrimmed1[argOutliers1] = np.nan
    
    argOutliers2 = getOutliersIndices(dataTrimmed2)
    dataTrimmed2[argOutliers2] = np.nan
    
    argOutliers3 = getOutliersIndices(dataTrimmed3)
    dataTrimmed3[argOutliers3] = np.nan
    
    return [dataTrimmed1,dataTrimmed2,dataTrimmed3]

    
def clean__US__UT01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]
    
def clean__UK01_100ms():
    pass # similar data exists (UK01a_100ms)

def clean__FR01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan
    return [dataRaw]

def clean__HR01_100ms(t_old, dataRaw):
    argOutliers = getOutliersIndices(dataRaw)
    dataRaw[argOutliers] = np.nan

    # bad data in the interval t = 2.42e6 to 2.69e6
    scale = 1000000
    init = 0
    final = -1
    a1 = int(2.42*scale)
    a2 = int(2.69*scale)
    dataTrimmed1 = dataRaw[init:a1]
    dataTrimmed2 = dataRaw[a2:final]
    
    return [dataTrimmed1, dataTrimmed2]

