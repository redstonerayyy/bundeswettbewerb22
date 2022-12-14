from sudoku import getallpermutations, getdiagonals, getsquare, getvertical, isValidSudoku, isequal, printarr, rotatesudoku, swaphorizontal, swapnumbers, swapvertical

def readsudoku(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.read().split("\n")

        while "" in lines:
            lines.remove("")

        sudoku1 = lines[:9]
        sudoku2 = lines[9:]

        for i in range(len(sudoku1)):
            new = []
            for j in sudoku1[i].split(" "):
                new.append(int(j))
            
            sudoku1[i] = new

        for i in range(len(sudoku2)):
            new = []
            for j in sudoku2[i].split(" "):
                new.append(int(j))
            
            sudoku2[i] = new

        return sudoku1, sudoku2


# main code
for i in range(1):
    sudoku1, sudoku2 = readsudoku(f"sudoku{i}.txt")
    printarr(sudoku1)
    print(isValidSudoku(sudoku1))
    printarr(getsquare(sudoku2, 0, 0))
    # print(isValidSudoku(sudoku1))
    # printarr(swaphorizontal(sudoku1, 0, 1))
    # print(isValidSudoku(sudoku1))
