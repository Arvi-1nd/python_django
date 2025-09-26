def makeMove(turn,board):
    while True:
        try:
          row = int(input("Enter the row (1-3): "))
          col = int(input("Enter the col (1-3): "))
        except ValueError:
          print("invalid input,enter positive integers")
          continue
            
        if row < 1 or row > 3:
            print("Invalid row.")
        elif col < 1 or col > 3:
            print("Invalid column.")
        elif board[row - 1][col - 1] != " ":
            print("already filled.")
        else:
            board[row - 1][col - 1] = turn
            break
        
        
def checkWin(board,turn):
    lines =[
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    
    for line in lines:
        if all(board[row][col] == turn for row,col in line):
            return True
    return False

def printBoard(board):
    for i in range(len(board)):
        row = board[i]
        print("   | ".join(row))
        if i != len(board) - 1:
            print("---------------")
    


board = [[" "]*3 for _ in range(3)]
turn = "X"
turncount = 0

print("---------Welcome to Tic-Tac-toe game---------")
printBoard(board)
print()

while turncount < 9:
    print(f"{turn}'s turn")
    makeMove(turn,board)
    printBoard(board)
    print()
    
    if checkWin(board,turn):
        print("{turn} has Won!")
        break
    
    turn = "O" if turn == "X" else "X"
    turncount += 1
else:
    print("Tie game!")
    