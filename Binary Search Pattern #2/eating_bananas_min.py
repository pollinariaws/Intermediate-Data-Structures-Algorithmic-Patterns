import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        possible = end
        while start <= end:
            speed = (start+end)//2
            time = sum(math.ceil(pile/speed) for pile in piles)
            if time > h:
                start = speed + 1
            else:
                possible = speed
                end = speed - 1
        return possible
