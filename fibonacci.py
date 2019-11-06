"""
assignment 1
to result first 10 fibonacci numbers
"""

f=[0,1]                             #defining first 2 numbers.

for j in range (2,10):              #this is a list from 2 to 9.
    f.append(f[j-1]+f[j-2])         #any entry is sum of two entries before it
    j=j+1

for j in range (0,10):
    print('f(',j+1,')=',f[j])
    j=j+1
