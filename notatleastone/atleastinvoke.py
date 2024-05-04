import numpy as np
import numpy.testing as npt
import trace
import inspect
import sys
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

# Define a function to trace function calls during test suite execution
def trace_test_functions(test_functions):
    traced_functions = set()
    for test_function in test_functions:
        # Trace function calls within each test function
        tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=0)
        tracer.runfunc(test_function)
        # Get the list of traced functions and update the set
        traced_functions.update(tracer.results().calledfuncs)
    return traced_functions

# List all functions in NumPy
numpy_functions = set(name for name, _ in inspect.getmembers(np, inspect.isfunction))

# Define your test functions
test_functions = [test_addition, test_multiplication]

# Trace function calls during test suite execution
traced_functions = trace_test_functions(test_functions)

# Determine functions in NumPy not invoked directly during testing
unused_functions = numpy_functions - traced_functions

# Print unused functions
print("Functions in NumPy not directly invoked by at least one test case during test suite execution:")
for func in unused_functions:
    print(func)
