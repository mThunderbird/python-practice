class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # a + b = target
        # a = target - b
        # b = target - a
        
        # 
        numMap = {}
        for idx, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = idx
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff not in numMap: # no matching number
                continue
            if idx == numMap[diff]: # matching number is the same one
                continue
            return sorted([idx, numMap[diff]])


