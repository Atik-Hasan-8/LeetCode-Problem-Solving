class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        val=n
        for i in range(n):
            result.append(nums[i])
            result.append(nums[val])
            val+=1
        return result
            
            
        
        