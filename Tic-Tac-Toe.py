"""
Name: Ifaz Alam
Date: May 8th, 2019
Description: ICS Game Production, Tic-Tac-Toe!
"""
#Modules
import random

#Counter variable for occupied coordinates
takenCoordinates = 0

computer = False
#Counter variable for score
playerOneScore = 0
playerTwoScore = 0
computerScore = 0

#List for grid coordinates
coordinate = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#Function for printing the Tic-Tac-Toe grid.
def grid(coordinate):
    print('       |       |')
    print('   ' + coordinate[1] + '   |   ' + coordinate[2] + '   |   ' + coordinate[3])
    print('       |       |')
    print('-----------------------')
    print('   ' + '    |  ' + '     |  ')   
    print('   ' + coordinate[4] + '   |   ' + coordinate[5] + '   |   ' + coordinate[6])
    print('       |       |')
    print('-----------------------')
    print('   ' + '    |  ' + '     |  ')  
    print('   ' + coordinate[7] + '   |   ' + coordinate[8] + '   |   ' + coordinate[9])
    print('   ' + '    |  ' + '     |  ')

#Initial screen when the program starts
def welcome():
  
  print("""
  ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
  ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
    ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  
    ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  
    ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
    ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
    """)
    
  welcome = int(input("Welcome to Tic-Tac-Toe!\n1) Play\n2) Instructions\n3) Leave Game\n>> "))
  if (welcome == 1):
    modeSelection()


  elif (welcome == 2):
    print("""
  Tic-Tac-Toe is a game where players take turns placing either an X, or an O on a
  3x3 grid. The objective is to successfully place three of your marks in a
  vertical, horizontal, or diagonal direction to win. If all the coordinates are
  occupied and there is no winner, it is a tie.

  Note: In Tic-Tac-Toe, X always goes first.

      """)
    begin = input("When you are ready to begin, type 'start'\n>> ")
    if (begin == 'start'):
      modeSelection()

#Function for gamemode selection           
def modeSelection():
  gamemode = int(input("\nHow would you like to play?\n1) Player versus Computer\n2) Player versus Player\n>> "))
  #Player versus Computer
  if (gamemode == 1):
    player_vs_computer()

  #Player versus Player
  elif (gamemode == 2):
    player_vs_player()
        
  else:
    print("Invalid entry, please try again!")
    modeSelection()

#Function for checking if a mark appears three times in a row in a certain direction
def winner(coordinate,mark):
    #Diagonally, top-left to bottom-right
    return ((coordinate[1] == mark and coordinate[5] == mark and coordinate[9] == mark) or

    #Diagonally, top-right to bottom-left
    (coordinate[3] == mark and coordinate[5] == mark and coordinate[7] == mark) or
    
    #Horizontally, top row
    (coordinate[1] == mark and coordinate[2] == mark and coordinate[3] == mark) or

    #Horizontally, middle row
    (coordinate[4] == mark and coordinate[5] == mark and coordinate[6] == mark) or

    #Horizontally, bottom row
    (coordinate[7] == mark and coordinate[8] == mark and coordinate[9] == mark) or

    #Vertically, left column
    (coordinate[1] == mark and coordinate[4] == mark and coordinate[7] == mark) or

    #Vertically, middle column
    (coordinate[2] == mark and coordinate[5] == mark and coordinate[8] == mark) or

    #Vertically, right column
    (coordinate[3] == mark and coordinate[6] == mark and coordinate[9] == mark))

#Function for placing a mark on the grid
def placeMark(position, mark):
  coordinate[position] = mark

def player_vs_computer():
  global takenCoordinates, playerOneScore, computerScore, computer
	#resets count for occupied coordinates
  takenCoordinates = 0

  computer = True

	#clears the board, useful for when the user chooses to play again
  for x in range (0, len(coordinate)):
    coordinate[x] = " "

	#determines which player goes first
  first = random.randint(1,2)
  if (first == 1):
    print("\nPlayer 1 goes first!\n")
    grid(coordinate)
    playerOneMove()
  else:
    print("\nComputer goes first!\n")
    grid(coordinate)
    computerMove()

