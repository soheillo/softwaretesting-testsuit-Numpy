import numpy as np
import numpy.testing as npt
import inspect

# List all functions in NumPy
numpy_functions = inspect.getmembers(np, inspect.isfunction)

# Define a list to store functions invoked during testing
invoked_functions = set()

# Define your test functions
def test_addition():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = np.add(a, b)
    expected = np.array([5, 7, 9])
    npt.assert_array_equal(result, expected)

def test_multiplication():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    result = np.dot(a, b)
    expected = np.array([[19, 22], [43, 50]])
    npt.assert_array_equal(result, expected)

# Iterate through test functions and record invoked functions
test_functions = [test_addition, test_multiplication]
for test_function in test_functions:
    invoked_functions.update(inspect.getclosurevars(test_function).globals.keys())

# Determine functions not invoked during testing
unused_functions = [func for func, _ in numpy_functions if func not in invoked_functions]

# Print unused functions
print("Functions in NumPy not invoked during test suite:")
for func in unused_functions:
    print(func)
