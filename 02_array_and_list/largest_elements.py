"""array = [10,50,100,500]
res = array[0]
for i in range(1,len(array)):
    print(i)
    if array[i] > res:
        res = array[i]
        
print(res)"""

# use reduce funtion
"""from functools import reduce
arr = [2,70,80, 120, 11, 17]
res = reduce(max,arr)
print(res)"""

# using sort() funtion
arr = [2,70,80, 120, 11, 17]
arr.sort()
# print(arr)
res = arr[-1]
print(res)