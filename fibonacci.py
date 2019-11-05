"""
assignment 1
code to result first 10 fibonacci numbers

"""

f=[0,1]                            #initial terms of series.

for j in range(2,10):              #this list is [2,........9].
    f.append(f[j-1]+f[j-2])        #any entry is sum of two entries before it.
    j=j+1

for k in range(0,10):
    print('f(',k+1,')=',f[k])      #to print the numbers.
    k=k+1
