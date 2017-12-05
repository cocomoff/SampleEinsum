# -*- coding: utf-8 -*-

import numpy as np

eijk = np.zeros((3, 3, 3))
eijk[0, 1, 2] = eijk[1, 2, 0] = eijk[2, 0, 1] = 1
eijk[0, 2, 1] = eijk[1, 0, 2] = eijk[2, 1, 0] = -1


A = np.random.rand(3, 3)
inv_numpy1 = np.linalg.inv(A)
inv_numpy2 = np.linalg.solve(A, np.identity(3))
det_einsum = np.einsum("ijk,i,j,k", eijk, A[0], A[1], A[2])
inv_einsum = np.einsum("ijk,pqr,qj,rk->ip", eijk, eijk, A, A) / (2.0 * det_einsum)

print(inv_numpy1)
print(inv_numpy2)
print(inv_einsum)
