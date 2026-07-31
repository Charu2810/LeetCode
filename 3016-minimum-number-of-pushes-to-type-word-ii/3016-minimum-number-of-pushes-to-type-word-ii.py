class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=[0]*26
        for ch in word:
            freq[ord(ch) - ord('a')] +=1
        freq.sort()
        min_p=0
        pushc=0
        for i in range(25,-1,-1):
            cuur=25-i
            if cuur%8==0:
                pushc +=1
            min_p +=freq[i]*pushc
        return min_p
        