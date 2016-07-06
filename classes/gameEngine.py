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

        self.players_count=-1
        self.max_bet = -1
        self.min_bet = -1
        self.nDecks = -1
        self.round_shuffle = -1
        self.dealer_take_limit = -1
        self.player_start_money = -1
        
        self.turn_id=0
        
        self.round_number=1    
        
        self.players = []
        self.deck = Deck(self.nDecks)
        self.dealer = Dealer()
        
        self.readConfig()
        self.createPlayers()

        
    def readConfig(self):
        config =[]
        
        config = config.ConfigParser()
        config.read('config.ini')
        self.players_count=config['Black Jack']['PlayersCount']
        self.max_bet = config['Black Jack']['MaxBet']
        self.min_bet = config['Black Jack']['MinBet']
        self.nDecks = config['Black Jack']['Decks']
        self.round_shuffle = config['Black Jack']['RoundShuffle']
        self.dealer_take_limit = config['Black Jack']['DealerTakeLimit']
        self.player_start_money = config['Black Jack']['StartMoney']
    
    def createPlayers(self):
        for i in range(self.players_count):
            self.players.append(Player(self.player_start_money))
    
    def hit(self,player_index):
        self.players[player_index].giveCard(self.Deck.pullCard())
        if self.players[player_index].calcSum() > 21:
            self.players[player_index].lose()
           
        
#    def stay(self,player_index):
#        self.nextTurn()
        
    def startTurns(self):

        for i in range(self.players):       
            stay = False
            stay=self.bot.hitOrStay(i)
            while stay == False:
                self.hit(i)
                stay=self.bot.hitOrStay(self.players.calcSum()) #Bot class not created yet
                
        dealer_sum = self.dealer.calcSum()
        while dealer_sum < self.dealer_take_limit[0]:
            self.dealer.giveCard(self.deck.pullCard())
            dealer_sum = self.dealer.calcSum()
        
        if dealer_sum > 21:
            for i in range(self.players):
                    self.players[i].win(self.players[i].blackjack)
        else:
            for i in range(self.players):
                player_sum = self.players[i].calcSum()
                
                if dealer_sum == player_sum:
                    if player_sum < self.dealer_take_limit[1]:
                        self.players[i].lose()
                    else:
                        self.players[i].even()
                else:
                    if player_sum > dealer_sum:
                        self.players[i].win(self.players[i].blackjack)
                    else:
                        self.players[i].lose()
                
                        
                        
                    
        
    def newRound(self):
        self.round_id = 0
        if self.round_shuffle == 1:
            self.deck = Deck(self.nDecks)
        else:
            if not self.deck.card:
                self.deck = Deck(self.nDecks)
            
        for i in range(self.players):
            self.players[i].clearHand()
            self.dealer.clearHand()
            self.players[i].lost = 0
            self.players[i].won = 0
            
            #REQUIRE BOT ATTENTION CODE HERE
            #bet?
            
            self.players[i].bet(self.Bot.bet)
            
            
        x=0
        while (x < 2):
            self.dealer.giveCard(self.deck.pullCard)
            for i in range(self.players):
                self.players[i].giveCard(self.deck.pullCard)
            x+=1
        
        #REQUIRE BOT ATTENTION CODE HERE
        #double? split? +13 -13?
        self.players[i].bet(self.Bot.newRoundAction)
        
        self.startTurns()
        
        
        

        