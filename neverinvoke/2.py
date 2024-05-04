import numpy as np

def test_addition():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = np.add(a, b)
    return result
def test_multiplication():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    result = np.dot(a, b)
    return result
 
print (test_addition(),'\n\n',test_multiplication() )
