class Solution:
    def checkDivisibility(self, n: int) -> bool:
        o=n
        ds=0
        dp=1
        while n>0:
            d=n%10
            ds +=d
            dp *=d
            n//=10
        div=ds+dp
        return o%div==0
        