def indexEqualsValueSearch(arr):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        i = (start+end)/2
        if (arr[i] - i < 0):
            start = i+1
        elif (arr[i] - i == 0):
            return i
        else:
            end = i-1

    return -1
    
    
arr = [-8,0,2,5]

print indexEqualsValueSearch(arr)
