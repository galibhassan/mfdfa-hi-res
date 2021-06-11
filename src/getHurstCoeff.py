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


DFALAG_DATA_DIR = './output2'

dataFOlderNames = os.listdir(DFALAG_DATA_DIR)

for dataFOlderName in dataFOlderNames:

    dataFOlderPath = f'{DFALAG_DATA_DIR}/{dataFOlderName}'
    dataFileNames = os.listdir(dataFOlderPath)


    detrendOrders = [0,1,2]

    for detrendOrder in detrendOrders:
        q_arr = []
        h_arr=[]
        for dataFileName in dataFileNames:
            if(dataFileName.startswith("dfa_")):
                dataInfo = getDataInfo(dataFileName)

                if(dataInfo["fittingOrder"] == detrendOrder ):
                    # print(dataFileName)
                    dataDfa = np.load(f'{dataFOlderPath}/{dataFileName}')
                    lagFileName = dataFileName.replace("dfa_", "lag_")
                    dataLag = np.load(f'{dataFOlderPath}/{lagFileName}')

                    fit =  np.polyfit(np.log(dataLag[11:-1]), np.log(dataDfa[11:-1]), 1)
                    m = fit[0][0]
                    c = fit[1][0]
                    modX = np.logspace(np.log(dataLag[0]), np.log(dataLag[-1]), 10, base=np.e)
                    # modY = m*modX + c
                    modY = np.exp(c) *(modX**m)
                    plt.loglog(dataLag, dataDfa, 'o')
                    plt.loglog(modX,modY, 'o--')

                    plt.title(f'''
                    Data: {dataInfo["datasetName"]}, detrending order: {dataInfo["fittingOrder"]}
                    ''')
                    q_arr.append(dataInfo["q"])
                    h_arr.append(m)
                    

        np.save(f'./outputHurstData/q__{dataFOlderName}__ord_{detrendOrder}', q_arr)
        np.save(f'./outputHurstData/h__{dataFOlderName}__ord_{detrendOrder}', h_arr)

    
        saveImage(f'./images/hurst_cLagM/fit__dataset_{dataFOlderName}__detrendOrder_{detrendOrder}')

        plt.plot(q_arr, h_arr, 'o')
        plt.title(f'''Dataset: {dataFOlderName}
        Detrending order: {detrendOrder}''')
        plt.xlabel("q")
        plt.ylabel("h")
        saveImage(f'./images/hurst_cLagM/hurst__dataset_{dataFOlderName}__detrendOrder_{detrendOrder}')
