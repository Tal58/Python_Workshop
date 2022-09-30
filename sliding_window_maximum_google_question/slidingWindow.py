

from re import X
k = 3
array = [10, 5, 2, 7, 8, 7]
array1 = [1,3,-1,-3,5,3,6,7]

def slidingWindow(arr, k):
    slidingArr = []
    newArr = []
    for i in range(len(arr)-k+1):
        newArr = arr[slice(i,k+i)]
        newArr.sort()
        slidingArr.append(newArr[-1])
    return slidingArr


print(slidingWindow(array,k))
print(slidingWindow(array1,k))


