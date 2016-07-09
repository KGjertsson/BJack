#from classes.card import Card
#from classes.deck import Deck
from classes.game_engine import GameEngine
from classes.walla import WallA
from classes.bot import BJBot
import tkinter as tk


if __name__ == "__main__":
    engine = GameEngine()
    mr_jack = BJBot()
    mr_jack.configure()
    
    yalla = WallA()
    
