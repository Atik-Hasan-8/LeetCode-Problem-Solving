class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix=[]
        for i in range(len(s)):
            prefix.append(s[:i+1])
        count=0
        for i in prefix:
            for j in words:
                if i==j:
                    count+=1
        return count
        
        
        
        