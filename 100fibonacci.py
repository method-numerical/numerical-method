"""
importing fibonacci to result first 100 fiboacci numbers.
using timeit() function to calculate time needed to complete it.
"""
import fibonacci
import timeit

a=fibonacci.fibonacci(100)

code="""
import fibonacci
a=fibonacci.fibonacci(100)
"""

t=timeit.timeit(code,number=1)
print('time needed in seconds :=',t,'.')
