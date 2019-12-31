n = int(input())
a = list(map(int, input().split()))

vect = [1]
for i in range(1,n) :
    vect.append(sum(vect)+vect[-1])

ans = 1
for i,ai in enumerate(reversed(a)) :
    ans += (ai-1)*vect[i]
    ans %= 1000007

print(ans)