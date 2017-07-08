
# coding: utf-8

# In[10]:

#Linear Search Program

def linear_search(obj, item, start=0):
    for i in range(start, len(obj)):
        if obj[i] == item:
            return i
    return -1 
    
#Binary Search Program 
def binary_search(arr, ele):
    mid = (len(arr))/2
    if not len(arr):
        return -1
    if ele == arr[mid]:
        return mid
    elif ele > arr[mid]:
        return mid + binary_search(arr[mid:], ele)
    elif ele < arr[mid]:
        return binary_search(arr[:mid], ele)
    else:
        return -1
        
    
        
    
    
arr = [1, 2, 3, 4, 5, 6]

print linear_search(arr,5)

print binary_search(arr,2)

