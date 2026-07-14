import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        dp = {}
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                ng1 = math.gcd(g1, x)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                ng2 = math.gcd(g2, x)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans
