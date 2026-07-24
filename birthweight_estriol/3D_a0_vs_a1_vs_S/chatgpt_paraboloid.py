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

for i in np.arange(-10, 10.1, 0.1):
    # clean for next loop
    x_row = []
    y_row = []
    z_row = []
    for j in np.arange(-10, 10.1, 0.1):
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

plt.figure()

# plt.contourf(x, y, z, levels=20)
levels = np.linspace(1.1, 50, 20)
plt.contourf(x, y, z, levels=levels)
plt.colorbar()
plt.xlabel("a0")
plt.ylabel("a1")
plt.title("SSE Contours")

plt.axis("equal")
plt.show()

r, c = np.unravel_index(np.argmin(z), z.shape)

print("Minimum SSE =", z[r, c])
print("a0 =", x[r, c])
print("a1 =", y[r, c])



plt.show()         