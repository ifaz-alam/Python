class Player:
  def __init__(self, cash, dealer=False):
    self.cash = cash
    self.cards = [] #stores the cards
    self.sum = 0 # sum of card values

class card:
  def __init__(self,filename,value, label=None):
    self.filename = filename
    self.value = value
    self.label = label
