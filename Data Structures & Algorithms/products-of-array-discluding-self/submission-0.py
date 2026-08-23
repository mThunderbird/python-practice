class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #  1  2  4  6
        #  1  1  2  8 - leftProds
        # 48 24  6  1 - rightProds
        # 48 24 12  8 - exceptProds

        leftProds = [1 for _ in nums]
        rightProds = [1 for _ in nums]

        for idx in range(1, len(nums)):
            leftProds[idx] = leftProds[idx-1] * nums[idx-1]

        for idx in range(len(nums)-2, -1, -1):
            rightProds[idx] = rightProds[idx+1] * nums[idx+1]

        output = [leftProds[idx] * rightProds[idx] for idx in range(len(nums))]
        return output

        