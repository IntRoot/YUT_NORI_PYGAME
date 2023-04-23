import pygame
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from components.board import YutNoriBoard
from components.textbox import TextBox
from components.button import Button
class Token:
    def __init__(self, width, height, image, player):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((1000, 800))
        self.board = YutNoriBoard(1000,800)
        self.current_position = (650,600) ##start position
        self.current_position_idx = 0
        self.in_game = False
        self.winner =''
        self.player = player
        self.image =  pygame.transform.scale(pygame.image.load(os.path.join(parent_dir, 'images', image) ), (75, 75)) 
        
        

    

    def move(self, moves):
        print(moves, self.player)
        # Move the token based on the number of moves given
        print('moved from', self.current_position)
        if self.current_position not in self.board.piece_positions or self.current_position == (150,100) or self.current_position == (650,100):
            print('shortcut')

            # Token is at an event position
            if self.current_position == (400, 350):
                print('center')
                self.current_position_idx = self.board.left_diagonal.index((400, 350))
                if (self.current_position_idx - moves+1) <= 0:
                        ## end of left diagonal path is start point(goal position)
                    self.winner = self.player
                    return self.winner
                else:
                ## if token arrived at center, it takes left diagonal route 
                    self.current_position = self.board.left_diagonal[self.current_position_idx-moves]

            elif self.current_position in self.board.right_diagonal:
                # token is in right diagonal route
                self.current_position_idx = self.board.right_diagonal.index(self.current_position)
                if (self.current_position_idx) < moves:
                    # if token will reache the end of right diagonal route (left bottom corner, 150,600), and past to original path agan
                    lefted_moves=moves-(self.current_position_idx+1)
                    print(lefted_moves)
        
                    self.current_position_idx = self.board.piece_positions.index((150, 600))
                    self.current_position = self.board.piece_positions[self.current_position_idx+lefted_moves]
                else:
                    #if token will still be in right diagonal after move
                    self.current_position = self.board.right_diagonal[self.current_position_idx-moves]
                print('From right corner', self.current_position)

            elif self.current_position in self.board.left_diagonal:
                print('left corner', self.current_position, self.in_game)
                self.current_position_idx = self.board.left_diagonal.index(self.current_position)
                # Token is at the end position on the diagonal path or transition point to horizontal path
                if (self.current_position_idx - moves+1) <= 0:
                        ## end of left diagonal path is start point(goal position)
                    self.winner = self.player
                    return self.winner
                else:
                    self.current_position = self.board.left_diagonal[self.current_position_idx-moves]
                    
        elif self.current_position == (650,600) and (self.in_game == True) and (moves > 0):
                self.winner = self.player
                return self.winner
        else:
            # Token is on the board, move forward by the number of moves
            self.current_position_idx = self.board.piece_positions.index(self.current_position) + moves
            self.in_game = True
            if self.current_position_idx+1 >= len(self.board.piece_positions):
                self.winner = self.player
                return self.winner
            self.current_position=self.board.piece_positions[self.current_position_idx]
        print('new position', self.current_position)

    def draw(self):
        x, y = self.current_position
        x -= self.width / 2
        y -= self.height / 2
        self.screen.blit(self.image, (x, y))

    def collides_with(self, other_token):
        return self.current_position == other_token.current_position

# /if it reach end of index, token go back to piece_position path. right path goes to right corner's index of pieice position and move based on their moves.
#             if left path and cenrtal path reach the end of index, token go back to piece_position path[0], steart point
