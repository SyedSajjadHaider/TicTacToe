#----------------------
def print_block1(a="",b="",c="",d="",e="",f="",g="",h="",i=""):
    print("_",a,"_|_",b,"_|_",c,"_")
    print("_",d,"_|_",e,"_|_",f,"_")
    print(" ",g," | ",h," | ",i," ")
#----------------------
def win_or_loose():
    if a==d==g=="x":
        print("x won")
        exit()
    elif a==d==g=="0":
        print("0 won")
        exit()
    else:
      pass

    if a==b==c=="x":
        print("x won")
        exit()
    elif a==b==c=="0":
        print("0 won")
        exit()
    else:
        pass

    if a==e==i=="x":
        print("x won")
        exit()
    elif a==e==i=="0":
        print("0 won")
        exit()
    else:
        pass
    if g==h==i=="x":
        print("x won")
        exit()
    elif g==h==i=="0":
        print("0 won")
        exit()
    else:
        pass

    if d==e==f=="x":
        print("x won")
        exit()
    elif d==e==f=="0":
        print("0 won")
        exit()
    else:
        pass
    if b==e==h=="x":
        print("x won")
        exit()
    elif b==e==h=="0":
        print("0 won")
        exit()
    else:
        pass
#==============================================
a="."
b="."
c="."
d="."
e="."
f="."
g="."
h="."
i="."
def print_block2(pos,symbol):

# Inserting data into block

    global a,b,c,d,e,f,g,h,i

    if pos == 1 and symbol == "x":
        a="x"
    elif pos==1 and symbol == "0":
        a="0"
    if pos == 2 and symbol == "x":
        b="x"
    elif pos==2 and symbol == "0":
        b="0"
    if pos == 3 and symbol == "x":
        c="x"
    elif pos==3 and symbol == "0":
        c="0"
    if pos == 4 and symbol == "x":
        d="x"
    elif pos==4 and symbol == "0":
        d="0"
    if pos == 5 and symbol == "x":
        e="x"
    elif pos==5 and symbol == "0":
        e="0"
    if pos == 6 and symbol == "x":
        f="x"
    elif pos==6 and symbol == "0":
        f="0"
    if pos == 7 and symbol == "x":
        g="x"
    elif pos==7 and symbol == "0":
        g="0"
    if pos == 8 and symbol == "x":
        h="x"
    elif pos==8 and symbol == "0":
        h="0"
    if pos == 9 and symbol == "x":
        i="x"
    elif pos==9 and symbol == "0":
        i="0"
    print("_",a,"_|_",b,"_|_",c,"_")
    print("_",d,"_|_",e,"_|_",f,"_")
    print(" ",g," | ",h," | ",i," ")

    win_or_loose() # checking win pattern is matched or not 
#----------------------
def player1():
    print("Player1 is x \n")
    pos = int(input(""))
    print_block2(pos,"x")  # calling global TicTacToe block with position and symbol
#----------------------    
def player2():
    print("Player2 is 0 \n")
    pos = int(input(""))
    print_block2(pos,"0") # calling global TicTacToe block with position and symbol
#----------------------

#---------------START OF MAIN ----------------------

print_block1(a="1",b="2",c="3",d="4",e="5",f="6",g="7",h="8",i="9")
#Priting the tic tac toe table with position number
start = input("who want to start p1 or p2\n")
# asking user who will start
#----------------------
#Total Nine chances 
count = 1
if start == "p1":
	while count !=10:
	    player1()
	    player2()
	    count = count + 1
elif start == "p2":
	while count !=10:
	    player1()
	    player2()
	    count = count + 1
#---------------END OF MAIN ----------------------
