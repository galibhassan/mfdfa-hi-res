import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MFDFA import MFDFA
import os

DATA_DIR_MAIN = "./sample_data_folder"
OUTPUT_DIR = "./output"

INTRO = f"""
    ----------
    This program will collect all data files from:
    {DATA_DIR_MAIN}
    and output plots and data in:
    {OUTPUT_DIR}
    ------------

"""
print(INTRO)


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


def makeOutputDir(dataFileName, output_dir):
    newDirName = f'output_{dataFileName.split(".")[0]}'
    newDirPath = f"{output_dir}/{newDirName}"
    if os.path.exists(newDirPath) != True:
        os.makedirs(newDirPath)
    return newDirPath


# Files in the main data directory
dataFileNames = os.listdir(DATA_DIR_MAIN)
fileCount = 0
for dataFileName in dataFileNames:
    fileCount += 1
    dataPath = f"{DATA_DIR_MAIN}/{dataFileName}"
    df = pd.read_csv(dataPath, delimiter=";")

    tColName = df.columns[0]
    dataSpanString = f"{df[tColName].iloc[0]} to {df[tColName].iloc[-1]}"
    fColName = df.columns[1]
    refFreq = int(fColName.split("_")[0].split("f")[1])
    f_data = df[fColName].to_numpy()
    t_domain = np.arange(0, len(f_data)) * 100 / 1000 / 60 / 60  # in hr
    timeUnit = "hour"

    # Create the output subfolder
    outputSubDir = makeOutputDir(dataFileName, OUTPUT_DIR)

    # plot of time vs frequency
    plt.plot(t_domain, f_data, label=f"Deviation from {refFreq}Hz")
    plt.ylim(-2000, 2000)
    plt.hlines(
        0,
        t_domain[0],
        t_domain[-1],
        colors="orange",
        linestyles="--",
        label=f"{refFreq}hz",
        data=None,
    )
    plt.xlabel(f"Time ({timeUnit})")
    plt.ylabel(f"Frequency Deviation (in mHz) from {refFreq}Hz")
    plt.title(
        f"""Time vs Frequency-deviation
    Time span: {dataSpanString}
    Data length: {len(f_data)} """,
        loc="left",
    )
    plt.legend()

    # saving figure
    tvsf_imageFileName = f't_vs_df__{dataFileName.split(".")[0]}'
    tvsf_imagePath = f"{outputSubDir}/{tvsf_imageFileName}"
    saveImage(tvsf_imagePath)

    # ---------- MFDFA ------------------

    # Sample code
    # lag = np.unique(np.logspace(0.5, 3, 100).astype(int))
    # q_list = np.linspace(-10,10,41)
    # q_list = q_list[q_list!=0.0]
    # lag, dfa, dfa_std = MFDFA(X, lag, q = q, order = 1, stat = True, extensions = {"eDFA": True})

    lag = np.unique(np.logspace(0.5, 30, 100).astype(int))
    orders = np.linspace(0, 10, 5).astype(int)
    q_list = np.linspace(-10, 10, 41)
    q_list = q_list[q_list != 0.0]

    ordCount = 0
    for order in orders:
        ordCount += 1
        qCount = 0
        for q in q_list:
            qCount += 1

            # Show status
            print(
                f"""
            Processing ... ...
                file: {fileCount}/{len(dataFileNames)},
                order: {ordCount}/{len(orders)},
                order: {qCount}/{len(q_list)},
            """
            )

            # Extract lags and dfa's
            lag, dfa = MFDFA(f_data, lag=lag, q=q, order=order)

            # save as numpy files
            currentFileNameWithoutExtension = dataFileName.split(".")[0]
            np.save(
                f"{outputSubDir}/lag_{currentFileNameWithoutExtension}__q_{q}__ord_{order}",
                lag,
            )
            np.save(
                f"{outputSubDir}/dfa_{currentFileNameWithoutExtension}__q_{q}__ord_{order}",
                dfa,
            )

            # Plot lag vs fluction functions
            plt.loglog(lag, dfa, "-", label=f"q={q:.2f}, ord={order}")

        plt.legend()
        plt.xlabel("lag s")
        plt.ylabel(f"$F_q(s)$")
        plt.title(
            f"""$F_q(s)$__order_{order}
        data length = {len(f_data)}"""
        )

        filename = f"F_q(s)__order_{order}__q_many"
        PLOT_DIR_PATH = outputSubDir
        imageFileName = f"{PLOT_DIR_PATH}/{filename}.png"

        saveImage(imageFileName)

OUTRO = f"""
    -----------------
    Process finished!
    Thank you!
    -----------------
"""
print(OUTRO)
