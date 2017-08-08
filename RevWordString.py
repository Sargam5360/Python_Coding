
s= "Hello World 1"

arr = s.split(" ")
x = int(arr[-1])
del arr[-1]
st =  arr[x-1]
arr[x-1] = st[::-1]
print  " ".join(arr)
