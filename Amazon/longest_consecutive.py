# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ma_set = set(nums)
        nums = list(ma_set)
        nums.sort()
        res = 1
        temp = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i] - 1:
                temp += 1
                res = max(temp, res)
            else:
                temp = 1
                
        return res
            