""""
assignment 1.
print first 10 fibonacci numbers.
"""

f=[0,1]

for j in range(2,10):
    f.append(f[j-2]+f[j-1])
    j=j+1

for j in range(2,10):
    print('f(',j+1,')=',f[j])
    j=j+1

completed.
