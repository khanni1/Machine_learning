import matplotlib.pyplot as plt
import numpy as np

def S(a0,a1):
    
    # no of observations
    m=5 
    
    x = [1,2,3,4,5]
    y = [1,1,2,2,4]
    sum = 0
    
    for i in range(0,m,1):
        temp = a0 + a1*x[i]
        temp1 = y[i] - temp
        sum = temp1**2 + sum
    
    # sum = a0**2 + a1**2
        
    return a0,a1,sum

x_data = []
y_data = []
z_data = []

# 2d array in array.

for i in np.arange(-2.1, 1.91, 0.01):
    # clean for next loop
    x_row = []
    y_row = []
    z_row = []
    for j in np.arange(-1.3, 2.71, 0.01):
        x, y, z = S(i, j)
        x_row.append(x)
        y_row.append(y)
        z_row.append(z)
    
    x_data.append(x_row)
    y_data.append(y_row)
    z_data.append(z_row)
        
x = np.array(x_data)
y = np.array(y_data)
z = np.array(z_data)

fig = plt.figure()
f1 = fig.add_subplot(projection='3d')

f1.plot_surface(x,y,z,cmap="viridis")


f1.set_xlabel("a0")
f1.set_ylabel("a1")
f1.set_zlabel("S(a0, a1)")
# f1.set_box_aspect((2, 0.2, 1)) 

plt.show()