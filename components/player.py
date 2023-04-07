from components.token import Token
import random
import pygame
from components.yut import YutGame

class Player:
    def __init__(self, board, token):
        self.board = board
        self.token = token  # the tiger token is always the first in the list
        self.moves = 0
   
    def play(self, yut_game):
        yut_game.flip_all_yuts()
        yut_game.count_yuts_front()
        # // flip yut one more when it is yut or mo
        self.moves = yut_game.decide_moves()
        self.token.move(self.moves)
        # if self.game.one_more == True:
        #     yut_game.flip_all_yuts()   
        #     yut_game.count_yuts_front()
        #     # // flip yut one more when it is yut or mo
        #     self.moves = yut_game.decide_moves()
        #     self.token.move(self.moves)
        #     self.game.one_more = False
## flicking back to button 
     
