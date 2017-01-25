from classes.game_engine import GameEngine
from classes.walla import WallA
from classes.bot import BJBot
from classes.stats import Stats
import tkinter as tk


if __name__ == "__main__":
    print('... initializing game engine')
    engine = GameEngine()
    engine.read_config() #Maybe read configs in main and send variables in engine=GameEngine(variables)??
    len_players=engine.create_players()
    mr_jack=[]
#    stats=Stats()
    
    for i in range(len_players):
        mr_jack.append(BJBot())#  BLOWJOB BOT
        mr_jack[i].configure()
    
    ###################################################
    ########### START THIS PIECE OF SHIT GAME #########
    ###################################################
    print('... initializing game')
        
    engine.initialize_board()
    round_id = 0
    max_rounds = 100 # TEMPORARY LIMIT, 
    while round_id < max_rounds:
        
        engine.new_round()
        player_turn = 0;
        
        while player_turn < len_players-1:

            
           
            

            action, bet_amount = mr_jack[player_turn].action(engine.players.hand, engine.players[player_turn].calc_sum())
            
            if action == 'hit':
                engine.hit(player_turn)
                stats.save_action(action,player_turn)
            else:
                player_turn=engine.stay(player_turn)
        
        for i in range(len_players):
            round_end_stats.players
            
        
        round_id +=1
    
#    
#    for i in range(len_players):
#        bet_amount=mr_jack[i].bet() #do calculation on how much we should bet, no info of cards at bet in game only remember old infos
#        engine.bet(i,bet_amount)
#        
 
    
    
    
     
    
    
    yalla = WallA()
    
