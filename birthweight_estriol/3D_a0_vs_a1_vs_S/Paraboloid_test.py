import matplotlib.pyplot as plt
import numpy as np

def paraboloid(x,y):
    z = (x**2 + y**2)
    return x,y,z
    
# empty ini 2D array
x_data = []
y_data = []
z_data = []

min = -50
max = 50


for i in range(min,max+1):
    # empty ini for each outer loop iteration
    # these are subarrays
    x_row = []
    y_row = []
    z_row = []
    
    for j in range(min,max+1):
        x,y,z = paraboloid(i,j)
        
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
f1.set_box_aspect((1, 1, 1.5)) 
# set_box_aspect just scales according to factor like z is scaled 1.9 comapred to x and y
plt.show()