class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        res=''.join(stack)
        return res
        