import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        current_max = 0
        
        for x in nums:
            current_max = max(current_max, x)
            prefixGcd.append(math.gcd(x, current_max))
            
        prefixGcd.sort()
        
        ans = 0
        l, r = 0, len(prefixGcd) - 1
        while l < r:
            ans += math.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
            
        return ans
