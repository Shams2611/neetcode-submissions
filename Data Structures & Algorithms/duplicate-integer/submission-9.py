class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_arr = set()

        for i in nums:
            if i in new_arr:
                return True

            new_arr.add(i)

        return False
        