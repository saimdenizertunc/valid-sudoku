import collections


def isValidArray(a):
    return len([item for item, count in collections.Counter(a).items() if count > 1 and item != '.']) == 0


def column(matrix, i):
    return [row[i] for row in matrix]


def isValidSudoku(board):
    for i in range(9):
        if(isValidArray(board[i]) == False):
            return False
        if(isValidArray(column(board, i)) == False):
            return False

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y]
                      for x in range(i, i + 3) for y in range(j, j + 3)]
            if(isValidArray(square) == False):
                return False

    return True
