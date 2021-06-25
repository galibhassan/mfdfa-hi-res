import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import modules.dataCleaner.dataCleaner as dc

# dataFileName = 'UK01a_100ms'
# dataFileName = 'HR01_100ms'
dataFileName = 'IT-SI01_100ms'

dataPath = f'../../data/{dataFileName}.csv'
df = pd.read_csv(dataPath, delimiter=";")

tColName = df.columns[0]
dataSpanString = f"{df[tColName].iloc[0]} to {df[tColName].iloc[-1]}"
fColName = df.columns[1]
refFreq = int(fColName.split("_")[0].split("f")[1])
f_data = df[fColName].to_numpy()
t_domain = np.arange(0, len(f_data)) * 100 / 1000 / 60 / 60  # in hr
t_domain_noScale = np.arange(0, len(f_data))
timeUnit = "hour"

# cleaned__UK01a_100ms = dc.clean__UK01a_100ms(t_domain_noScale, f_data)
# cleaned__HR01_100ms = dc.clean__HR01_100ms(t_domain_noScale, f_data)
cleaned__SI01_100ms = dc.clean__IT_SI01_100ms(t_domain_noScale, f_data)
