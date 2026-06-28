class Solution:
    def trap(self, height: List[int]) -> int:

        maxfromleft = []
        maxfromright = []

        maxx = 0
        for i in height:
            maxx = max(i, maxx)
            maxfromleft.append(maxx)
        maxx = 0
        for i in reversed(height):
            maxx = max(i, maxx)
            maxfromright.append(maxx)
        maxfromright = maxfromright[::-1]


        water = 0
        for i in range(len(height)):
            water += min(maxfromleft[i], maxfromright[i]) - height[i]
        
        return water