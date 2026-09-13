#solution by ai...
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != char:
                    return False
        return len(stack) == 0


#my dumb code... i was doing '(' '(' instead of doing '(' ')' lol...
class Solution:
    def isValid(self, s: str) -> bool:
        left=0
        right=len(s)-1
        res=False
        while left<=right:
            if s[left]==s[right]:
                res=True
                left+=1
                right-=1
            else:
                res=False
        return res