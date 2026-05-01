class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row-1
        left = 0
        right = col-1
        direction = 0
        result = []
        while top <= bottom and left <= right:
            if direction == 0:
                for c in range(left, right+1):
                    result.append(matrix[top][c])
                top += 1
                direction += 1
            elif direction == 1:
                for r in range(top, bottom+1):
                    result.append(matrix[r][right])
                right -= 1
                direction += 1
            elif direction == 2:
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
                direction += 1
            else:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                left += 1
                direction = 0
        return result
