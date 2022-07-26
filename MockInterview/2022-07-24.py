# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]


def allSubsets(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def backTracking(pos, subset, total):
        # edge case: Good
        if total == target:
            res.append(subset.copy()) # need to be deep copy
            return
        # edge case: Bad
        if pos > len(candidates) or total > target:
            return

        # 1. include current candidate as possible subset and unique usege
        prv = -1
        for i in range(pos, len(candidates)):
            if prv == candidates[i]: contiune
            subset.append(candidates[i])
            backTracking(i+1, subset, total+candidates[i])
            subset.pop()
            prv = candidates[i]
        
    backTracking(0, [], 0)
    return res

    
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

# Example 1:

# Input: s = "aaba"
#             ^ ^
# Output: [["a","a","b","a"],["aa","b","a"],["a", "aba"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

# Q: Empty? return []
# checking palindrome => two pointors with backtracking
#                   "aaba"
#                 /       \
#isPalindrome?  "a" start = 0 and end = 0 and curPalindrome
#              /     \
#          "a" "a"   "a" 
#           /
#       "a""a""b"

def partitionalPanlindrome(self, s: str) -> List[List[str]]:
    res = []
        
    def backTracking(start, curList):
        if start >= len(s):
            res.append(curList.copy())
            return

        for end in range(start, len(s)):
            # current sub string
            subStr = s[start:end+1]
            # checking palindrome
            if self.isPalindrome(subStr):
                curList.append(subStr)
                backTracking(start+1, curList)
                curList.pop()    

    backTracking(0, [])
    return res
    
def isPalindrome(self, subStr):
    l, r = 0, len(substr) - 1
    while l < r:
        if subStr[l] != subStr[r]:
            return False
        l, r = l+1, r-1
    return True    































