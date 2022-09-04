# https://www.geeksforgeeks.org/check-if-given-sudoku-solution-is-valid-or-not/

def isinRange(board):

    for i in range(0, 9):
        for j in range(0, 9):
            # check if in range
            if ((board[i][j] <= 0) or
                (board[i][j] > 9)):
                return False

    return True
 
def isValidSudoku(board):
    if (isinRange(board) == False):
        return False
    
    return True

def isequal(s1, s2):
    pass

def getallpermutations(board):
    print(isValidSudoku(board[:]))