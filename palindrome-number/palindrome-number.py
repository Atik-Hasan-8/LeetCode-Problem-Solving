class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=x
        reversed_num=0
        
        if x<0 or (x>0 and x%10==0):
            return False
        while number != 0:
            digit = number % 10
            reversed_num = reversed_num * 10 + digit
            number //= 10
            
        if reversed_num==x:
            return True
        else:
            return False