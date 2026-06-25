class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            curr = (top + bot) // 2
            if matrix[curr][0] > target:
                bot = curr - 1
            elif matrix[curr][-1] < target:
                top = curr + 1
            else:
                break

        # if not (top <= bot):
        #     return False
        
        left, right = 0, cols - 1
        while left <= right:
            if matrix[curr][(left + right) // 2] == target:
                return True
            elif matrix[curr][(left + right) // 2] < target:
                left = (left + right) // 2 + 1
            else:
                right = (left + right) // 2 - 1

        return False