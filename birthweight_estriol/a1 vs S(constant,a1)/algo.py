# matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np

def S(a1):
    
    # no of observations
    m=5 
    
    x = [1,2,3,4,5]
    y = [1,1,2,2,4]
    sum = 0
    
    for i in range(0,m,1):
        temp = (-0.1) + a1*x[i]
        temp1 = y[i] - temp
        sum = temp1**2 + sum
        
    return a1,round(sum,5)

# lets take range from -0.9 to 1.1 (original_minima) to 3.1

xcord = []
ycord = []

for i in range(-13,28,1):
    ansx,ansy  = S(i/10)
    xcord.append(ansx)
    ycord.append(ansy)
    
    
# numpy used here
x1 = np.array(xcord)
y1 = np.array(ycord)

# matplotlib usedd from here
plt.plot(x1,y1,marker='o')
plt.grid(True)
plt.show()
    


