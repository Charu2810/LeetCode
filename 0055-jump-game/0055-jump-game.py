class Solution(object):
    def canJump(self, nums):
        r=0
        for i in range(len(nums)):
            if i>r:
                return False
            r=max(r,i+nums[i])
        return True