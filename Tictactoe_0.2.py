board = ["."]*10
def print_board(player):
    print("_",board[1],"_|_",board[2],"_|_",board[3],"_")
    print("_",board[4],"_|_",board[5],"_|_",board[6],"_")
    print(" ",board[7]," | ",board[8]," | ",board[9]," ")

    check_win(player)

def check_win(player):
    if ( (board[1] == board[2] == board[3] !=".")  or 
       (board[4] == board[5] == board[6] !=".")  or
       (board[7] == board[8] == board[9] !=".")  or
       (board[1] == board[4] == board[7] !=".")  or
       (board[2] == board[5] == board[8] !=".")  or
       (board[3] == board[6] == board[9] !=".")  or
       (board[1] == board[5] == board[9] !=".")  or
       (board[3] == board[5] == board[7] !=".")):
          print("{} won the game ".format(player))
          exit()
    elif count == 5:
        print("draw")
        exit()
def player1():
    pos =int(input("Player 1 Enter position"))
    board[pos] = "X"
    print_board("p1")


def player2():
    pos = int(input("player2 Enter position"))
    board[pos] = "O"
    print_board("p2")


start = input("who wants to start, enter option p1 or p2")
count = 1
if start  == "p1":
    while count !=6:
        player1()    

        if count == 5:
            break
        
        player2()
        count = count + 1
else:
    while count !=6:
        player2()

        if count == 5:
            break
        
        player1()    
        count = count + 1
    
