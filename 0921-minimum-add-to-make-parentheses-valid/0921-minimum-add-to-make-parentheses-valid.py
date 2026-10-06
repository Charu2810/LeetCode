class Solution(object):
    def minAddToMakeValid(self, s):
        o=0
        a=0
        for c in s:
            if c=='(':
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    a+=1
        return a+o

        