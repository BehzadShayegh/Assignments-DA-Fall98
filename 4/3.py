import numpy as np 

def f(arr,s,haveone) :
    if haveone and s==0 :
        return True
    if len(arr) == 0 :
        return False
    if f(arr[1:],s,haveone) :
        return True
    if f(arr[1:],s-arr[0],True) :
        return True
    return False

maxSum = 0
n = int(input())
arr = list()
for i in range(n) :
    a,b,c = input().split()
    a = 1 if a == 'acid' else -1
    b = int(b)
    c = int(c)
    arr.append(a*b*c)
    maxSum += b*c

if f(arr,0,False) :
    print('yes')
else :
    print('no')