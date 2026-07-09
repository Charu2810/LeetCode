class Solution(object):
    def jump(self, nums):
        j=0
        e=0
        f=0
        for i in range(len(nums)-1):
            f=max(f,i+nums[i])
            if i==e:
                j+=1
                e=f
        return j