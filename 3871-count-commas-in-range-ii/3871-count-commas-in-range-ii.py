class Solution:
    def countCommas(self, n: int) -> int:
        count, a = 0, 1000
        while a <= n:
            count += n - a + 1
            a *= 1000
        return count
