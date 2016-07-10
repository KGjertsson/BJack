from configparser import *

class BJBot:
    
    def __init__(self):
        print('jag är en bot, varför finns jag?')
    
    
    def configure(self):
        config = ConfigParser()
        config.read('bot_config.ini')
        test = config['Bot']['TestMoney']
        # add suitable values
        
    def action(self,player_cards,player_sum):
        action = 'NONE'
        if player_sum < 17:
            action = 'hit'
            return action, 0
        else:
            action = 'stay'
            return action, 0
        
        
        