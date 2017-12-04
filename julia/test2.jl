# -*- coding: utf-8 -*-

using Einsum

time_num = []
time_ein = []
d = 20
iteration = 1000

for N=1:d
    a = ones(N, N)
    b = ones(N, N)

    tic()
    for _i = 1:iteration
        dot(a, b)
    end
    push!(time_num, toq())

    tic()
    Aik = zeros(N, N)
    for _i = 1:iteration
        @einsum Aik[i, k] = a[i, j] * b[j, k]
    end
    push!(time_ein, toq())
end

open("../time_julia_product.csv", "w") do f
    for N=1:d
        write(f, "$N,$(time_num[N]),$(time_ein[N])\n")
    end
end
