# a0 and a1, 2 features !

def SSE(a0,a1,m,xdata:list,ydata:list):
    
    sum = 0
    
    for i in range(0,m,1):
        temp = a0 + a1*xdata[i]
        temp1 = ydata[i] - temp
        sum = temp1**2 + sum
    
        
    return sum

def MSSE(a0,a1,m,xdata:list,ydata:list):

    ans = SSE(a0,a1,m,xdata,ydata)/(2*m)
    
    return ans

def df(x):
    return

def GD(x,x1,a,e):

    # ini large value just for entering the loop
    step_size = 100 
    iter = 0
    
    # print(f"{'Iter':<6} | {'x':<12} | {'df(x)':<12} | {'a*df(x)':<12} | {'x_new':<12} | {'f(x)':<12} |")
    print("-" * 70)
    
    # iter <= 100 for force stop
    
    while (abs(step_size) >= e and iter <= 21):
        
        step_size = a*df(x)
        
        # just storing x's value before changing it further
        temp = x 
        
        x = x - step_size
        
        iter = iter + 1
        
        # print(f"{iter:<6} | {temp:<12.5f} | {df(x) :<12.5f} | {step_size :<12.5f} | {x :<12.5f} | {f(x) :<12.5f}")
        
  
x = [4.37, 9.56, 7.59, 6.39, 2.4, 2.4, 1.52, 8.8, 6.41, 7.37, 1.19, 9.73, 8.49, 2.91, 2.64, 2.65, 3.74, 5.72, 4.89, 3.62, 6.51, 2.26, 3.63, 4.3, 5.1]
x1 = [41.41, 17.99, 30.57, 33.7, 11.86, 34.3, 16.82, 12.6, 47.96, 48.63, 42.34, 22.18, 13.91, 37.37, 27.61, 14.88, 29.81, 11.38, 46.37, 20.35, 36.5, 22.47, 30.8, 31.87, 17.39]
y  = [50.16, 43.55, 48.26, 47.48, 18.27, 37.36, 21.57, 38.67, 59.91, 59.68, 42.33, 46.49, 36.34, 43.09, 35.23, 24.93, 36.94, 27.94, 54.82, 31.79, 49.76, 28.35, 37.06, 39.45, 32.88]
