# -*- coding: utf-8 -*-
# reference:
# - code 5 @ http://www.procrasist.com/entry/einsum
#

import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

time_num = []
d = 201
iteration = 1000
for N in range(d):
    a = np.ones((N, N))
    b = np.ones((N, N))
    np_start = time.time()
    for _ in range(iteration):
        np.dot(a,b)
    time_num.append(time.time()-np_start)

with open("../time_python_product_np.csv", "w") as f:
  for N in range(d):
    f.write("{},{}\n".format(N, time_num[N]))
