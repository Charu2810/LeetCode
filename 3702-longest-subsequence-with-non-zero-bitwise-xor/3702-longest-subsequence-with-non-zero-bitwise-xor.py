class Solution(object):
    def longestSubsequence(self, nums):
        count=0
        total=0
        for i in nums:
            total |= i>0
            count ^=i
        return total * (len(nums)- (not count))