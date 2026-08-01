class Solution(object):
    def predictTheWinner(self, nums):
        n=len(nums)
        if n%2==0:
            return True
        dp=list(nums)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[j]=max(nums[i]-dp[j],nums[j]-dp[j-1])
        return dp[-1]>=0
        """
        :type nums: List[int]
        :rtype: bool
        """
        