import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MFDFA import MFDFA

DATA_PATH = "./sample_data/sample.csv"
# DATA_PATH = "./sample_data/UK01a_100ms.csv"

df = pd.read_csv(DATA_PATH, delimiter=";")
f_data = df["f50_UK01a"].to_numpy()
t_domain = np.arange(0, len(f_data))
# print(domain)

# plt.plot(t_domain, f_data)
# plt.show()

# lag = np.unique(np.logspace(0.5, 3, 100).astype(int))
# q_list = np.linspace(-10,10,41)
# q_list = q_list[q_list!=0.0]
# lag, dfa, dfa_std = MFDFA(X, lag, q = q, order = 1, stat = True, extensions = {"eDFA": True})

# lag = np.array([5,6,7,8,9,10])
# q_list = [2, 3, 4]
lag = np.unique(np.logspace(0.5, 3, 1000).astype(int))
# q_list = np.linspace(-10,10,3)
# orders = np.linspace(0,10,5).astype(int)
q_list = np.array([2])
q_list = q_list[q_list != 0.0]
orders = [0, 1, 2, 3, 6, 7, 10]
for order in orders:
    for q in q_list:
        lag, dfa = MFDFA(f_data, lag=lag, q=q, order=order)
        plt.loglog(lag, dfa, "-", label=f"q={q}, order={order}")

plt.legend()
plt.xlabel("lag s")
plt.ylabel(f"$F_{q}(s)$")
plt.title(f'''$F_{q}(s)$ with different order(degree) of polynomial fitting
data length = {len(f_data)}''')
# plt.show()

PLOT_DIR_PATH = './images'
filename = f'q_{q}__order_many'
imageFileName=f'{PLOT_DIR_PATH}/{filename}.png'
plt.savefig(
    imageFileName, 
    facecolor = 'w', 
    edgecolor = 'w',
    orientation = 'portrait',
    format=None,
    dpi=300,
    transparent = False,
    bbox_inches = None, 
    pad_inches = 0.1,
    metadata = None
)
# plt.clf()