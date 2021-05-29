import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MFDFA import MFDFA

DATA_PATH = "./sample_data/sample.csv"
# DATA_PATH = "./sample_data/UK01a_100ms.csv"
PLOT_DIR_PATH = './images'

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
lag = np.unique(np.logspace(0.5, 30, 100).astype(int))
# orders = np.linspace(0,10,5).astype(int)
q_list = np.linspace(0,10,5)
q_list = q_list[q_list != 0.0]
orders = [0,1,2,3,4,5]
for order in orders:
    for q in q_list:
        lag, dfa = MFDFA(f_data, lag=lag, q=q, order=order)
        plt.loglog(lag, dfa, "-", label=f"q={q:.2f}, ord={order}")

    plt.legend()
    plt.xlabel("lag s")
    plt.ylabel(f"$F_q(s)$")
    plt.title(f'''$F_q(s)$__order_{order}
    data length = {len(f_data)}''')
    # plt.show()

    filename = f'F_q(s)__order_{order}__q_many'
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
    plt.clf()