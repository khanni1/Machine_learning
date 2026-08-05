def height_weight(x):
    a0 = -22.72372
    a1 = 0.47603
    
    y = a0 + a1*x
    
    return round(y,4)

while(True):
    height = float(input("Enter height to predict corresponding weight : "))
    print("weight : ",height_weight(height))
    