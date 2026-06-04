class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = {}

        for i, n in enumerate(nums):
            if n in new_set:
                return True

            new_set[n] = n

        return False 
        