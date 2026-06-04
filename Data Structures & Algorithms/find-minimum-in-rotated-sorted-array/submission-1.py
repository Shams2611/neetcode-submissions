class Solution:
    def findMin(self, nums: List[int]) -> int:
        #sorted in ascending 
        # minimum should be on the left side of the middle point 
        l, r = 0, len(nums) - 1
        while l < r: 
            mid =  (l + (r - 1)) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[r]

