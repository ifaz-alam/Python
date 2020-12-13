# imports the modules necessary for the program to function
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage
from Player import Player, card
import random


"""
Names: Ifaz Alam
Date: March 13, 2020
Description: BlackJack Program using Tkinter

NOTE:
It is recommended to run this program through IDLE as Tkinter on repl.it can be faulty at times. (Although opening repl.it through incognito sometimes works)
"""

# Blackjack game class
class Blackjack:
  def __init__(self, master):
    self.master = master
    master.title("Blackjack")

    # initializes list for player / dealer hand and deck
    self.hand = []
    self.dealer_hand = []
    self.deck = []
    
    # player and dealer objects
    self.player = Player(500) # starts the player with some money
    self.dealer = Player(0, dealer=True) # the dealer is also a 'Player' object

    # calls main menu function
    self.main_menu()
  

  # function that displays main menu  
  def main_menu(self):            
    # labels
    self.title_label = Label(text="♠ BlackJack ♠", width ='20', font=("Courier", 30))
    self.title_label.grid(row=0, column=0, pady=(10,5))
    
    self.cash_label = Label(text="You currently have $%.2f" % (self.player.cash), font=("Verdana", 20))
    self.cash_label.grid(row=1, column=0, pady=(0,10))

    self.wager_label = Label(text="Enter the amount you would like to wager", font=("Avant Garde",15), bg="Green", fg="White", width=35)
    self.wager_label.grid(row=2, column=0, pady=(10,10))

    self.warning_label = Label(text="", font=("Arial Black", 12), fg="Red")
    self.warning_label.grid(row=4, column=0, pady=(10,10))

    self.width_label = Label(width='100')
    self.width_label.grid(row=10,column=0)

    # wager entry field
    self.wager_entry = Entry(font=("Calibri", 30), justify='center')
    self.wager_entry.grid(row=3, column=0)

    # deal button
    self.deal_button = Button(text="Deal", font=("Georgia", 20), command=self.wager, state="active", width='20')
    self.deal_button.grid(row=5, column=0, pady = (5 ,40))


  # function for handling wager entry
  def wager(self):
    # gets value of user input
    self.wager_amount = self.wager_entry.get()

    # handles user input accordingly
    try:
      self.wager_amount = float(self.wager_amount)
      if self.wager_amount < 0:
        self.warning_label.config(text="You must enter a positive number!")
      elif self.wager_amount == 0:
        self.warning_label.config(text="You must enter a number greater than zero!") 
      elif self.wager_amount > self.player.cash:
        self.warning_label.config(text="You cannot wager more than you currently have!")  
      else:
        # destroys previous widgets
        self.title_label.grid_forget()
        self.cash_label.grid_forget()
        self.wager_label.grid_forget()
        self.warning_label.grid_forget()
        self.wager_entry.grid_forget()
        self.deal_button.grid_forget()
        
        # calls the deal function
        self.deal()
    except:
      self.warning_label.config(text = "You must enter a positive number!")      


  # function for creating new deck of cards    
  def set_cards(self):
    for letter in ["C","D","H","S"]:
      for number in range(1,14):
        filename = "cards//%s%s.png" % (number,letter)
        # Jacks, Kings, and Queens have a value of 10
        if number > 10:
          value = 10
        else:
          value = number
        # adds cards to deck
        self.deck.append(card(filename,value))
    # shuffles the deck
    random.shuffle(self.deck)


  # function for dealing cards
  def deal(self):
    # frames
    self.dealer_frame = Frame()
    self.dealer_frame.grid(row=0, column=0)
    
    self.player_frame = Frame()
    self.player_frame.grid(row=1, column=0)
    
    self.buttons_frame = Frame()
    self.buttons_frame.grid(row=2, column=0)

    # labels
    self.spacing_top_label = Label(self.player_frame, text="")
    self.spacing_top_label.grid(row=1, column=0)
    
    self.spacing_bottom_label = Label(self.dealer_frame, text="")
    self.spacing_bottom_label.grid(row=0, column=0)

    # buttons
    self.hit_button = Button(self.buttons_frame, text="Hit", font=("Arial Black",10), command=self.player_hit, state="active")
    self.hit_button.grid(row=0, column=0)
    
    self.stand_button = Button(self.buttons_frame, text="Stand", font=("Arial Black",10), command=self.revealCard, state="active")
    self.stand_button.grid(row=1, column=0)
    
    # creates shuffled deck of cards
    self.set_cards()

    # gives player and dealer two cards each
    self.player.sum = self.new_card()
    self.player.sum = self.new_card()
    
    self.dealer.sum = self.new_card_dealer()
    self.dealer.sum = self.new_card_dealer()

    # dealer's hidden card
    self.photo = PhotoImage(file = "cards//hidden.png")
    self.hidden_card_label = Label(self.dealer_frame, image=self.photo)
    self.hidden_card_label.photo = self.photo
    self.hidden_card_label.grid(row=1, column=1, pady=(0,20))


  # function for revealing dealer's hidden card
  def revealCard(self):
    # reveals the hidden card
    self.hidden_card_label.grid_forget()

    # game tie
    if self.dealer.sum == self.player.sum:
      self.tie()
    
    # dealer wins
    elif self.dealer.sum > self.player.sum:
      self.lose()

    # dealer hits
    else:
      self.master.after(2000,self.dealer_hit)


  # function for Player drawing new card
  def new_card(self):
    sum = 0
    
    # takes card out of deck and puts it in hand
    new = self.deck[0]
    self.hand.append(new)
    self.deck.pop(0)

    # displaying card image to screen
    photo = PhotoImage(file = new.filename)
    new.label = Label(self.player_frame, image=photo)
    new.label.photo = photo

    # refresh the screen and adds an image for each card
    for card in self.hand:
      # dual ace functionality
      if card.value == 1:
        if self.player.sum + 10 <= 21:
          card.value = 10
          sum += card.value
        else:
          card.value = 1
          sum += card.value
      else:
        sum += card.value
        
      # displays player's cards side by side
      card.label.grid(row=0, column=self.hand.index(card))
    
    # updates player's sum
    return sum


  # function for Dealer drawing new card
  def new_card_dealer(self):
    sum = 0
    
    # takes card out of deck and puts it in hand
    new = self.deck[0]
    self.dealer_hand.append(new)
    self.deck.pop(0)

    # displaying card image to screen
    photo = PhotoImage(file = new.filename)
    new.label = Label(self.dealer_frame, image=photo)
    new.label.photo = photo

    # refresh the screen and adds an image for each card
    for card in self.dealer_hand:
      # dual ace functionality
      if card.value == 1:
        if self.dealer.sum + 10 <= 21:
          card.value = 10
          sum += card.value
        else:
          card.value = 1
          sum += card.value
      else:
        sum += card.value
          
      # displays dealer's cards side by side
      card.label.grid(row=1, column=self.dealer_hand.index(card), pady=(0,20))

    # updates dealer's sum
    return sum


  # function for player hit
  def player_hit(self):
    # draws new card from deck
    self.player.sum = self.new_card()

    # checks if player busts
    if self.player.sum > 21:
      self.lose()


  # recursive function for dealer hit
  def dealer_hit(self):
    # draws new card from deck
    self.dealer.sum = self.new_card_dealer()

    # game tie
    if self.dealer.sum == self.player.sum:
      self.tie()

    # dealer wins
    elif self.dealer.sum > self.player.sum and self.dealer.sum <= 21:
      self.lose()

    # dealer busts
    elif self.dealer.sum > 21:
      self.win()

    # dealer hits
    else:
      self.master.after(2000,self.dealer_hit)

      
  # function for when player wins
  def win(self):
    # destroys the hit and stand buttons
    self.hit_button.destroy()
    self.stand_button.destroy()

    # compares player's old and new balance
    self.results_label = Label(self.buttons_frame, text="YOU WIN!\nPrevious Balance: $%.2f\nNew Balance: $%.2f (+$%.2f×1.5)" % (self.player.cash, self.player.cash + self.wager_amount * 1.5, self.wager_amount), font=("Bahnschrift",20), fg = 'green')
    self.results_label.grid(row = 1, column=0)
    
    # player's new balance
    self.player.cash += self.wager_amount * 1.5
    
    # button for returning to main menu
    self.restart_button = Button(self.buttons_frame, text="Return to Main Menu", font=("Arial Black",10), command=self.reset, state="active")
    self.restart_button.grid(row=2, column=0, pady=(30,30))

  # function for when player loses 
  def lose(self):
    # destroys the hit and stand buttons
    self.hit_button.destroy()
    self.stand_button.destroy()

    # compares player's old and new balance
    self.results_label = Label(self.buttons_frame, text="YOU LOSE!\nPrevious Balance: $%.2f\nNew Balance: $%.2f (-$%.2f)" % (self.player.cash, self.player.cash - self.wager_amount, self.wager_amount), font=("Bahnschrift",20), fg = 'red')
    self.results_label.grid(row = 1, column=0)

    # player's new balance
    self.player.cash -= self.wager_amount

    # button for returning to main menu
    self.restart_button = Button(self.buttons_frame, text="Return to Main Menu", font=("Arial Black",10), command=self.reset, state="active")
    self.restart_button.grid(row=2, column=0, pady=(30,30))

  # function for game tie
  def tie(self):
    # destroys the hit and stand buttons
    self.hit_button.destroy()
    self.stand_button.destroy()

    # tie message
    self.results_label = Label(self.buttons_frame, text="IT'S A TIE!", font=("Bahnschrift",20), fg = 'yellow')
    self.results_label.grid(row = 1, column=0)

    # button for returning to main menu
    self.restart_button = Button(self.buttons_frame, text="Return to Main Menu", font=("Arial Black",10), command=self.reset, state="active")
    self.restart_button.grid(row=2, column=0, pady=(30,30))


  # function for resetting hands and deck
  def reset(self):
    # clears hands and deck
    self.hand.clear()
    self.dealer_hand.clear()
    self.deck.clear()

    # resets sum of cards
    self.player.sum = 0
    self.dealer.sum = 0

    # destroys card images and buttons
    self.dealer_frame.destroy()
    self.player_frame.destroy()
    self.buttons_frame.destroy()

    # calls main menu function
    self.main_menu()
    
root = Tk()
my_gui = Blackjack(root) #creates the instance
#root.geometry("640x480")
root.mainloop()
