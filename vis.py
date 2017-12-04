# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X1 = np.loadtxt("./time_python.csv", delimiter=",")
X2 = np.loadtxt("./time_julia.csv", delimiter=",")

plt.figure(figsize=(6, 3))
plt.plot(X1[:,0], X1[:, 1], "ro--", label="np.einsum @ python")
plt.plot(X1[:,0], X2[:, 1], "mv-.", label="Einsum.jl @ julia")
plt.legend()
plt.tight_layout()
# plt.show(block=True)
plt.savefig("compare.png", dpi=300)
