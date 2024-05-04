def max2():
    
    x=[10,1,2,3,15,20,4,7,9,25,14,28]
    max1=x[0]
    
    for i in range(1,12):
        if x[i] > max1 :
            max1 = x[i]
    return max1

def min2():

    x=[10,1,2,3,15,20,4,7,9,25,14,28]
    min1=x[0]
    
    for j in range(1,12):
        if x[j] < min1 :
            min1 = x[j]
    return min1


print ("maximum number is equal to: ",'\n',max2(),'\n',"minimum number is equal to: ",'\n', min2())            
 
