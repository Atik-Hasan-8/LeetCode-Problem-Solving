class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        begin,end=0,len(nums)-1
        
        while begin<=end:
            if nums[begin]%2==0:
                begin+=1
            else:
                nums[begin],nums[end]=nums[end],nums[begin]
                end-=1
          
        return nums
        
        