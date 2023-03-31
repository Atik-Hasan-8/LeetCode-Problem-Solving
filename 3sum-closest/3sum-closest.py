class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum_=nums[i]+nums[l]+nums[r]
                if sum_==target:
                    return sum_
                if abs(sum_-target)<abs(result-target):
                    result=sum_
                if sum_<target:
                    l+=1
                elif sum_>target:
                    r-=1
        return result
                
            
        