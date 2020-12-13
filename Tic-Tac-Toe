"""
Name: Ifaz Alam
Date: May 8th, 2019
Description: Tic-Tac-Toe
"""
#Modules
import random, sys

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

    
#Function for placing a mark on the grid
def placeMark(position, mark):
    coordinate[position] = mark

"""
def tieCHECK():
"""
count = 0
def playerOneMove():
  global count
  if (Winner(coordinate,'O')):
    print("Player 2 wins")

  elif (count == 9):
    if not Winner(coordinate, 'X') or not Winner(coordinate,'O'):
      print("its a tie")
      sys.exit()
    
  elif (" " in coordinate):
    position = int(input("\nPlayer 1, choose a position from 1-9: "))
    if (1 <= position <= 9 and coordinate[position] == " "):
      placeMark(position, 'X')
      grid(coordinate)
      count += 1
      print(count)
      playerTwoMove()
    elif count == 9:
      if not Winner(coordinate, 'X') or not Winner(coordinate,'O'):
        choice = input("It's a tie! Would you like to play again?(Y/N)")
        if choice == "Y":
          Welcome()
        elif choice == "N":
          print("""
          
          """)
          print("Thank you for playing!")
    else:
      print("Square Taken")
      playerOneMove()


      
def playerTwoMove():
  global count
  if (Winner(coordinate,'X')):
    print("Player 1 wins ")
  elif (count == 9):
    if not Winner(coordinate, 'X') or not Winner(coordinate,'O'):
      choice = input("Would you like to play again?(Y/N) ")
      if choice == "Y":
        Welcome()
      elif choice == "N":
        print("Thank you for playing!")
  elif (" " in coordinate):  
    position = int(input("\nPlayer 2, choose a position from 1-9: "))
    if (1 <= position <= 9 and coordinate[position] == " " and count < 9):
        placeMark(position, 'O')
        grid(coordinate)
        count += 1
        print(count)
        playerOneMove()
    else:
      print("Square Taken")    
      playerTwoMove()   
    
#Function for Player versus Player gamemode
def player_vs_player():
    first = random.randint(1,10)
    
    if (1 <= first <= 5):
        print("\nPlayer 1 goes first!\n")
        grid(coordinate)
        playerOneMove()
        
    else:
        print("\nPlayer 2 goes first!\n")
        grid(coordinate)
        playerTwoMove()

#Function for checking if a mark appears three times in a row in a certain direction
def Winner(coordinate,mark):
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




#Function for gamemode selection           
def modeSelection():
  #try:
  gamemode = int(input("\nHow would you like to play?\n1) Player versus Computer\n2) Player versus Player\n>> "))
    #Player versus Computer
  if (gamemode == 1):
    grid()
    #Player versus Player
  elif (gamemode == 2):
    player_vs_player()
        
  else:
    print("Invalid entry, please try again!")
    modeSelection()
  #Asks
  """
  except:
    print("\nPlease enter a number\n")
    modeSelection()
"""
def Welcome():
  
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
    
Welcome()
