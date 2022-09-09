# https://www.geeksforgeeks.org/check-if-given-sudoku-solution-is-valid-or-not/

def isValidSudoku(board):
    if not isinRange(board):
        return "range"
    
    # check vertical
    for i in range(9):
        for j in range(9):
            if getvertical(board, i).count(j + 1) > 1:
                return "vertical"

    # check horizontal
    for i in range(9):
        for j in range(9):
            if gethorizontal(board, i).count(j + 1) > 1:
                return "horizontal"
    
    # check squares
    for y in range(3):
        for x in range(3):
            square = getsquare(board, x, y)
            for i in range(9):
                if square.count(i + 1) > 1:
                    return "squares"

    # diagonals are not valid in the sudokus so they probably
    # should not be checked
    # check diagonals
    # for diagonal in getdiagonals(board):
    #     for i in range(9):
    #         if diagonal.count(i + 1) > 1:
    #             return "diagonals"

    return "valid"

def isinRange(board):
    for y in range(9):
        for x in range(9):
            # check if in range
            if (board[y][x] < 0) or (board[y][x] > 9):
                return False

    return True

def getdiagonals(board):
    diagonal1 = []
    for i in range(9):
        diagonal1.append(board[i][i])
    diagonal2 = []
    for y in range(9):
        diagonal2.append(board[y][8-y])

    return [ diagonal1, diagonal2 ]

def setsquare(board, x, y, square):
    for i in range(3 * y, 3 + 3 * y):
        for j in range(3 * x, 3 + 3 * x):
            board[i][j] = square[i - 3 * y][j - 3 * x]

    return board

def getsquare(board, x, y): # 0, 1 or 2
    square = []
    for i in range(3 * y, 3 + 3 * y):
        line = []
        for j in range(3 * x, 3 + 3 * x):
            line.append(board[i][j])
        
        square.append(line)

    return square


def gethorizontal(board, y):
    return board[y]

def sethorizontal(board, y, horizontal):
    board[y] = horizontal
    return board

def setvertical(board, x, vertical):
    for y in range(9):
        board[y][x] = vertical[y]
    
    return board

def getvertical(board, x):
    vertical = []

    for y in range(9):
        vertical.append(board[y][x])
    
    return vertical


def rotatesudoku(board, rotateright=True):
    rotated = []

    for x in range(9):
        if rotateright:
            rotated.append(getvertical(board, x)[::-1])
        else:
            rotated.append(getvertical(board, x))

    if not rotateright:
        rotated = rotated[::-1]
    
    board = rotated
    return board

def isequal(s1, s2):
    for y in range(9):
        for x in range(9):
            if s1[y][x] != s2[y][x]:
                return False
    
    return True

def printarr(arr):
    for i in arr:
        print(i)

def swapvertical(board, x1,x2):
    v1 = getvertical(board, x1)
    v2 = getvertical(board, x2)
    setvertical(board, x2, v1)
    setvertical(board, x1, v2)

    return board

def swaphorizontal(board, y1, y2):
    h1 = gethorizontal(board, y1)
    h2 = gethorizontal(board, y2)
    sethorizontal(board, y1, h2)
    sethorizontal(board, y2, h1)

    return board

def swapnumbers(board, n1, n2):
    for y in range(9):
        for x in range(9):
            if board[y][x] == n1:
                board[y][x] = n2
            elif board[y][x] == n2:
                board[y][x] = n1
            else:
                pass
    return board

def getallpermutations(board):
    print(board)
