class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = [(idx, num) for idx, num in enumerate(nums)]
        nums.sort(key=lambda idxnum: idxnum[1])

        left = 0
        right = len(nums) - 1

        while left < right:
            currentSum = nums[left][1] + nums[right][1]
            if currentSum == target:
                return sorted([nums[left][0], nums[right][0]])
            elif currentSum > target:
                right -= 1
            else:
                left += 1
        
        return None
        