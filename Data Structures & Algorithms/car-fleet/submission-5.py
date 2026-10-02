import math
from collections import deque
class Solution:

    # Constraints:
    # 0 < n <= 10^6
    # target > 0
    # each speed is > 0
    # 0 <= positions < target - edge case 0 cars
    # no 2 cars start at the same position

    # O(n^2) is too expensive we need something faster

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = zip(position, speed)
        car_fleets = sorted(car_fleets, key=lambda x: x[0], reverse=True) # O(nlogn)
        
        fleets = 0
        last_time = 0
        for pos, spd in car_fleets:
            time_to_target = (target - pos) / spd

            if time_to_target > last_time:
                # Not reaching next fleet
                fleets += 1
                last_time = time_to_target

        return fleets