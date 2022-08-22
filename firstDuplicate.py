# Asked By:  google
# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there is more than 1 duplicated number, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
# Example
# For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.
# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2, so the answer is 3.
# For a = [2, 2], the output should be solution(a) = 2;
# For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.

def firstDuplicate(arr):
    newArr = []
    if len(arr)== len(set(arr)):
        return -1
    else:
        for x in arr:
            if arr.count(x)>1:
                if x in newArr:
                    return x
                else:
                    newArr.append(x)
 

a = [2, 1, 3, 5, 3, 2]    
b = [2, 4, 3, 5, 1]
c = [2, 2]
print(firstDuplicate(a))
print(firstDuplicate(b))
print(firstDuplicate(c))
