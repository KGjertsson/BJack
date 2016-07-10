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
        player_turn, player_cards, player_sum = engine.turn_handler()
        
        while player_turn < len_players-1:
            print('before turnhandler',player_turn)
            
            player_turn, player_cards, player_sum = engine.turn_handler() 
            
            print('after turnhandler',player_turn)
            action, bet_amount = mr_jack[player_turn].action(player_cards,player_sum)
            print(action)
            
            if action == 'hit':
                engine.hit(player_turn)
            else:
                player_turn=engine.stay(player_turn)
        
        round_end_stats = engine.turn_handler()        
        
        round_id +=1
    
#    
#    for i in range(len_players):
#        bet_amount=mr_jack[i].bet() #do calculation on how much we should bet, no info of cards at bet in game only remember old infos
#        engine.bet(i,bet_amount)
#        
 
    
    
    
     
    
    
    yalla = WallA()
    
