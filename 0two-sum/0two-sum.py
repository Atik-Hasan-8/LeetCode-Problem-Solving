class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in container:
                return [i,container[diff]]
            container[nums[i]]=i
        return []