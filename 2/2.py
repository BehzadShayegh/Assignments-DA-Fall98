from math import inf
jen = input()
want = input()
costs = list(map(int, input().split()))
wantLen = len(want)
jenlen = len(jen)
cost = inf

for i,char in enumerate(jen) :
    costt = 0
    ii = i
    j = 0
    while j < wantLen :
        if ii < jenlen and jen[ii] == want[j] :
            ii += 1
            j += 1
        else :
            costt += costs[0] if want[j] == 'A'\
                else costs[1] if want[j] == 'C'\
                else costs[2] if want[j] == 'G'\
                else costs[3]
            j += 1
    cost = min(cost , costt)

print(cost)