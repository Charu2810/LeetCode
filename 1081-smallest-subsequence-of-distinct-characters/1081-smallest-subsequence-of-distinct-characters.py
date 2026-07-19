class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
                
        return "".join(stack)
