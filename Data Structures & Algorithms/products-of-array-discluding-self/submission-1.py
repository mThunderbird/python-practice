class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #  1  2  4  6
        #  1  1  2  8 - leftProds
        # 48 24  6  1 - rightProds
        # 48 24 12  8 - exceptProds

        prefix = 1
        suffix = 1
        res = [1 for _ in nums]

        for idx in range(1, len(nums)):
            prefix = prefix * nums[idx-1]
            res[idx] = prefix

        for idx in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[idx+1]
            res[idx] *= suffix

        return res

        