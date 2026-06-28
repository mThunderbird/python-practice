class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn) sorting
        result = []
        print(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                        
        return result
        