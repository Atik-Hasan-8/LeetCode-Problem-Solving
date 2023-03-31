class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1=deque()
        stack_2=deque()
        
        for i in s:
            if i!='#':
                stack_1.append(i)
            else:
                if not stack_1:
                    continue
                stack_1.pop()
        
        for j in t:
            if j!='#':
                stack_2.append(j)
            else:
                if not stack_2:
                    continue
                stack_2.pop()
        return stack_1==stack_2
        
        
        