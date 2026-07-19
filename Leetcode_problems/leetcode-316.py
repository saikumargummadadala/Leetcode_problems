class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #similar to leetcode -1081(identical)
        stack = []
        seen = set()
        last_occurrence = {char: i for i, char in enumerate(s)}
    
        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i <           last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
            
        return "".join(stack)