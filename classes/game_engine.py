from configparser import *

from .players import Player
from .players import Dealer
from .deck import Deck
from .bot import BJBot

class GameEngine:
    
    def __init__(self,):

        self.players_count=-1
        self.max_bet = -1
        self.min_bet = -1
        self.n_decks = -1
        self.round_shuffle = -1
        self.dealer_take_limit = [-1, -1]
        self.player_start_money = -1
        self.player_turn = -1
        
        
#        self.round_number=1    
        
        self.players = []
        
        self.dealer = Dealer()
        


        
    def read_config(self):
        
        config = ConfigParser()
        config.read('config.ini')
        self.players_count=int(config['Black Jack']['PlayersCount'])
        self.max_bet = int(config['Black Jack']['MaxBet'])
        self.min_bet = int(config['Black Jack']['MinBet'])
        self.n_decks = int(config['Black Jack']['Decks'])
        self.round_shuffle = int(config['Black Jack']['RoundShuffle'])
        
        self.dealer_take_limit[0] = int(config['Black Jack']['DealerTakeLowerLimit'])
        self.dealer_take_limit[1] = int(config['Black Jack']['DealerTakeUpperLimit']) 
        print (self.dealer_take_limit[1])
        self.player_start_money = int(config['Black Jack']['StartMoney'])
    
    def create_players(self):
        for i in range(self.players_count):
            self.players.append(Player(self.player_start_money))
        return len(self.players)
    
    def hit(self,player_index):
        self.players[player_index].give_card(self.deck.pull_card())
        if self.players[player_index].calc_sum() > 21:
            self.players[player_index].lose()
            self.player_turn +=1
        return player_index, self.players[player_index].state, self.players[player_index].hand, self.players[player_index].calc_sum()
            
    def bet(self,player_index,money):
        self.players[player_index].bet_money += money              
        #maybe check money is enough or something else throw error back
        
    def stay(self,player_index):
        self.player_turn +=1
        return self.player_turn
        
    def initialize_board(self):
        self.deck = Deck(self.n_decks)
        self.player_turn = -1
    
    def deal_cards(self):
        x=0
        while (x < 2):
            current_card = self.deck.pull_card()
            self.dealer.give_card(current_card)
            for i in range(len(self.players)):
                current_card = self.deck.pull_card()
                self.players[i].give_card(current_card)
                x+=1
                    

      
    def round_end(self):
        #Deal to dealer and check win conditions
        dealer_sum = self.dealer.calc_sum()
        while dealer_sum < self.dealer_take_limit[0]:
            self.dealer.give_card(self.deck.pull_card())
            dealer_sum = self.dealer.calc_sum()
        if dealer_sum > 21:
            for i in range(len(self.players)):
                self.players[i].win(self.players[i].blackjack)
                self.save_stats(i,'win',self.players[i].blackjack)
        else:
               for i in range(len(self.players)):
                   player_sum = self.players[i].calc_sum()
               
               if dealer_sum == player_sum:
                   if player_sum < self.dealer_take_limit[1]:
                       self.players[i].lose()
                       self.save_stats(i,'lose')
                   else:
                       self.players[i].even()
                       self.save_stats(i,'even')
               else:
                   if player_sum > dealer_sum:
                       self.players[i].win(self.players[i].blackjack)
                       self.save_stats(i,'win',self.players[i].blackjack)
                   else:
                       self.players[i].lose()
                       self.save_stats(i,'lose')
                       

    def save_stats(self,player_index,event,blackjack=False,card=-1,turn_id=-1):
        if event == 'win':
            pass
        elif event == 'lose':
            pass
        elif event == 'hit':
            pass
        elif event == 'stay':
            pass
                    
        
    def new_round(self):
        
        self.player_turn = -1
        if self.round_shuffle == 1:
            self.deck = Deck(self.n_decks)
        else:
            if not self.deck.cards:
                self.deck = Deck(self.n_decks)
        
        self.dealer.clear_hand()   
        for i in range(len(self.players)):
            self.players[i].clear_hand()            
            self.players[i].state = 'NONE'
            

        
             
        

        
        
        