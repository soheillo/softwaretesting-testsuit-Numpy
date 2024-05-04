import numpy as np
x=np.array(dir (np))
print("write a number from 1 to " , len (x),":", "\n")
f=input()
print('\n')
h=int(f)
n=x[h]
print ('the ', h,"th array in numpy fuctions array is:" ,n,'\n')

def tenarray():
        print ("enter a number from 1 to ",len(x)," with the aim of printing the list of numpy fuctions equal to this number:" )
        l=input() 
        for i in range(int(l)):
           print( x[i])

tenarray()
    
    

