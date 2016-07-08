#from classes.card import Card
#from classes.deck import Deck
from classes.gameEngine import GameEngine
from classes.bot import jack
import tkinter as tk
import tkinter as tk


if __name__ == "__main__":
    engine = GameEngine()
    engine.readConfig()
    engine.createPlayers()
    bot = jack()
