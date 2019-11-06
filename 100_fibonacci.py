import fibonacci
fibonacci.fibonacci(100)

import timeit

code="""
import fibonacci
fibonacci.fibonacci(100)
"""

t=timeit.timeit(code,number=1)
print('time required =',t,'seconds')

