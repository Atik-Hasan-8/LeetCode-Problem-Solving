class Solution:
    def countVowelStrings(self, n: int) -> int:
        myarr = [1, 1, 1, 1, 1]
        for i in range(n-1):
            for j in range(len(myarr)):
                myarr[j]= sum(myarr[j:])
        return sum(myarr)
            
            
        