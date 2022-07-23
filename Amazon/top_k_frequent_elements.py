class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counting dic: key = number and value = count
        # freq dic: value = count and key = list of number (ex. [3 [2,3,4]])
        # init the freq dic

        count = {}
        freq = [[] for i in range(len(nums)+1)] # reason for plus one: freq == len(nums)

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for c in range(len(freq)-1, 0, -1):
            for n in freq[c]:
                res.append[n]
            if len(res) >= k:
                return res
            