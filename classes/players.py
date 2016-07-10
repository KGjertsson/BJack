from .card import Card
from numpy import *

class Dealer:

    def __init__(self):
        self.hand = []
        
    def give_card(self, pulled):
        self.hand.append(pulled)
        
    def calc_sum(self):
        sum = 0
        aces = []
        for i in range(len(self.hand)):
            if hand[i].value == 1:
                aces.append[13]
            elif hand[i].value > 10:
                sum = sum + 10
            else:
                sum = sum + hand[i].value
        if len(aces) > 0:
          low = aces*1 
          high = 11+(aces-1)*1
          if sum+high > 21:
              sum+=low
          else:
              sum+=high
        return sum
        
    def clear_hand(self):
        self.hand=[]


class Player:
    
    def __init__(self,player_start_money):
        self.money=player_start_money
        self.bet_money=0
        self.state = 'NONE' #Can be none, won, lost
        self.hand=[]
        self.blackjack=False
    
    def give_card(self, card):
        self.hand.append(card)
    
    def clear_hand(self):
        self.hand=[]
        self.blackjack=False
        
    def lose(self):
        #WE FUCKING LOST
        self.money -= self.bet_money
        self.state = 'LOST'
        
        
    def win(self,blackjack):
        #WE FUCKING won
        if blackjack == True:
            self.money += self.bet_money*1.5
            self.state = 'WON'  
        else:
            self.state = 'WON' 
            self.money += self.bet_money
            
    def even(self):
        self.bet_money = 0
        self.state = 'EVEN'

        
    def hit_or_stay(self):
        return True
        
    def calc_sum(self):
        sum = 0
        aces = 0
        for i in range(len(self.hand)):
            if self.hand[i].value == 1:
               aces+=1
               
            elif self.hand[i].value > 10:
                sum = sum + 10
            else:
                sum = sum + self.hand[i].value
        
        if aces > 0:
          low = aces*1 
          high = 11+(aces-1)*1
          if sum+high > 21:
              sum+=low
          else:
              sum+=high
              
        if sum == 21:
            if len(self.hand) == 2:
                self.blackjack=True
                    
        return sum
    