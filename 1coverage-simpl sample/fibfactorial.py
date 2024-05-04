def fibonacci (n):
     if n<0:
         print ('invalid number')
     elif n<=1:
         return n
     else:
         return fibonacci(n-1)+ fibonacci(n-2)
     
def factorial (n):
     if n==0:
          return 1
     else:
          return n*factorial(n-1) 
        
print (fibonacci(-1))
print (factorial (5))


    
