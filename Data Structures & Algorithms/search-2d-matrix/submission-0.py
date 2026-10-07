class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            current_val = matrix[mid // cols][mid % cols]
            # 0 1
            # 2 3 
            # 4 5   => if asked for id=4 => 5 // 2 => 2, 5 % 2 => 1
            if current_val == target:
                return True
            elif current_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
