from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create many sets for each row, col, and box
        # as you iterate through matrix add the number to its related sets
        # So index 0, 0 will be added to row 0, col 0 and box 0
        # If the number is already in the set O(1) lookup it is invalid and we return

        # 9 row sets
        row_sets = [set() for i in range(9)]
        print(row_sets)
        # 9 col sets
        col_sets = [set() for i in range(9)]
        print(col_sets)
        # 9 box sets
        box_sets = [[set(), set(), set()],
                    [set(), set(), set()],
                    [set(), set(), set()]]

        # Iterate through matrix
        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num != ".":

                    if num in row_sets[row]:
                        print("In row set")
                        return False
                    if num in col_sets[col]:
                        print("In col set")
                        return False

                    box_row = row // 3

                    box_col = col // 3
                    print(box_row, box_col, num)
                    if num in box_sets[box_row][box_col]:
                        print("In box set")
                        return False

                    row_sets[row].add(num)
                    print(row, row_sets[row])
                    col_sets[col].add(num)
                    box_sets[box_row][box_col].add(num)

        return True


sol = Solution()
board_test = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sol.isValidSudoku(board_test))

board_test = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sol.isValidSudoku(board_test))
