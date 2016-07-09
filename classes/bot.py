from configparser import *

class BJBot:
    
    def __init__(self):
        print('jag är en bot, varför finns jag?')
    
    
    def configure(self):
        config = ConfigParser()
        config.read('bot_config.ini')
        test = config['Bot']['TestMoney']
        # add suitable values
        