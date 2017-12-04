# -*- coding: utf-8 -*-

import numpy as np

a = np.random.normal(size=5*2).reshape((5, 2))
b = np.random.normal(size=6*2).reshape((6, 2))
c = np.random.normal(size=7*2).reshape((7, 2))
ABC = np.einsum("ij,kj,lj->ikl", a, b, c)
print(ABC.shape)
