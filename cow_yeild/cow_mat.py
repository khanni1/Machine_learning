import khanjan_matfunc as k

# x = [4,6,10,12]
# `mat_mul` works with list-of-lists matrices.  Keep the target values as a
# 1 x 4 row matrix so it can be multiplied by `a2`.
y = [[3,5.5,6.5,9]]

X = [[1,1,1,1],
     [4,6,10,12]]

a1 = k.mat_inverse(k.mat_mul(X,k.transpose(X)))

a2 = k.mat_mul(k.transpose(X),a1)

a3 = k.mat_mul(y,a2)

k.pretty_print_2D(a3,4)
# gives the correct output for a0 = 0.8 and a1 = 0.65

