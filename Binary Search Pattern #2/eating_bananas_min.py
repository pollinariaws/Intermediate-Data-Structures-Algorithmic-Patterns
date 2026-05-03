import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        possible = 1
        start = 1
        end = max(piles)
        while start <= end:
            speed = (start+end)//2
            time = sum(math.ceil(pile/speed) for pile in piles)
            if time > h:
                start = speed + 1
            elif time < h:
                end = speed - 1
            else:
                possible = speed
                end = speed - 1
        return possible
