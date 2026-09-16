def getBoxIndex(row, col):
    starting_row=(row//3)*3
    starting_col=(col//3)*3
    return (starting_row//3)*3+(starting_col//3)

def findBestCell(board,rows,cols,boxes):
    bestRow=-1
    bestCol=-1
    bestCandidates=None

    for row in range(9):
        for col in range(9):
            if board[row][col]==".":
                boxIndex=getBoxIndex(row,col)
                candidates=[]
                for numDigit in range(1,10):
                    digit=str(numDigit)
                    if digit not in rows[row] and digit not in cols[col] and digit not in boxes[boxIndex]:
                        candidates.append(digit)

                if bestCandidates is None or len(candidates)<len(bestCandidates):
                    bestRow=row
                    bestCol=col
                    bestCandidates=candidates

                    if len(candidates)==0:
                        return bestRow,bestCol,bestCandidates
    return bestRow,bestCol,bestCandidates

def solveBoard(board,rows,cols,boxes):
    row,col,candidates=findBestCell(board,rows,cols,boxes)
    if row==-1:
        return True
    boxIndex=getBoxIndex(row,col)

    for digit in candidates:
        board[row][col]=digit
        rows[row].add(digit)
        cols[col].add(digit)
        boxes[boxIndex].add(digit)

        if solveBoard(board,rows,cols,boxes):
            return True

        board[row][col]="."
        rows[row].remove(digit)
        cols[col].remove(digit)
        boxes[boxIndex].remove(digit)
    return False
class Solution(object):
    def solveSudoku(self, board):
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
                if digit!=".":
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxIndex=getBoxIndex(row,col)
                    boxes[boxIndex].add(digit)
        solveBoard(board,rows,cols,boxes)