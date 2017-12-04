# -*- coding: utf-8 -*-
# reference:
# - code 5 @ http://www.procrasist.com/entry/einsum
#

import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

time_num = []
time_ein = []
d = 101
iteration = 1000
for N in range(d):
    a = np.ones(N)
    b = np.ones(N)
    np_start = time.time()
    for _ in range(iteration):
        np.dot(a,b)
    time_num.append(time.time()-np_start)
    ein_start = time.time()
    for _ in range(iteration):
        np.einsum("i,i",a,b)
    time_ein.append(time.time()-ein_start)

plt.figure(figsize=(6, 4))
plt.plot(range(d),time_num,label="builtin")
plt.plot(range(d),time_ein,label="einsum")
plt.legend()
plt.xlabel("dimension")
plt.ylabel("time")
plt.xlim(0,100)
plt.savefig("../output/inner.png")
plt.legend()

with open("../time_python_inner.csv", "w") as f:
  for N in range(d):
    f.write("{},{},{}\n".format(N, time_num[N], time_ein[N]))
