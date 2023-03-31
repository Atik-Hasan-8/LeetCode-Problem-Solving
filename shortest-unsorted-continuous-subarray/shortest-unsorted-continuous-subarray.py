class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_k = float('inf')
        max_k = float('-inf')
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_k = min(min_k, nums[i])
    
        for j in range(len(nums)-2, -1, -1):
            if nums[j] > nums[j+1]:
                max_k = max(max_k, nums[j])
        
        for l in range(len(nums)):
            if min_k < nums[l]:
                break
        for r in range(len(nums)-1, -1, -1):
            if max_k > nums[r]:
                break
        return r - l + 1 if r -l > 0 else 0