#Function for Player versus Player gamemode
def player_vs_player():
  global takenCoordinates, playerOneScore, playerTwoScore
	#resets count for occupied coordinates
  takenCoordinates = 0  


  #clears the board, useful for when the user chooses to play again
  for x in range (0, len(coordinate)):
    coordinate[x] = " "
        
  #determines which player goes first
  first = random.randint(1,2)
  if (first == 1):
    print("\nPlayer 1 goes first!\n")
    grid(coordinate)
    playerOneMove()
  else:
    print("\nPlayer 2 goes first!\n")
    grid(coordinate)
    playerTwoMove()

#Function that lets player one move
def playerOneMove():
  global takenCoordinates, playerOneScore, playerTwoScore, computer

  #when player two wins, ask if the user would like to play again
  if (winner(coordinate,'O')):
    playerTwoScore += 1
    print("Player 2 wins!\nThe score is %d - %d\n" % (playerOneScore, playerTwoScore))
    choice = input("Would you like to play again? (Y/N)\n>> ")

    if (choice == "Y"):
        player_vs_player()
    elif (choice == "N"):
      print("\nOk, see you next time! •ᴗ•\n\nMATCH SUMMARY: %d - %d" % (playerOneScore, playerTwoScore))

  #when the match is tied, ask if the user would like to play again
  elif (takenCoordinates == 9):
    if not winner(coordinate, 'X') or not winner(coordinate,'O'):
      choice = input("It's a tie!\n Would you like to play again? (Y/N)\n>> ")
      if choice == "Y":
        player_vs_player()
      elif choice == "N":
        print("\nOk, see you next time! •ᴗ•\n\nMATCH SUMMARY: %d - %d" % (playerOneScore, playerTwoScore))
  
  #allow player one to move if there is an available coordinate for their turn
  elif (" " in coordinate):
    position = int(input("\nPlayer 1, choose a position from 1-9: "))
    if (1 <= position <= 9 and coordinate[position] == " "):
      placeMark(position, 'X')
      grid(coordinate)
      takenCoordinates += 1
      if (computer == True):
        computerMove()
      elif (computer == False):
        playerTwoMove()
    
    #asks player one to select a different coordinate
    else:
      print("The square you have selected is not available!")
      playerOneMove()
      
def playerTwoMove():
  global takenCoordinates, playerOneScore, playerTwoScore

  #when player one  wins, ask if the user would like to play again
  if (winner(coordinate,'X')):
    playerOneScore += 1
    print("Player 1 wins!\nThe score is %d - %d\n" % (playerOneScore, playerTwoScore))
    choice = input("Would you like to play again? (Y/N)\n>> ")
    if (choice == "Y"):
        player_vs_player()
    elif (choice == "N"):
      print("\nOk, see you next time! •ᴗ•\n\nMATCH SUMMARY: %d - %d" % (playerOneScore, playerTwoScore))

  #when the match is tied, ask if the user would like to play again
  elif (takenCoordinates == 9):
    if not winner(coordinate, 'X') or not winner(coordinate,'O'):
      choice = input("Would you like to play again?(Y/N) ")
      if choice == "Y":
        player_vs_player()
      elif choice == "N":
        print("\nOk, see you next time! •ᴗ•\n\nMATCH SUMMARY: %d - %d" % (playerOneScore, playerTwoScore))
  
  #allow player two to move if there is an available coordinate for their turn
  elif (" " in coordinate):  
    position = int(input("\nPlayer 2, choose a position from 1-9: "))
    if (1 <= position <= 9 and coordinate[position] == " " and takenCoordinates < 9):
        placeMark(position, 'O')
        grid(coordinate)
        takenCoordinates += 1
        playerOneMove()
        
    #asks player one to select a different coordinate
    else:
      print("The square you have selected is not available!")    
      playerTwoMove()   
    
def computerMove():
  placeMark(random.randint(1,9), 'O')
  playerOneMove()

 
welcome()

