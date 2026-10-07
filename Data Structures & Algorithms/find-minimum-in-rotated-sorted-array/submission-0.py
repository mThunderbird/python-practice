class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if nums[low] <= nums[high]:
            return nums[low]
        
        while low < high - 1:
            mid = (low + high) // 2

            if nums[low] <= nums[mid]:
                low = mid
            else:
                high = mid
        
        return nums[high]