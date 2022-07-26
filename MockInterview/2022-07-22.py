# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Q: empty nums => []

# 1. backTracking
#         [1,2,2,3]
#                ^  
#  in   [1]     [] not-in
#  V [1,2] [1] 
#  [1,2,2] V[1,3][1] <- no need to add 2, go til i reaching to len(nums)
# Time: O(2^n)
# Space: O(2^n)

def noDuplicatedSubSet(nums: List[int]) -> List[List[int]]:
    res = []

    def backTrack(p, subset):
        if p == len(nums):
            res.append(subset.copy()) # deep copy
            return

        if p > len(nums):
            return

        subset.append(nums[p])
        backTrack(p+1, subset)
        subnet.pop()

        while p + 1 < len(nums) and nums[p] == nums[p+1]
            p+1
        backTrack(p+1, subset)


    backTrack(0, [])
    return res