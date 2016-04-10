# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:47:06 2016
"""

from .card import Card
from numpy import *

class Dealer:
    
    hand = []
    
    def __init__(self):
        self.current_hand = []
        
    def giveCard(self, pulled):
        hand.append(pulled)
        
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
        
        if len(aces) > 0:
            for i in range(len(aces)):
                sum = sum + aces[i]
            if (sum > 21):
                done = 0
                while(done == 0):
                    for i in range(len(aces)):
                        if aces[i] == 13:
                            aces[i] == 1
                            sum = sum - 10
                            break
                    if sum <= 21:
                        done = 1
        return sum

class Player:
    
    hand = []
    
    def __init__(self,player_count):
        pass        
    
    def giveCard(self, card):
        self.hand.append(card)
    
    def clearHand(self):
        self.hand=[]
        
#    def money(self,number):
#        1=1
    
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
        
        if len(aces) > 0:
            for i in range(len(aces)):
                sum = sum + aces[i]
            if (sum > 21):
                done = 0
                while(done == 0):
                    for i in range(len(aces)):
                        if aces[i] == 13:
                            aces[i] == 1
                            sum = sum - 10
                            break
                    if sum <= 21:
                        done = 1
        return sum