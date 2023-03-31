class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        reverse=s[::-1]
        if reverse[len(reverse)-1]=='-':
            reverse=reverse[len(reverse)-1]+reverse[:len(reverse)-1]
        if int(reverse) > 2147483647 or int(reverse)< -2147483647:
            return 0
        else:
            return int(reverse)
        
            
        