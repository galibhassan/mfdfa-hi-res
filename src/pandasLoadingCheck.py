import numpy as np
import pandas as pd
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


DATA_DIR_MAIN = "./dataDir"
OUTPUT_DIR = "./output"
dataFileName= "FO-01_100ms.csv"

dataPath = f"{DATA_DIR_MAIN}/{dataFileName}"
df_full = pd.read_csv(dataPath, delimiter=";")
df_partial = df_full.iloc[0:10]
print(df_full.shape)
print(df_partial.shape)


tColName = df.columns[0]
dataSpanString = f"{df[tColName].iloc[0]} to {df[tColName].iloc[-1]}"
fColName = df.columns[1]
refFreq = int(fColName.split("_")[0].split("f")[1])
f_data = df[fColName].to_numpy()
t_domain = np.arange(0, len(f_data)) * 100 / 1000 / 60 / 60  # in hr
timeUnit = "hour"

plt.plot(t_domain, f_data)
saveImage(f'{OUTPUT_DIR}/sampleImage.png')