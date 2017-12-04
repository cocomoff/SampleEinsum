    using Einsum

A = zeros(5, 6, 7)
X = randn(5, 2)
Y = randn(6, 2)
Z = randn(7, 2)
@einsum A[i, j, k] = X[i, r] * Y[j, r] * Z[k, r]

println(size(A))
