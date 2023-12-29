import player
# Create board array
# Variable assignment without types 
boardarray = [                    #Created and assigned 2-D Array
              ["_","_","_"],      # (lines 3-7 Array init with string literals)
              ["_","_","_"],
              [" "," "," "]
              ]
# Create Renderboard fxn     (   renderboard('X')  )
def renderboard(boardarray):      # fxn def with one parameter
    # Can be modified to exactly how we want
    outerlength = len(boardarray)
    #Problem 1: how to print without a new line
    #Prob 2: how to print create a new line everytime you hit the end of a row (check row variable, see last time when it's going to access the row OR
    # )
    for i in range(outerlength):
        innerlength = len(boardarray[i])
        for j in range(innerlength):
            print(boardarray[i][j], end="")  #print 
            if(j == 0 or j == 1):
               print("|", end="")
            if(j == 2):
               print(" ")  # print a new line
            
    # Another way of doing the top for nested loop () CANNOT be modified -> Assumes to go to full size of object
    # for i in boardarray:
    #     for j in boardarray[i]:
    
    # for(let i = 0; i < boardarray.length; i++)         #this iterates thru the columns
    #   for(let j = 0; j < boardarray[i].length;j++)    #this iterates thru the rows
       
            
            
            
    # print(f'{boardarray[0][0]}|{boardarray[0][1]}|{boardarray[0][2]}')    # Logging printing with f-string type (Dereferencing/Accessing 2-d array values instead of string literals)
    # print(f'{boardarray[1][0]}|{boardarray[1][1]}|{boardarray[1][2]}')
    # print(f'{boardarray[2][0]}|{boardarray[2][1]}|{boardarray[2][2]}')

    
# Create PlayerMove fxn (indicate whether it's X or O)
def playermove(row,col,playericon):             # fxn def with multiple parameter
    # If last move was 'X' then do
    boardarray[row][col] = playericon


# def improvedwinconditions(boardarray):
#     outerboard = len(boardarray)
  
#     for i in outerboard:
#         innerboard = len(boardarray[i])
#         for j in innerboard:
#             if(boardarray[0][j+1] == 'X'):
#                 print("Winner")

# win function 
def winconditions():
   winbool = False
   if(boardarray[0][0] == 'X' and boardarray[0][1] == 'X' and boardarray[0][2] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[1][0] == 'X' and boardarray[1][1] == 'X' and boardarray[1][2] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[2][0] == 'X' and boardarray[2][1] == 'X' and boardarray[2][2] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[0][0] == 'X' and boardarray[1][0] == 'X' and boardarray[2][0] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[0][1] == 'X' and boardarray[1][1] == 'X' and boardarray[2][1] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[0][2] == 'X' and boardarray[1][2] == 'X' and boardarray[2][2] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[0][0] == 'X' and boardarray[1][1] == 'X' and boardarray[2][2] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
   elif(boardarray[0][2] == 'X' and boardarray[1][1] == 'X' and boardarray[2][0] == 'X'):
       print("Player 1 wins")
       winbool = True
       return winbool
       
   elif(boardarray[0][0] == 'O' and boardarray[0][1] == 'O' and boardarray[0][2] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[1][0] == 'O' and boardarray[1][1] == 'O' and boardarray[1][2] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[2][0] == 'O' and boardarray[2][1] == 'O' and boardarray[2][2] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[0][0] == 'O' and boardarray[1][0] == 'O' and boardarray[2][0] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[0][1] == 'O' and boardarray[1][1] == 'O' and boardarray[2][1] == 'O'):
       print("Player 2 wins")       
       winbool = True
       return winbool
   elif(boardarray[0][2] == 'O' and boardarray[1][2] == 'O' and boardarray[2][2] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[0][0] == 'O' and boardarray[1][1] == 'O' and boardarray[2][2] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool
   elif(boardarray[0][2] == 'O' and boardarray[1][1] == 'O' and boardarray[2][0] == 'O'):
       print("Player 2 wins")
       winbool = True
       return winbool



# Create Player    
playericon = player.slayer()  #object created called playericon
# print(playericon.player1)
    
currentplayer = 1
gameisrunning = True #Flag is something that indicates a current state (what the program is going thru right now without having to check the program entirely)
#can be a BOOL value, or integer



# Single responsibility principle (watch video on it) 
#-> Classes fxns variables etc. in programming (building blocks of programming that we define) even if they dont exist in a class should only
#loop
while gameisrunning:                         #Infinite while loop implementation
   #render board
   renderboard(boardarray)

   #players prompt 
   row,col = input(f"Player {currentplayer} make move:").split()        # input/cleaning and player(user input) decisions using split method
   row = int(row)
   col = int(col)
   #validate player move (will take a look at the second conditional statement'DOESNT MAKE SENSE')
   if(row < 0 or row > 3 or col < 0 or col > 3) and (boardarray[row][col] != '_' or boardarray[row][col] != ' '):      #Attempt at conditional
       print("Invalid move")
   #add player move to board
   #encapsulate into fxn that handles entires player turn 
   if(currentplayer == 1): 
       playermove(row,col,playericon.player1)
       currentplayer = 2
   elif(currentplayer == 2): 
       playermove(row,col,playericon.player2) 
       currentplayer = 1
  
   
   #check win conditions
   
   winbool = winconditions()
   if(winbool == True):
       gameisrunning = False
   #check draw conditions
#   break                                              # Conditional break

#icebox features
# draw conditions
# have game not replace "_" with player icon
# ask if it wants to play again (set back to default board[keep track of default board])
# Modify while loop and if they want to reset the board.