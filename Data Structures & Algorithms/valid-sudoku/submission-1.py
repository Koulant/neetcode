class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each cell
        # If row, col, or cell contains duplicates return False
        # If ".", skip

        row_set = defaultdict(set) # Map index to values
        col_set = defaultdict(set)
        cell_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit == ".":
                    continue

                if digit in row_set[r]:
                    return False
                
                if digit in col_set[c]:
                    return False
                
                cell_index = (r // 3, c // 3)

                if digit in cell_set[cell_index]:
                    return False
                
                row_set[r].add(digit)
                col_set[c].add(digit)
                
                cell_set[cell_index].add(digit)

        return True
                




        