import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import modules.dataCleaner.dataCleaner as dc

dataFileName = 'UK01a_100ms'
# dataFileName = 'HR01_100ms'
# dataFileName = 'IT-SI01_100ms'
# dataFileName = 'RUS01_100ms'
# dataFileName = 'PL01_100ms'
# dataFileName = 'PT_LI01_100ms'
# dataFileName = 'SE01_100ms'
# Faroe island
# dataFileName = 'DE_OL01_100ms'
# dataFileName = 'US-TX01_100ms'
# dataFileName = 'FO-01_100ms'
# dataFileName = 'UK02b_100ms'
# dataFileName = 'UK02a_100ms'
# dataFileName = 'DE-KA02_100ms'


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

cleaned__UK01a_100ms = dc.clean__UK01a_100ms(t_domain_noScale, f_data)
# cleaned__HR01_100ms = dc.clean__HR01_100ms(t_domain_noScale, f_data)
# cleaned__SI01_100ms = dc.clean__IT_SI01_100ms(t_domain_noScale, f_data)
# cleaned__RUS01_100ms = dc.clean__RUS01_100ms(t_domain_noScale, f_data)
# cleaned__PL01_100ms = dc.clean__PL01_100ms(t_domain_noScale, f_data)
# cleaned__PL01_100ms = dc.clean__PT_LI01_100ms(t_domain_noScale, f_data)
# cleaned__SE01_100ms = dc.clean__SE01_100ms(t_domain_noScale, f_data)
# cleaned__DE_OL01_100ms = dc.clean__DE_OL01_100ms(t_domain_noScale, f_data)
# cleaned__DE_OL01_100ms = dc.clean__US__TX01_100ms(t_domain_noScale, f_data)
# cleaned__FO__01_100ms = dc.clean__FO__01_100ms(t_domain_noScale, f_data)
# cleaned__UK02b_100ms = dc.clean__UK02b_100ms(t_domain_noScale, f_data)
# cleaned__UK02a_100ms = dc.clean__UK02a_100ms(t_domain_noScale, f_data)
# clean__DE__KA02_100ms = dc.clean__DE__KA02_100ms(t_domain_noScale, f_data)
