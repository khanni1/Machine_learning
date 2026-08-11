def yicap(a:list,x:list,i,n):
    sumx = 0
    for j in range(0,n):
        sumx = sumx + (a[j] * x[j][i])
        
    return sumx
        


def GD(x:list,y:list,a:list,al,max_iter):
    m = len(x[0]) #number of records i 0->m
    
    n = len(x) #number of features j 0->n
    
    temp = a.copy()
    
    for h in range(0,max_iter):

        a = temp.copy()
        
        for j in range (0,n):
            step = 0
            
            for i in range(0,m):
                step = step + ((y[i] - yicap(a,x,i,n)) * x[j][i])
        
            temp[j] = a[j] + (al/m)*step
            
    
    return a


import khanjan_matfunc as k

x = [
    [1,1,1,1,1], # x0
    [8,11,9,6,6], # x1
    [12,6,6,3,18], # x2
]

if(not k.isnt_jagged(x)):
    print("x not a mat error")

y = [0.6,1.2,1.0,0.7,0.3]

a = [1,1,1] #ini for each x feature here x0,x1,x2

    
print(GD(x,y,a,0.01,99999))
# [0.10365079365081545, 0.11507936507936298, -0.029365079365079844]
# rounded
# [0.1037, 0.1151, -0.0294]
    

