from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import os


def saveImage(imagePath):
    plt.savefig(
        imagePath,
        facecolor="w",
        edgecolor="w",
        orientation="landscape",
        format=None,
        dpi=300,
        transparent=False,
        bbox_inches=None,
        pad_inches=0.1,
        metadata=None,
    )
    plt.clf()


OUTPUT_DIR_MAIN = './output2'
NUMPY_FILE_EXTENSION = '.npy'
IMAGE_DIR = './images'

dirs = os.listdir(OUTPUT_DIR_MAIN)
filenameSample = 'dfa_DE_OL01_100ms__q_-0.5__ord_0.npy'


ORDERS = [0,1,2]
for dirname in dirs:
    currentDirPath = f'{OUTPUT_DIR_MAIN}/{dirname}'
    currentDatasetName = dirname.split('output_')[1]
    allFIles = os.listdir(currentDirPath)
    
    """ 
    orderifiedFiles = {
        "order0":[],
        "order1":[],
        "order2":[]
    }
    """
    orderifiedFiles = [
        [],[],[]
    ]

    for fileName in allFIles:
        if fileName.startswith("dfa") and fileName.endswith(NUMPY_FILE_EXTENSION):

            if '__ord_0.npy' in fileName:
                orderifiedFiles[0].append(fileName)
            elif '__ord_1.npy' in fileName:
                orderifiedFiles[1].append(fileName)
            else:
                orderifiedFiles[2].append(fileName)
                

    for order in range(len(orderifiedFiles)):
        currentOrderFiles = orderifiedFiles[order]
        fileName = None
        for fileName in currentOrderFiles:
            chunk0 = fileName.split("__ord_")[0]
            chunk1 = "__ord_"
            chunk2 = f"{order}.npy"
            filenameWithOrder = chunk0+chunk1+chunk2
            q = float(chunk0.split('__q_')[1])

            dfaFilePath = f'{currentDirPath}/{filenameWithOrder}'
            lagFilePath = dfaFilePath.replace("dfa_", "lag_")
            dfaData = np.load(dfaFilePath)
            lagData = np.load(lagFilePath)

            if q>0:
                plotColor = '#6BAED6' # blue
            else:
                plotColor = '#F79E60' # orange
                

            plt.loglog(lagData, dfaData, 'o-', color=plotColor, markersize=2, linewidth=0.5, label=f'q:{q}')
            plt.xlabel("lag s")
            plt.ylabel(f"$F_q(s)$")
            plt.title(f'''Data: {currentDatasetName}, Fitting order: {order}
            Blue ~ q>0, Orange ~ q<0
            ''')
            # plt.legend(loc="lower right", ncol=6)
        saveImage(f'{IMAGE_DIR}/MFSpec__{currentDatasetName}__ord_{order}.png')    
        