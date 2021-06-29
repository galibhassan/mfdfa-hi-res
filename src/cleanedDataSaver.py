import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules.dataCleaner.dataCleaner import *

CLEANED_DATA_DIR = f'../../data_cleaned'
datasetNames = [
    "HR01_100ms",
    "UK01a_100ms",
    # "UK01_100ms",
    "PL01_100ms",
    "FO-01_100ms",
    "TUR-IS01_100ms",
    "UK02b_100ms",
    "DE_OL01_100ms",
    "FR01_100ms",
    "PT_LI01_100ms",
    "US-TX01_100ms",
    "ES-PM01a_100ms",
    "RUS01_100ms",
    "US-UT01_100ms",
    "EST01_100ms",
    "IT-SI01_100ms",
    "SE01_100ms",
    "UK02a_100ms",
    "DE-KA02_100ms",
]


print('''
    ------Data Cleaning------
    ''')

fileCount = 0
for datasetName in datasetNames:
    # Feedback in console -------
    fileCount += 1
    feedbackIntro = f'''
        Working on dataset: {datasetName}
            File: {fileCount} / {len(datasetNames)}'''
    print(feedbackIntro)
    # ---------------------------
    

    dataRawPath = f'../../data/{datasetName}.csv'
    df = pd.read_csv(dataRawPath, delimiter=";")

    fColName = df.columns[1]
    f_data = df[fColName].to_numpy()
    t_domain = np.arange(0, len(f_data)) * 100 / 1000 / 60 / 60  # in hr
    t_domain_noScale = np.arange(0, len(f_data))

    datasetName_dunder = datasetName.replace('-', '__')
    functionName = f'clean__{datasetName_dunder}'
    callerString = f'{functionName}(t_domain_noScale, f_data)'
    print(f'''
        Evaluating:  {callerString}
    ''')
    cleanedDatasets = eval(callerString)

    dataChunkCount = 0
    for cleanedDataset in cleanedDatasets:
        dataSavePath = f'{CLEANED_DATA_DIR}/{datasetName}__{dataChunkCount}'
        np.save(dataSavePath, cleanedDataset)
        print(f'''
        Writing: {datasetName}__{dataChunkCount}
        ''')
        dataChunkCount += 1



feedbackOutro = '''
    -------- Done! --------
'''
print(feedbackOutro)
