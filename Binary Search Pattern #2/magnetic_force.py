class Solution:
    def possible_distance(self, position, m, dist):
        putted_balls = 1
        last_position = position[0]
        for i in range(len(position)):
            if position[i] >= last_position + dist:
                last_position = position[i]
                putted_balls += 1
        if putted_balls < m:
            return False
        return True
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        start = 1
        end = position[-1] - position[0]
        possible = 1
        while start <= end:
            distance = (start+end)//2
            if self.possible_distance(position, m, distance):
                possible = distance
                start = distance + 1
            else:
                end = distance - 1
        return possible
