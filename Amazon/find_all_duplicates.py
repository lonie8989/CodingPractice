# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

nums = [4,3,2,7,8,2,3,1]
res = []
dict = {}

for i in nums:
    if i in dict:
        res.append(i)
    else:
        dict[i] = 0

print(res)
    