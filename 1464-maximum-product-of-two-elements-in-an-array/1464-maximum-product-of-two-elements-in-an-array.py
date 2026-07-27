class Solution(object):
    def maxProduct(self, nums):
        d1=d2=0
        for i in nums:
            if d1<=i:
                d2=d1
                d1=i
            elif d2<i:
                d2=i
        return (d1-1)*(d2-1)

        
        