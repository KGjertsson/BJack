# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import configparser
from .card import Card
from .players import Player
from .players import Dealer
from .deck import Deck

class GameEngine:
    
    def __init__(self,):
        self.dealer = Dealer()
        self.players_count=-1
        self.max_bet = -1
        self.min_bet = -1
        self.nDecks = -1
        self.round_shuffle = -1
        self.dealer_take_limit = -1
        
        self.round_number=1        
        self.players = []
        self.deck = Deck(self.nDecks)
        self.dealer = Dealer()
        
        self.readConfig()
        self.createPlayers()

        
    def readConfig(self):
        config = config.ConfigParser()
        config.read('config.ini')
        self.players_count=config['Black Jack']['PlayersCount']
        self.max_bet = config['Black Jack']['MaxBet']
        self.min_bet = config['Black Jack']['MinBet']
        self.nDecks = config['Black Jack']['Decks']
        self.round_shuffle = config['Black Jack']['RoundShuffle']
        self.dealer_take_limit = config['Black Jack']['DealerTakeLimit']
    
    def createPlayers(self):
        for i in range(self.players_count):
            self.players.append(Player())
    
    def hit(self,player_index):
        self.players[player_index].giveCard(self.Deck.pullCard())
    
#    def stay(self,player_index):
#        self.nextTurn(self)
        
    def nextTurn(self):
        '''
        0 = dealer        
        1 to n = player ID
        '''
        
        dealerSum = self.dealer.calcSum()
        if dealerSum < self.dealer_take_limit[0]:
            self.dealer.giveCard(self.deck.pullCard())
            dealerSum = self.dealer.calcSum()
        
        for i in range(self.players_count):
            pass
        
        '''
        det är här som magin med boten ska ske, vi måste få in boten här på 
        något sätt
        '''
        
#    def newRound(self):
#        pass
        
#    def bet(self):
#        pass