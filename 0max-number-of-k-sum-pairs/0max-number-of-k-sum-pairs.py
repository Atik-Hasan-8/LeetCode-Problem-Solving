class Solution: 
    def maxOperations(self, nums, k):
        nums.sort()
        count = 0
        left = 0
        right = len(nums) -1
        while left < right:
            sum1 = nums[left] + nums[right]
            if sum1 == k:
                count += 1
                left += 1
                right -= 1
            elif sum1 < k:
                left += 1
            else :
                right -= 1
        return count
        
        
            
            
        
        