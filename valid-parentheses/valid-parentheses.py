
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='{':
                stack.append('}')
            elif item=='[':
                stack.append(']')
            elif len(stack)==0 or item !=stack.pop():
                return False
        return len(stack)==0