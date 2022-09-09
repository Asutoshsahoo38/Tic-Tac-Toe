import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s = "X"
p2s = "O"

def check_column(symbols):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbols:
                count+=1
        if count == 3:
            print(symbols,"won")
            return True
    return False

def check_row(symbols):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbols:
                count+=1
        if count == 3:
            print(symbols,"won")
            return True
    return False

def check_diagonals(symbols):
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] == symbols:
        print(symbols,"won")
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbols:
        print(symbols,"won")
        return True
    return False

def won(symbols):
    return check_row(symbols) or check_column(symbols) or check_diagonals(symbols)


def place(symbols):
    print(numpy.matrix(board))
    while(1):
        row = int(input("enter row- 1 or 2 or 3  "))
        col = int(input("enter columns - 1 or 2 or 3 "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1] == "-":
            break
        else:
            print("Invalid syntax. Plz enter again")
    board[row-1][col-1] = symbols
    

def play():
    for turn in range(9):
        if turn%2 == 0:
            print("X turns")
            place(p1s)
            if won(p1s):
                break
        else:
            print("O turns")
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print("match draw")
play()
