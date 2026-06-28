class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 3 4 4 5 6 7 7 8 - non-decreasing order
        left, right = 0, len(numbers) - 1

        while left < right:
            csum = numbers[left] + numbers[right]
            if csum == target:
                return [left + 1, right + 1]
            elif csum > target:
                right -= 1
            elif csum < target:
                left += 1