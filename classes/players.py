# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:47:06 2016

@author: yihan
"""

from card import Card
from numpy import *

class Dealer:
    
    current_hand=-1;
    def __init__(self):
        self.current_hand=zeros(1,22)


class Player:
    
    current_hand=-1;
    def __init__(self,player_count):
        self.current_hand=zeros(1,22)
    def giveCard(card):
        self.current_hand.append(card)
    
    
    def clearHand(self):
        self.current_hand=[]
        
    def money(self,number):
        1=1
    
    