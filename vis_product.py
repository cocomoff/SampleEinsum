# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X1 = np.loadtxt("./time_python_product.csv", delimiter=",")
X2 = np.loadtxt("./time_julia_product.csv", delimiter=",")

plt.figure(figsize=(6, 3))
plt.plot(X1[1:, 0], X1[1:, 1], "ro--", label="product buildin @ python")
plt.plot(X1[1:, 0], X1[1:, 2], "g^-", label="product einsum @ python")
plt.plot(X1[1:, 0], X2[:, 1], "mv-.", label="product buildin @ julia")
plt.plot(X1[1:, 0], X2[:, 2], "cs-", label="product einsum @ julia")
plt.legend()
plt.tight_layout()
plt.show(block=True)
# plt.savefig("compare.png", dpi=300)
