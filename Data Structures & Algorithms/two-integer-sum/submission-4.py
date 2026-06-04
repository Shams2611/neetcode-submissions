class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, n in enumerate(nums):
            difference = target - nums[i]

            if difference in result:
                return [result[difference], i]
        
            result[n] = i 