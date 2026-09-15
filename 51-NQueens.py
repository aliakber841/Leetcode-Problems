def isSafe(board,row,col,n):
    #Horizontal
    for i in range(0,n):
        if board[row][i]=="Q":
            return False
    # Vertical 
    for i in range(0,n):
        if board[i][col]=="Q":
            return False
            
    #Left Diagonal
    r,c=row,col
    while r>=0 and c>=0:
        if board[r][c]=="Q":
            return False
        r-=1
        c-=1
        
    #Right Diagonal
    r,c=row,col
    while r<=n-1 and c<=n-1:
        if board[r][c]=="Q":
            return False
        r-=1
        c+=1
        
    return True 


def nQueens(board,row,n,result):
    if row==n:
        new_board=[]
        for row in board:
            new_row="".join(row)
            new_board.append(new_row)
        result.append(new_board)
        return
    for i in range(0,n):
        if isSafe(board,row,i,n):
            board[row][i]=('Q')
            nQueens(board,row+1,n,result)
            board[row][i]='.'
class Solution(object):
    def solveNQueens(self, n):
        board=[]
        for i in range(0,n):
            row=[]
            for j in range(0,n):
                row.append(".")
            board.append(row)
        result=[]
        nQueens(board,0,n,result) 
        return result