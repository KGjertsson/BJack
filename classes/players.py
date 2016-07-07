# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:47:06 2016
"""

from .card import Card
from numpy import *

class Dealer:

    
    def __init__(self):
        self.hand = []
        
    def giveCard(self, pulled):
        self.hand.append(pulled)
        
    def calcSum(self):
        sum = 0
        aces = []
        for i in range(len(hand)):
            if hand[i].value == 1:
                aces.append[13]
            elif hand[i].value > 10:
                sum = sum + 10
            else:
                sum = sum + hand[i].value
        
        if aces > 0:
          low = aces*1 
          high = 11+(aces-1)*1
          if sum+high > 21:
              sum+=low
          else:
              sum+=high
                          
       
        return sum

class Player:
    
    
    def __init__(self,player_start_money):
        self.money=player_start_money
        self.bet_money=0
        self.lost = 0
        self.won = 0
        self.hand=[]
        self.blackjack=False
    
    def giveCard(self, card):
        self.hand.append(card)
    
    def clearHand(self):
        self.hand=[]
        self.blacjack=False
        
    def lose(self):
        #WE FUCKING LOST
        self.money -= self.bet_money
        self.lost = 1
        
    def win(self,blackjack):
        #WE FUCKINg won
        if blackjack == True:
            self.money += self.bet_money*1.5
            self.won = 1  
        else:
            self.won = 1
            self.money += self.bet_money
            
    def even(self):
        self.bet_money = 0
        
    def bet(self,money):
        self.bet_money += money      
        
    def calcSum(self):
        sum = 0
        aces = 0
        for i in range(self.hand):
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
    
    