class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        maximum = max(milestones)
        return min(total, 2 * (total - maximum) + 1)