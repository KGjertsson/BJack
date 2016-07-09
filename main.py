#from classes.card import Card
#from classes.deck import Deck
from classes.game_engine import GameEngine
from classes.walla import WallA
from classes.bot import BJBot
import tkinter as tk


if __name__ == "__main__":
    engine = GameEngine()
    
    engine.read_config() #Maybe read configs in main and send variables in engine=GameEngine(variables)??
    len_players=engine.create_players()
    mr_jack=[]
    
    for i in range(len_players):
        mr_jack.append( BJBot() )#  BLOWJOB BOT
        mr_jack[i].configure()
    
    ###################################################
    ########### START THIS PIECE OF SHIT GAME #########
    ###################################################
    engine.initialize_board()
    round_id = 0
    max_rounds = 100 # TEMPORARY LIMIT, 
    while round_id < max_rounds:
        
        engine.new_round()
        player_turn, player_cards, player_sum = engine.turnhandler()

        while player_turn < len_players:
        
            player_turn, player_cards, player_sum = engine.turnhandler()    
            action, bet_amount = mr_jack[player_turn].ation(player_cards,player_sum)
            if action == 'bet':
                engine.Bet(player_turn,bet_amount)
            else:
                player_turn=engine.Stay(player_turn)
        round_id +=1
    
#    ########## BETTING HERE ###########################
#    for i in range(len_players):
#        bet_amount=mr_jack[i].bet() #do calculation on how much we should bet, no info of cards at bet in game only remember old infos
#        engine.bet(i,bet_amount)
#        
 
    
    
    
     
    
    
    yalla = WallA()
    
