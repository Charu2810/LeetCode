class Solution(object):
    def maximumWealth(self, accounts):
        r=0
        for i in accounts:
            r=max(r,sum(i))
        return r