class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        res=0
        for i in sentences:
            word=i.split(' ')
            count=len(word)
            res=max(count,res)
        return res
        