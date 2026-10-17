def distance(a:list,b:list,n,p=2):
    # n dimensionals points an
    summ = 0
    for i in range(0,n):
        summ = summ + abs(a[i] - b[i])**p
        
    return summ**(1/p)