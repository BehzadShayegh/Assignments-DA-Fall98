n = int(input())

flowers = list(map(int, input().split()))

d = 0
for i in reversed(range(1,n)) :
    if flowers[i] == flowers[i-1] :
        del flowers[i]
        d += 1

n = len(flowers)

if n <= 1 :
    print(d)
    exit()

flowers = [flowers[1]]+flowers+[flowers[-2]]

c = 0
for i in range(1, n+1) :
    if flowers[i-1] < flowers[i] > flowers[i+1] \
    or flowers[i-1] > flowers[i] < flowers[i+1] :
        c += 1


print(n-c+d)