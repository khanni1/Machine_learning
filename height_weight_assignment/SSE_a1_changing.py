import matplotlib.pyplot as plt
import numpy as np
import khanjan_matfunc as k


x=[152,175,164,165,166,164,150,158,170,167,177.8,160,185.9,158,161,150,170,160,156,152.4,157,172,160,160,175,188,167,157.5,157,188,177,180,151,183,165.1,167,167.6,162,181,152,161,157.5,160,160,161.5,166,180,151,175,180] 
y=[60,65,45,65,48,43,40,47,55,60,79,65,53,42,48,49,55,52,46,55,70,50,65,42,77,48,61,42,40,71,61,90,42,52,59,52,40,57,70,42,90,55,55,51,60,55,57,52,65,63]


def J(a0,a1,m,x:list,y:list):
    
    sum = 0
    
    for i in range(0,m,1):
        temp = a0 + a1*x[i]
        ei = y[i] - temp
        sum = ei**2 + sum
        
    return sum/(2*m)




incr = 0.1
l1 = []
l2 = []

# found values in scatter.py
a0 = -22.72372
a1 = 0.47603


#  a1 is constant
for i in np.arange(-1.5,2.5+incr,incr):
    l2.append(J(a0,i,50,x,y))
    l1.append(i)

plt.plot(l1,l2,marker='o')
plt.title("J(a0,a1) VS a0")
plt.xlabel("a1")
plt.ylabel("J(a0,a1)")
plt.grid(True)
plt.show()    
    
    
    