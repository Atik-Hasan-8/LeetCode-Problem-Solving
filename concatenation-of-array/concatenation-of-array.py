class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        container=nums
        nums.extend(container)
        return nums

        