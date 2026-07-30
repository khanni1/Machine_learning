import matplotlib.pyplot as plt
import numpy as np

# holds main function
def f(x):
   return (x**2 - 4*x + 8)

# derivative if f(x) written here
def df(x):
    return (2*x - 4)

# GD
def GD(x,a,e):
    
    xlst = [] # no of iterations
    ylst = [] # cost function
    
    # ini large value just for entering the loop
    step_size = 100 
    iter = 0
    
    print(f"{'Iter':<6} | {'x':<12} | {'df(x)':<12} | {'a*df(x)':<12} | {'x_new':<12} | {'f(x)':<12} |")
    print("-" * 70)
    
    # iter <= 100 for force stop
    
    while (abs(step_size) >= e and iter <= 21):
        
        step_size = a*df(x)
        
        # just storing x's value before changing it further
        temp = x 
        
        x = x - step_size
        
        iter = iter + 1
        
        print(f"{iter:<6} | {temp:<12.5f} | {df(x) :<12.5f} | {step_size :<12.5f} | {x :<12.5f} | {f(x) :<12.5f}")
        
        xlst.append(iter)
        ylst.append(f(x))
        
    return xlst,ylst
        
# called the function
x,y = GD(0,0.1,0.01)
x1,y1 = GD(0,0.2,0.01)
x2,y2 = GD(0,0.3,0.01)
x3,y3 = GD(0,0.4,0.01)
x4,y4 = GD(0,0.5,0.01)

x5,y5 = GD(0,0.99,0.01)



# plotting
plt.plot(x,y,marker='o',label = "a = 0.1")
plt.plot(x1,y1,marker='o',label = "a = 0.2")
plt.plot(x2,y2,marker='o',label = "a = 0.3")
plt.plot(x3,y3,marker='o',label = "a = 0.4")
plt.plot(x4,y4,marker='o',label = "a = 0.5")
plt.plot(x5,y5,marker='o',label = "a = large")


plt.legend()

plt.title("iteration vs cost function")
plt.xlabel("iteration number")
plt.ylabel("cost function value at that iteration")
plt.grid(True)

plt.show()



        