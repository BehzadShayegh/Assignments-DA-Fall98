def merge(arr1, arr2) :
    result = list()
    while len(arr1) > 0 and len(arr2) > 0 :
        if arr1[0] < arr2[0] :
            print(1,end='')
            result.append(arr1[0])
            del arr1[0]
        else :
            print(2,end='')
            result.append(arr2[0])
            del arr2[0]
        
    result += arr1
    result += arr2
    return result

def merge_sort(arr) :
    n = len(arr)
    if n <= 1 :
        return arr
    
    mid = n//2
    first_half = merge_sort(arr[:mid])
    second_half = merge_sort(arr[mid:])
    return merge(first_half, second_half)

inp = list(input())
merge_sort(inp)