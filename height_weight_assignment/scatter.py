import matplotlib.pyplot as plt
import numpy as np

from functools import reduce

import khanjan_matfunc as k


x=[152,175,164,165,166,164,150,158,170,167,177.8,160,185.9,158,161,150,170,160,156,152.4,157,172,160,160,175,188,167,157.5,157,188,177,180,151,183,165.1,167,167.6,162,181,152,161,157.5,160,160,161.5,166,180,151,175,180] 
y=[60,65,45,65,48,43,40,47,55,60,79,65,53,42,48,49,55,52,46,55,70,50,65,42,77,48,61,42,40,71,61,90,42,52,59,52,40,57,70,42,90,55,55,51,60,55,57,52,65,63]

yc = []

m = len(x)

sum_xi = reduce(lambda a,b : a+b,x)

sum_yi = reduce(lambda a,b : a+b,y)

sum_xi_sq = reduce(lambda a,b : a+b,list(map(lambda z:z**2,x)))

sum_xi_yi = 0

for i in range(0,len(x)):
    sum_xi_yi = sum_xi_yi + x[i]*y[i]


# X = A^-1 . B

A = [
    [m,sum_xi],
    [sum_xi,sum_xi_sq]
]

B = [
    [sum_yi],
    [sum_xi_yi]
]

C= k.mat_mul(k.mat_inverse(A),B)

k.pretty_print_2D(C)

a0 = C[0][0]

a1 = C[1][0]

yc = []



# print(len(x),len(y))

# print(sum_xi)
# print(sum_yi)
# print(sum_xi_sq)
# print(sum_xi_yi)






# to plot need to calculate many values of y from x OR just use set of x values to calculate corresponding y values

for i in range(0,len(x),1):
    yc.append(a0+a1*x[i])  
    
    

plt.scatter(x,y,marker='o',label="x vs y")
plt.plot(x,yc,label="regression line")
plt.xlabel("height")
plt.ylabel("weight")
plt.legend()
plt.grid(True)
plt.title("height vs weight")
plt.show()
