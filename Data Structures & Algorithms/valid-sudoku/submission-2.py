class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cek baris
        for row in board:
            checked = set()
            for num in row:
                if num == ".":
                    continue
                if num in checked:
                    return False
                checked.add(num)
        
        # cek kolom
        for index in range(9):
            col = []
            for i in range(9):
                col.append(board[i][index])
            
            checked = set()
            for num in col:
                if num == ".":
                    continue
                if num in checked:
                    return False
                checked.add(num)
        
        # cek kotak 3x3
        for b in range(9):
            box_row = b // 3
            box_col = b % 3
            row_start = box_row * 3
            col_start = box_col * 3
            
            box = []
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    box.append(board[r][c])
            
            checked = set()
            for num in box:
                if num == ".":
                    continue
                if num in checked:
                    return False
                checked.add(num)
        
        return True