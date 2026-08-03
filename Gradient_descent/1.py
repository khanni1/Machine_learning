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
        
        print(f"{iter:<6} | {temp:<12.5f} | {df(temp) :<12.5f} | {step_size :<12.5f} | {x :<12.5f} | {f(x) :<12.5f}")
        
        xlst.append(iter)
        ylst.append(f(x))
        
    return xlst,ylst

def GD_fixed_iter(x,a,iters):
    
    xlst = [] # no of iterations
    ylst = [] # cost function
    
    # ini large value just for entering the loop
    step_size = 100 
    iter = 0
    
    print(f"{'Iter':<6} | {'x':<12} | {'df(x)':<12} | {'a*df(x)':<12} | {'x_new':<12} | {'f(x)':<12} |")
    print("-" * 70)
    
    for i in range(0,iters,1):
        
        step_size = a*df(x)
        
        # just storing x's value before changing it further
        temp = x 
        
        x = x - step_size
        
        iter = iter + 1
        
        print(f"{iter:<6} | {temp:<12.5f} | {df(temp) :<12.5f} | {step_size :<12.5f} | {x :<12.5f} | {f(x) :<12.5f}")
        
        xlst.append(iter)
        ylst.append(f(x))
        
    return xlst,ylst

        
# called the function
iters = 50
a0 = 0.05
a1 = 0.07
a2 = 0.1
a3 = 0.2
a4 = 0.3
a5 = 0.99

x,y = GD_fixed_iter(0,0.05,iters)
x1,y1 = GD_fixed_iter(0,0.07,iters)
x2,y2 = GD_fixed_iter(0,0.1,iters)
x3,y3 = GD_fixed_iter(0,0.2,iters)
x4,y4 = GD_fixed_iter(0,0.3,iters)

x5,y5 = GD_fixed_iter(0,0.99,100)



# plotting
plt.plot(x,y,marker='o',label = f"a = {a0}")
plt.plot(x1,y1,marker='o',label = f"a = {a1}")
plt.plot(x2,y2,marker='o',label = f"a = {a2}")
plt.plot(x3,y3,marker='o',label = f"a = {a3}")
plt.plot(x4,y4,marker='o',label = f"a = {a4}")
plt.plot(x5,y5,marker='o',label = f"a = {a5}")


plt.legend()

plt.title("iteration vs cost function")
plt.xlabel("iteration number")
plt.ylabel("cost function value at that iteration")
plt.grid(True)

plt.show()



        