import numpy as np
x=np.array(dir (np))
print("write a number from 1 to " , len (x),":", "\n")
f=input()
print('\n')
h=int(f)
n=x[h]
print ('the ', h,"th array in numpy members array is:" ,n,'\n')

def tenmembers():
        print ("enter a number from 1 to ",len(x)," with the aim of printing the list of numpy members equal to this number:" )
        l=input() 
        for i in range(int(l)):
           print( x[i])
def tenfunctions():
        numpy_functions = [member for member in x if callable(getattr(np, member))]
        print('\n\n',"the Number of Functions in NumPy:", len(numpy_functions))


tenmembers()
tenfunctions()

    
    

