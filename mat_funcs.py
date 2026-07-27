# normal python list of lists best for from sratch matrices else numpy matrices provide their built in functions
def mat_create_ini(rows,cols):
    temp = []
    
    for i in range(0,rows,1):
        row = []
        for j in range(0,cols,1):
            row.append(0)
        temp.append(row)
    
    return temp
# ==============================================================
def is_square_mat(A):
    
    if (not isnt_jagged(A)):
        return False
    
    for i in range(0,len(A),1):
        if(len(A) != len(A[i])):
            return False
        
    return True
# ==============================================================

def isnt_jagged(A):
    x = len(A[0])
    for i in range(1,len(A),1):
        if(x != len(A[i])):
            return False
        # returns true if not jagged
    return True
        
# ==============================================================

def Minor(A,x,y):
    # x = x-1
    # y = y-1
    # -1 for compensation math index start from 1 while list starts with 0 thats it 
    if(not isnt_jagged(A)):
        return False,"jagged matrix error"
    
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
                
# ==============================================================
       
def det(A):
    if(not is_square_mat(A)):
        return False,"Not a square matrix"
    
    if(len(A) == 1):
    # if 1x1 mat
        return A[0][0] 

    if(len(A) == 2):
        # if 2x2 mat
       return A[0][0]*A[1][1] - A[0][1]*A[1][0]
        
    
    i = 0 
    sum = 0
    for j in range (0,len(A),1):
        if((i+j)%2==1):
            sign = -1
        else:
            sign = 1
        sum = sum + (A[i][j] * det(Minor(A,i,j)) * sign)
        
    return sum
        
# ==============================================================
                
def mat_mul(A,B):
    if(not isnt_jagged(A) or not isnt_jagged(B) or len(A[0]) != len(B)):
        return False,"conditions not suitable for mutiplication"
    
# ==============================================================

def tranpose(A):
    
    if(not isnt_jagged(A)):
        return False
    
    t_mat = mat_create_ini(len(A[0]),len(A))
     #temp variable initialised with 0s

    for i in range(0,len(A),1):
        for j in range(0,len(A[i]),1):
            t_mat[j][i] = A[i][j]

    return t_mat
          


X = [
    [1,2,4],
    [5,6,6],
    [5,6,8],
    ]

A1 = [
    [3,2],
    [1,5],
    [3]]

print(tranpose(A1))
