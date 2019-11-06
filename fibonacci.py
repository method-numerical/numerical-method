"""
assignment 1
module that can result any number of fibonacci number.

"""
def fibonacci(n):
    f=[0,1]
    
    for j in range(2,n):               #this list is [2,.......,n-1].
        f.append(f[j-1]+f[j-2])        #any entry is sum of two entries before it.
        j=j+1                          #initial terms of series.

    for k in range(0,n):
        print('f(',k+1,')=',f[k])      #to print the numbers.
        k=k+1
    return

