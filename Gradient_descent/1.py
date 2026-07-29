# holds main function
def f(x):
   return (x**2 - 4*x + 8)

# derivative if f(x) written here
def df(x):
    return (2*x - 4)

# GD
def GD(x,a,e):
    
    # ini large value just for entering the loop
    step_size = 100 
    iter = 0
    
    print(f"{'Iter':<6} | {'x':<12} | {'df(x)':<12} | {'a*df(x)':<12} | {'x_new':<12} | {'f(x)':<12} |")
    print("-" * 70)
    
    while (abs(step_size) >= e):
        
        step_size = a*df(x)
        
        # just storing x's value before changing it further
        temp = x 
        
        x = x - step_size
        
        iter = iter + 1
        
        print(f"{iter:<6} | {temp:<12.5f} | {df(x) :<12.5f} | {step_size :<12.5f} | {x :<12.5f} | {f(x) :<12.5f}")
        
        
GD(0,0.1,0.01)
        