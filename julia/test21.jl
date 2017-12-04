# -*- coding: utf-8 -*-

using Einsum

time_num = []
d = 200
iteration = 1000

for N=1:d
    a = ones(N, N)
    b = ones(N, N)

    tic()
    for _i = 1:iteration
        dot(a, b)
    end
    push!(time_num, toq())
end

open("../time_julia_product_dot.csv", "w") do f
    for N=1:d
        write(f, "$N,$(time_num[N])\n")
    end
end
