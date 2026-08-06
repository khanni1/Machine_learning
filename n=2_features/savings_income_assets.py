import khanjan_matfunc as k

# K = (X'X)^-1 X' Y
# here i wrote X and Y in row vector form
# but for the formula i need col vector form so i will just replace X with X' and Y with Y' everywhere in formula

x = [
    [1,1,1,1,1],
    [8,11,9,6,6],
    [12,6,6,3,18],
]

y = [
    [0.6,1.2,1,0.7,0.3]
]

x = k.transpose(x)
y = k.transpose(y)

# now apply formula as it is

t1 = k.mat_inverse(k.mat_mul(k.transpose(x),x))

t1 = k.mat_mul(k.mat_mul(t1,k.transpose(x)),y)

k.pretty_print_2D(t1)


# WORKS PERFECTLY


