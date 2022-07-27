# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:

# Input: points = [[1,1][-2,2],[1,3]], k = 1
# d = {0: 2, 1: 8, 2: 10}
# Output: [[-2,2]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Q: k could be 0? no
# Q: extra space? yes

# need to make max heap and loop k
def kthDistance(points: list[list[int]], k: int) -> list[list[int]]:
    res = []
    ds = []

    for i in range(len(points)):
        d = points[i][0]**2 + points[i][1]**2
        heapq.heappush(ds, (d, i)) # store (distence, index) into min heap by distance

    for _ in range(K):
        n = heapq.heappop()[1] # get index 
        res.append(points[n])

    return res

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
    
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# nums size? greater than k
# k == 0 ? no 
    
# sort? nlogn so no!
# only max heap => rev min heap
# time: o(k)
# space: o(n)

import heapq

def kthLargestElementinArray(nums: List[int], k: int) -> int:
    res = 0
    rev_nums = [-n for n in nums]:
    heapq.heapify(rev_nums) # max heap

    for _ in range(k):
        res = heapq.heappop(rev_nums)

    return -res
    
    
    
    












