# normal python list of lists best for from sratch matrices else numpy matrices provide their built in functions

def scalar_mul(A:list,s):
    
    rows = len(A)
    cols = len(A[0])
    
    temp = mat_create_ini(rows,cols)
    
    for i in range(0,rows):
        for j in range(0,cols):
            temp[i][j] = round(A[i][j] * s,5)
            
    return temp
# ==============================================================

def pretty_print_2D(A:list,rounder=5):
    if not A:
        print("error")
        return False
        
    for lst in A:
        lst = list(map(lambda x: round(x,rounder),lst))
        print(lst)  
            

# ==============================================================

def mat_create_ini(rows,cols):
    temp = []
    
    for i in range(0,rows,1):
        row = []
        for j in range(0,cols,1):
            row.append(0)
        temp.append(row)
    
    return temp
# ==============================================================
def is_square_mat(A:list):
    
    # jagged checked if not jagged means all rows have same length
    if (not isnt_jagged(A)):
        return False
    
    # if no. of rows != no. of cols (ie is elements in any one of non - jagged row so taken 0th row for simplicity)
    if(len(A) != len(A[0])):
        return False
        
    return True
# ==============================================================

def isnt_jagged(A:list):
    x = len(A[0])
    for i in range(1,len(A),1):
        if(x != len(A[i])):
            return False
        # returns true if not jagged
    return True
        
# ==============================================================

def Minor(A:list,x,y):
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
       
def det(A:list):
    if(not is_square_mat(A)):
        return False,"Not a square matrix"
    
    rows = len(A)
    
    if(rows == 1):
    # if 1x1 mat
        return A[0][0] 

    if(rows == 2):
        # if 2x2 mat
       return A[0][0]*A[1][1] - A[0][1]*A[1][0]
        
    
    i = 0 
    sum = 0
    for j in range (0,rows,1):
        if((i+j)%2==1):
            sign = -1
        else:
            sign = 1
        sum = sum + (A[i][j] * det(Minor(A,i,j)) * sign)
        
    return sum
        
# ==============================================================
                
def mat_mul(A:list,B:list):
    if(not isnt_jagged(A) or not isnt_jagged(B) or len(A[0]) != len(B)):
        return False,"conditions not suitable for mutiplication"
    
    Arows = len(A)
    Acols = len(A[0])
    
    Brows = len(B)
    Bcols = len(B[0])
    
    
    pro = mat_create_ini(Arows,Bcols) # mxn . nxp = mxp matrix
    
    for i in range(0,Arows,1):
        for k in range(0,Bcols,1):
            sum = 0
            for j in range(0,Acols):
                sum = sum + A[i][j] * B[j][k]
            pro[i][k] = sum
            

    return pro
            
            
            
    
# ==============================================================

def transpose(A:list):
    
    if(not isnt_jagged(A)):
        return False
    
    rows = len(A)
    cols = len(A[0])
    
    t_mat = mat_create_ini(cols,rows)
     #temp variable initialised with 0s

    for i in range(0,rows,1):
        for j in range(0,cols,1):
            t_mat[j][i] = A[i][j]

    return t_mat
          
# ==============================================================

def adjoint(A:list):
    if(not is_square_mat(A)):
        return False
    
    rows = len(A)
    cols = len(A[0])
    cofacmat = mat_create_ini(rows,cols)
    
    for i in range(0,rows):
        for j in range(0,cols):
            sign = 1
            if ((i+j) % 2 == 1):
                sign = -1
                
            cofacmat[i][j] = det(Minor(A,i,j)) * sign
            
    return transpose(cofacmat)

def mat_inverse(A:list):
    x = det(A)
    adj = adjoint(A)
    if(x==0 or not adj):
        return False
    
    return scalar_mul(adj,1.0/x)
# ==============================================================
# main area for testing

