import os
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd

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


DATA_DIR_MAIN = "../../data"
FREQ_PLOT_IMAGE_OUTPUT_DIR = "./images/frequency_plot"

dataFileNames = os.listdir(DATA_DIR_MAIN)
fileCount = 0
for dataFileName in dataFileNames:
    fileCount += 1
    dataPath = f"{DATA_DIR_MAIN}/{dataFileName}"
    df = pd.read_csv(dataPath, delimiter=";")
    # df = df_full.iloc[0:999]

    
    # Show status
    print(
    f"""
        Processing ... ...
        file: {fileCount}/{len(dataFileNames)},
    """
    )
    
    tColName = df.columns[0]
    dataSpanString = f"{df[tColName].iloc[0]} to {df[tColName].iloc[-1]}"
    fColName = df.columns[1]
    refFreq = int(fColName.split("_")[0].split("f")[1])
    f_data = df[fColName].to_numpy()
    t_domain = np.arange(0, len(f_data)) * 100 / 1000 / 60 / 60  # in hr
    timeUnit = "hour"
    
    
    # plot of time vs frequency
    cutoffFreqDev  = 300
    plt.plot(
        t_domain[np.abs(f_data) < cutoffFreqDev],
        f_data[np.abs(f_data) < cutoffFreqDev],
        'o',
        color="#198A97",
        markersize=0.5,
        label=f"Deviation from {refFreq}Hz",
    )
    plt.plot(
        t_domain[np.abs(f_data) >= cutoffFreqDev],
        f_data[np.abs(f_data) >= cutoffFreqDev],
        'd',
        color="#F7196D",
        markersize=3,
        label=f"outliers",
    )
    # plt.plot(xDataHistNP, yDataHistNP, 'o', markersize=0.5, label=f'np.hist(), bins={nBinsNP}', alpha=0.4)
    '''
    plt.hlines(
        0,
        t_domain[0],
        t_domain[-1],
        colors="orange",
        linestyles="--",
        label=f"{refFreq}hz",
        data=None,
    )
    '''
    plt.xlabel(f"Time ({timeUnit})")
    plt.ylabel(f"Frequency Deviation (in mHz) from {refFreq}Hz")
    plt.title(
        f"""Time vs Frequency-deviation, Dataset: {dataFileName}
    Time span: {dataSpanString}
    Data length: {len(f_data)}, |outliers|>{cutoffFreqDev}mHz""",
        loc="left",
    )
    plt.legend(loc="upper left")

    # saving figure
    tvsf_imageFileName = f't_vs_df__{dataFileName.split(".")[0]}'
    tvsf_imagePath = f"{FREQ_PLOT_IMAGE_OUTPUT_DIR}/{tvsf_imageFileName}"
    saveImage(tvsf_imagePath)
