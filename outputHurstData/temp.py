import numpy as np
import matplotlib.pyplot as plt

h = np.load('./h__output_DE_OL01_100ms__ord_1.npy')
q = np.load('./q__output_DE_OL01_100ms__ord_1.npy')

plt.plot(q,h, 'o')
plt.show()