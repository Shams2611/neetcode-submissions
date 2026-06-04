class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = {}
        for i, n in enumerate(nums):
            if n in new:
                return True 
            new[n] = i

        return False
        