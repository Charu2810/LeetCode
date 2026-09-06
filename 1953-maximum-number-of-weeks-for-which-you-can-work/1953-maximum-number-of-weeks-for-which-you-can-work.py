class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = max(milestones)
        sm = sum(milestones) - mx
        if sm >= mx:
            return sm+mx
        else: 
            return 2*sm+1 