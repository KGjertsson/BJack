#from classes.card import Card
#from classes.deck import Deck
from classes.gameEngine import GameEngine
from classes.walla import WallA
import tkinter as tk
import tkinter as tk


if __name__ == "__main__":
    engine = GameEngine()
    engine.readConfig()
    engine.createPlayers()
    engine.initialize_board()
    
    yalla = WallA()
    
