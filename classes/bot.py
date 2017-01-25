from configparser import *

class BJBot:
    
    def __init__(self):
        """
        Initialize empty bot. The bot works as the players i.e. by heuristics
        set by the user of the program. There are other classes for ML and the
        dealer.
        """
        pass
    
    
    def configure(self):
        """
        Configure the bot with the parameters specified in the bot config file.
        """
        config = ConfigParser()
        config.read('bot_config.ini')
        self.money = int(config['Bot']['Money'])
        self.limit = int(config['Bot']['Limit'])
        
    def action(self,player_cards,player_sum):
        """
        Performs an action based on the bot's policy and the provided variables.
        
        type player_cards:
        param player_cards:
        
        type player_sum
        param player_sum 
        """
        
        action = 'NONE'
        if player_sum < self.limit:
            action = 'hit'
            return action, 0
        else:
            action = 'stay'
            return action, 0
        
        
        