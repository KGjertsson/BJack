# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import configparser
from .card import Card
from .players import Players
from .deck import Deck

class GameEngine:

    def __init__(self,):
        self.players_count=-1
        self.max_bet = -1
        self.min_bet = -1
        self.decks = -1
        self.round_shuffle = -1
        self.dealer_take_limit = -1
        
        self.round_number=1        
        
        self.readConfig()
        self.createPlayers()

        
    def readConfig(self):
        config = config.ConfigParser()
        config.read('config.ini')
        self.players_count=config['Black Jack']['PlayersCount']
        self.max_bet = config['Black Jack']['MaxBet']
        self.min_bet = config['Black Jack']['MinBet']
        self.decks = config['Black Jack']['Decks']
        self.round_shuffle = config['Black Jack']['RoundShuffle']
        self.dealer_take_limit = config['Black Jack']['DealerTakeLimit']
    
    def createPlayers(self):
        for i in range(self.players_count):
            self.player[i]=self.Player()
    
    def hit(self,player_index):
        (value,suite) = self.Deck.pullCard()
        
        self.player[player_index].giveCard(Card(value,suite))        
      
    
    def stay(self,player_index):
        self.nextTurn(self)
    
        
    def nextTurn(self):
        '''
        0 = dealer        
        1 to n = player ID
        '''
        
    def newRound(self):
        pass
        
    def bet(self):
        pass