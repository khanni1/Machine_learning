# normal python list of lists best for from sratch matrices else numpy matrices provide their built in functions

def is_square_mat(A):
    for i in range(0,len(A),1):
        if(len(A) != len(A[i])):
            return False
        
    return True

def Minor(A,x,y):
    x = x-1
    y = y-1
    # -1 for compensation math index start from 1 while list starts with 0 thats it 
    T = []
    
    for i in range (0,len(A),1):
        t = []
        if(x == i):
            continue
        for j in range (0,len(A[0]),1):
            if(y == j):
                continue
            else:
                t.append(A[i][j])
                
        T.append(t)
        
    return T
                
                
                
        

X = [
    [1,2,4],
    [5,6,6],
    [5,6,8],
    ]

print(Minor(X,1,3))