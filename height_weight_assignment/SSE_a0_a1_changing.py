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




incr_i = 1
incr_j = 0.01

l1 = []
l2 = []
l3 = []

# found values in scatter.py
a0 = -22.72372
a1 = 0.47603


for i in np.arange(-80,40+incr_i,incr_i):
    for j in np.arange(-0.2,1.2+incr_j,incr_j):
        l1.append(i)
        l2.append(j)
        l3.append(J(i,j,50,x,y))
        

        
plt.figure(figsize=(8, 6))

# A standard contour plot with 25 automatically spaced levels
contours = plt.tricontour(l1, l2, l3, levels=25, cmap="viridis")

# Add the standard labels
plt.clabel(contours, inline=True, fontsize=8)

# Mark the center
plt.plot(-22.72, 0.47, 'rx', markersize=8, markeredgewidth=2, label="Global Minimum")

plt.xlabel("a0 (Intercept)")
plt.ylabel("a1 (Slope)")
plt.title("Standard Contour Plot of Cost Function")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()