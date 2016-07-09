from configparser import *
from .card import Card
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
        
        self.hit_no=0
        
        self.round_number=1    
        
        self.players = []
        self.deck = Deck(self.n_decks)
        self.dealer = Dealer()
        
        # i thinkg it's a bit weird to have this here, probably clearer to 
        # call them separately from main
        
        # self.read_config()
        # self.create_players()

        
    def read_config(self):
        
        config = ConfigParser()
        config.read('config.ini')
        self.players_count=config['Black Jack']['PlayersCount']
        self.max_bet = config['Black Jack']['MaxBet']
        self.min_bet = config['Black Jack']['MinBet']
        self.n_decks = config['Black Jack']['Decks']
        self.round_shuffle = config['Black Jack']['RoundShuffle']
        self.dealer_take_limit = [map(int, x) for x in config['Black Jack']['DealerTakeLimit']]
        self.player_start_money = config['Black Jack']['StartMoney']
    
    def create_players(self):
        for i in range(len(self.players_count)):
            self.players.append(Player(self.player_start_money))
    
    def hit(self,player_index):
        self.players[player_index].giveCard(self.Deck.pullCard())
        if self.players[player_index].calcSum() > 21:
            self.players[player_index].lose()
           
        
#    def stay(self,player_index):
#        self.nextTurn()
        
    def initialize_board(self):
        #Starting turns, loop through players, give them choice to do
        for i in range(len(self.players)):

            ###################################################
            # CHANGE STUFF HERE, BOT IS WRONGLY ASSIGNED!!!!! #           
            ###################################################

            bot = self.players[i]            
            stay=False
            while True:
                stay=bot.hit_or_stay() #Bot class not created yet
                if stay:
                    break
                else:
                    self.hit(i) 
                    
        #After all players done, do dealer -- in the butt        
        dealer_sum = self.dealer.calc_cum()
        while dealer_sum < self.dealer_take_limit[0]:
            self.dealer.give_card(self.deck.pull_card())
            dealer_sum = self.dealer.calc_sum()
        
        #Check wins and losses
        if dealer_sum > 21:
            for i in range(self.players):
                    self.players[i].win(self.players[i].blackjack)
                    self.save_stats(i,'win',self.players[i].blackjack)
        else:
            for i in range(self.players):
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
        self.round_id = 0
        if self.round_shuffle == 1:
            self.deck = Deck(self.n_decks)
        else:
            if not self.deck.card:
                self.deck = Deck(self.n_decks)
            
        for i in range(self.players):
            self.players[i].clear_hand()
            self.dealer.clear_hand()
            self.players[i].lost = 0
            self.players[i].won = 0
            
            #REQUIRE BOT ATTENTION CODE HERE
            #bet how much?
            ##
            self.players[i].bet(self.Bot.bet)
            ##
            
        x=0
        while (x < 2):
            self.dealer.give_card(self.deck.pull_card)
            for i in range(self.players):
                self.players[i].give_card(self.deck.pull_card)
            x+=1
        
        #REQUIRE BOT ATTENTION CODE HERE
        #double? split? +13 -13? no action?
        self.players[i].bet(self.Bot.new_round_action)
        
        initialize_board()
        