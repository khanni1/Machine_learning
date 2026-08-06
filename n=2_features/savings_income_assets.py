import khanjan_matfunc as k

# AX = B
# X = A^-1

A = [
    [5,40,45],
    [40,338,342],
    [45,342,545],
]

B = [
    [3.8],
    [33],
    [27.9],
]

temp = k.mat_inverse(A)

temp2 = k.mat_mul(temp,B)

k.pretty_print_2D(temp2)