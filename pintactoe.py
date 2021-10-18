from random import randrange

# Starting variables 
board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
numberofmoves = 1
human = "O"
computer = "X"

# Function's created below
def DisplayBoard(board):
    print("\n+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")    
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")    
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+\n\n")
def EnterMove(board):
    while True:        
      try:
        move = int(input("Please pick a square to by typing a number from the board 1-9: "))
        if move < 1 or move > 9:
          print("\n\nERROR: Invalid entry\n\n")
          continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
          print("\n\nSorry that square is taken already!\nPlease select a different square\n\n")
          continue
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = "O"
        break
      except ValueError:
          print("\n\nERROR: Invalid entry  (no letters, numbers only)\n\n")
def MakeListOfFreeFields(board):
    global free_squares
    free_squares = []
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == "X" or board[row][column] == "O":
                pass
            else:
                free_squares.append(([row],[column]))
    print()
def VictoryFor(board, sign):  
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True
    else:
        print()
def DrawMove(board):
    while True:
        row = randrange(3)
        column = randrange(3)
        if ([row],[column]) not in free_squares:
            continue
        else:
            board[row][column] = "X"
            return
def IntChecker(board):
  global yesorno
  if yesorno == "1":
    print("\n\nChallenge ACCEPTED - Let's begin\n\n")
  elif yesorno == "0":
    print("\n\nChallenge DENIED - Arcade Power Down...\nTomorrow is another day. Goodbye for now.")
    exit()
  else:
    print("\nERROR: Invalid Entry\nPlease enter valid response (1 or 0)")
    yesorno = input("\n(Type 1 for Yes and Type 0 for No): \n")
    if yesorno == "1":
      print("Challenge ACCEPTED - Let's begin\n\n")
    elif yesorno == "0":
      print("\n\nChallenge DENIED - Arcade Power Down...\nTomorrow is another day. Goodbye for now.")
      exit()
    else:
      print("\nFINAL ERROR: Invalid Entry\nPlease enter valid response (1 or 0) or system will SHUT DOWN")
      yesorno = input("\n(Type 1 for Yes and Type 0 for No): \n")
      if yesorno == "1":
        print("Challenge ACCEPTED - Let's begin\n\n")
      elif yesorno == "0":
        print("\n\nChallenge DENIED - Arcade Power Down...\nTomorrow is another day. Goodbye for now.")
        exit()
      else:
        print("\n\n\n3 Invalid Attempts - System is shutting down.\nGoodbye for now. ")
        exit()  
def StartGame(board):
  global yesorno
  global name
  print('___________________________________________________________\n')
  print("Arcade App Idea: GAMERS DAILY CHALLENGE (powered by Python)\nCreated by: Daniel Pinto")
  print('___________________________________________________________')
  name = input("\nYour Name: ")
  print('\n.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .\n')
  print("\nGreetings " + str.capitalize(name) + ",\nMy creators refer to me as Beep-Bop the 3rd")
  print("\n\nToday's challenge is a friendly game of Tic Tac Toe") 
  print("\n\nDo you accept the challenge?")
  yesorno = input("(Type 1 for Yes and Type 0 for No): ")
  print('\n. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n')
  

StartGame(board)
IntChecker(board)
print("Here is the current board with CPU starting X at square 5")
DisplayBoard(board)

while numberofmoves < 9:
  EnterMove(board)
  numberofmoves += 1
  DisplayBoard(board)

  if VictoryFor(board, human) == True:
    print("You CRUSHED the computer! You are a super human! Woot woot!")
    break
  else:
    MakeListOfFreeFields(board)
    print()
  print("Time for the computer to make its move!\n\n\n")
        
  DrawMove(board)
  numberofmoves += 1
  DisplayBoard(board)
  
  if numberofmoves == 9:
    continue

  if VictoryFor(board, computer) == True:
    print("Beep-Bop the 3rd has OUTSMARTED you " + str.capitalize(name) + "! Better luck next time!")
    break
  else:
    MakeListOfFreeFields(board)
    print("Now it is time for you to make another move!\n")
else:
  print("We have a cat's game (it's a tie)!!!")
    
print("\n\nThank you for playing! Rerun the program for a rematch")



