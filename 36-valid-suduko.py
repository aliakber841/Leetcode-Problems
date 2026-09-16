class Solution(object):
    def isValidSudoku(self, board):
        rows=[]
        cols=[]
        boxes=[]
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for row in range(9):
            for col in range(9):
                digit=board[row][col]
                if digit==".":
                    continue

                boxIndex=(row//3)*3+(col//3)

                if digit in rows[row]:
                    return False
                if digit in cols[col]:
                    return False
                if digit in boxes[boxIndex]:
                    return False

                rows[row].add(digit)
                cols[col].add(digit)
                boxes[boxIndex].add(digit)
        return True