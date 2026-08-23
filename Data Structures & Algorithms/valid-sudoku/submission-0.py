class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Rows & Cols:
        for i in range(9):
            if not self.isValidSubarr(i, i+1, 0, 9, board):
                print(f"Invalid row {i}")
                return False
            if not self.isValidSubarr(0, 9, i, i+1, board):
                print(f"Invalid col {i}")
                return False
        
        # Boxes:
        for i in range(3):
            for j in range(3):
                if not self.isValidSubarr(i*3, i*3+3, j*3, j*3+3, board):
                    print(f"Invalid box {i}, {j}")
                    return False 

        return True

    
    def isValidSubarr(self, row_start, row_end, col_start, col_end, board: List[List[str]]) -> bool:
        table = set()
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                el = board[i][j]
                if el ==  ".":
                    continue
                if el in table:
                    return False
                table.add(el)
        return True
                
