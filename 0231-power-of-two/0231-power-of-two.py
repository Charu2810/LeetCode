class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and not (n & (n - 1))
        """
        :type n: int
        :rtype: bool
        """
        