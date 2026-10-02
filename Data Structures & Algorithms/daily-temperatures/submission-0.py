from collections import deque

class Solution:

    # Constraints: 
    # len(temps) > 0 and len(temps) < 10^6
    # temps[i] > 0 and temps[i] <= 100

    # Naive solution:
    # for each day i:
    # go forward until you find a day with warmer temp
    # O(n^2) => 10^12 > 10^8 => too slow

    # Improved solution:
    # 

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]  # O(n)
        to_fill = deque()

        # 30 29 -> to_fill will have both 0 1
        # 30 31 -> to_fill will be only 1

        # O(n) total for loop
        for idx, temp in enumerate(temperatures): # each day once 
            while len(to_fill) > 0:                          
                if temp > temperatures[to_fill[-1]]:  # Loses one 
                    res[to_fill[-1]] = idx - to_fill[-1]
                    to_fill.pop()
                else:                                 # Or reduces one step
                    break

            to_fill.append(idx) # Gains one
        
        # O(n)
        while len(to_fill) > 0:
            res[to_fill.pop()] = 0
        
        # Total complexity O(n)
        return res
