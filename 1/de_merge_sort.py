def checksum(arr) :
    result = 1
    for i in range(len(arr)) :
        result = (31 * result + arr[i]) % 1000003
    return result

N = int(input())
prime_debug_result = list(input())
debug_result = list()

def com(n, s) :
    global debug_result
    if (n < 2) :
        return s
    s = com(n//2, s)
    s = com(n-n//2, s)
    c1,c2,s0 = 0,0,s
    while c1 < n//2 and c2 < n/2 :
        if prime_debug_result[s]=='1' :
            c1 += 1
        else :
            c2 += 1
        s += 1
    debug_result += prime_debug_result[s0:s]
    r = n-c2-c1
    if c1 == n//2 :
        debug_result += ['2']*r
    else :
        debug_result += ['1']*r
    return s

com(N, 0)

def f(data, debug_data) :
    # print(data)
    if len(data) <= 1 :
        return data, debug_data

    left = list()
    right = list()
    for i,d in enumerate(debug_data[-len(data):]) :
        if d == '1' :
            left.append(data[i])
        else :
            right.append(data[i])
    rem_debug_data = debug_data[:-len(data)]
    right, rem_debug_data = f(right, rem_debug_data)
    left , rem_debug_data = f(left, rem_debug_data)

    return left+right, rem_debug_data

sortedList = list(range(1,N+1))
primeList,_ = f(sortedList, debug_result)
cs = checksum(primeList)
# print(primeList)
print(cs)