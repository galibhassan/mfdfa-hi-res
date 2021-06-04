from matplotlib import colors
import numpy as np
import os
import matplotlib.pyplot as plt

def getDataInfo(fileName):
    q = float(fileName.split("__q_")[1].split("__")[0])
    orderStr, fileExtension =  fileName.split("__ord_")[1].split(".")
    fittingOrder = int(orderStr)
    contentType = fileName.split("_")[0]
    datasetName = fileName.split("__q_")[0].split(f'{contentType}_')[1]

    return {
        "contentType": contentType,
        "datasetName": datasetName,
        "q":q,
        "fittingOrder": fittingOrder,
        "fileExtension": fileExtension
    }


DFALAG_DATA_DIR = './output2'

dataFOlderName = os.listdir(DFALAG_DATA_DIR)[8]
dataFOlderPath = f'{DFALAG_DATA_DIR}/{dataFOlderName}'
dataFileNames = os.listdir(dataFOlderPath)

q_arr = []
h_arr=[]

for dataFileName in dataFileNames:

    if(dataFileName.startswith("dfa_")):
        dataInfo = getDataInfo(dataFileName)

        if(dataInfo["fittingOrder"] ==1 ):
            print(dataFileName)
            dataDfa = np.load(f'{dataFOlderPath}/{dataFileName}')
            lagFileName = dataFileName.replace("dfa_", "lag_")
            dataLag = np.load(f'{dataFOlderPath}/{lagFileName}')

            fit =  np.polyfit(dataLag[11:-1], dataDfa[11:-1], 1)
            # print(fit)
            m = fit[0][0]
            c = fit[1][0]
            # print(m,c)
            modX = np.linspace(dataLag[0], dataLag[-1], 10)
            modY = m*modX + c
            #data = np.load
            plt.loglog(dataLag, dataDfa, 'o')
            plt.loglog(modX,modY, '--')

            plt.title(f'''
            Data: {dataInfo["datasetName"]}, detrending order: {dataInfo["fittingOrder"]}
            ''')
            q_arr.append(dataInfo["q"])
            h_arr.append(m)

plt.show()
plt.plot(q_arr, h_arr, 'o')
plt.title(f'''Dataset: {dataFOlderName}
Detrending order: {dataInfo["fittingOrder"]}''')
plt.xlabel("q")
plt.ylabel("h")
plt.show()