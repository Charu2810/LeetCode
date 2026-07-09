class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        sum_1=bin(a+b)[2:]
        return sum_1
        