# -*- coding:utf-8 -*-

import numpy as np
import functools
import timeit

def benchmark(dim1=30, dim2=20):
  A = np.random.randn(dim1, dim2)
  B = np.random.randn(dim1, dim2)
  C = np.random.randn(dim1, dim2)
  D = np.random.randn(dim1, dim2)
  E = np.random.randn(dim1, dim2)
  return np.einsum("ra,rb,rc,rd,re->abcde", A, B, C, D, E)


with open("../time_python.csv", "w") as f:
  for n in range(5, 40):
    t = timeit.Timer(functools.partial(benchmark, 30, n)).timeit(number=1)
    f.write("{},{}\n".format(n, t))
