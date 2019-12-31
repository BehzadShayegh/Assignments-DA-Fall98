from copy import deepcopy
import sys

lines = sys.stdin.read().split('\n')
n,m,k = list(map(int, lines[0].split()))
a = list(map(lambda l: list(map(int, l.split())), lines[1:]))
# n,m,k = list(map(int, input().split()))
# a = list(map(lambda line: list(map(int, line.split())), lines[1:]))
# a = []
# for i in range(n) :
    # a.append(list(map(int, input().split())))
vect = [0]*(k+1)
vect = [deepcopy(vect) for i in range(m)]
vect = [deepcopy(vect) for i in range(n)]

rightest = downest = True
for i in range(n-1,-1,-1) :
    downest = (i == n-1)
    for j in range(m-1,-1,-1) :
        rightest = (j == m-1)
        v = a[i][j]
        for q in range(k+1) :
            if rightest and downest :
                vect[i][j][q] = int((q==k) or (q+v==k))
            elif downest :
                vect[i][j][q] = vect[i][j+1][q]
                if q+v <= k :
                    vect[i][j][q] += vect[i][j+1][q+v]
            elif rightest :
                vect[i][j][q] = vect[i+1][j][q]
                if q+v <= k :
                    vect[i][j][q] += vect[i+1][j][q+v]
            else :
                vect[i][j][q] = vect[i][j+1][q] + vect[i+1][j][q]
                if q+v <= k :
                    vect[i][j][q] += vect[i][j+1][q+v] + vect[i+1][j][q+v]
            vect[i][j][q] %= (1e9+7)

print(int(vect[0][0][0]))