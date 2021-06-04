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

# testing
fileName = "dfa_DE_OL01_100ms__q_-3.0__ord_2.npy"
print(getDataInfo(fileName=fileName))
