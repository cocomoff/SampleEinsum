# -*- coding: utf-8 -*-

using Einsum

tic()
a = transpose(reshape(0:24, (5, 5)))
b = copy(a) * 2

A = Array{Int64}(size(a)[1])
@einsimd A[i] = a[i, i]
println(A)

@einsimd A[i] = a[i, j]
println(A)

@einsimd A[j] = a[i, j]
println(A)

AA = Array{Int64}(size(a))
@einsimd AA[i, j] = a[j, i]
println(AA)

AB = Array{Int64}(size(a))
@einsimd AB[i, k] = a[i, j] * b[j, k]
println(AB)

@einsimd AB[k, i] = a[i, j] * b[j, k]
println(AB)

@einsimd AB[i, j] = a[i, j] * b[i, j]
println(AB)

println(toq())
