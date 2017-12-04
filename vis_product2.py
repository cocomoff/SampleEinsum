# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X1 = np.loadtxt("./time_python_product_np.csv", delimiter=",")
X2 = np.loadtxt("./time_julia_product_dot.csv", delimiter=",")

plt.figure(figsize=(4, 3))
plt.plot(X1[1:, 0], X1[1:, 1], "ro--", label="np.dot @ python")
plt.plot(X1[1:, 0], X2[:, 1], "mv-.", label="buildin dot @ julia")
plt.legend()
plt.tight_layout()
plt.show(block=True)
# plt.savefig("compare.png", dpi=300)
