def S(a0):
    
    # no of observations
    m=5 
    
    x = [1,2,3,4,5]
    y = [1,1,2,2,4]
    sum = 0
    
    for i in range(0,m,1):
        temp = a0 + 0.7*x[i]
        temp1 = y[i] - temp
        sum = temp1**2 + sum
        
    return a0,round(sum,5)

for i in range(10,-30,-1):
    ansx,ansy  = S(i/100)
    print(ansx,',',ansy)
    


