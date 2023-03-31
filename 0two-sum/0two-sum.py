class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        for index,elements in enumerate(nums):
            complement=target-elements
            if complement in data:
                return[data[complement],index]
            data[elements]=index
            
        return []