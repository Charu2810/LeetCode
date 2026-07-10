class Solution(object):
    def findLHS(self, nums):
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ans = 0
        for i in freq:
            if i + 1 in freq:
                if freq[i] + freq[i + 1] > ans:
                    ans = freq[i] + freq[i + 1]
        return ans