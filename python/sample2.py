# -*- coding: utf-8 -*-

from time import time
import numpy as np
from copy import deepcopy

start = time()
a = np.arange(25).reshape(5, 5)
b = deepcopy(a) * 2

print(np.einsum("ii", a))
print(np.einsum("ii->i", a))
print(np.einsum("ij->i", a))
print(np.einsum("ij->j", a))
print(np.einsum("ij->ji", a))

print(np.einsum("ij,jk->ik", a, b))
print(np.einsum("ij,jk->ki", a, b))
print(np.einsum("ij,ij->ij", a, b))

print(time() - start)
