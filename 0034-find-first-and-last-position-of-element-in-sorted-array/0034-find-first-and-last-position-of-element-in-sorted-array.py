class Solution(object):
    def searchRange(self, nums, target):
        f=-1
        l=-1
        for i in range(len(nums)):
            if nums[i]==target:
                if f==-1:
                    f=i
                l=i
        return f,l
