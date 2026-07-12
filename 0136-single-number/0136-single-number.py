class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        for x in freq:
            if freq[x] == 1:
                return x