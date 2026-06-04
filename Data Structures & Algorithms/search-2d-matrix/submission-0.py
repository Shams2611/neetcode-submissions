class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        length = len(matrix) * len(matrix[0])
        right = length - 1
        column = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2

            row = mid // column 
            col = mid % column 

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1


        return False

            
        