import pygame
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))




class YutNoriBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.path_length = self.width * 2 + self.height * 2 - 4
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.center_position = (400, 350)
        self.piece_positions = []
        self.event_positions = [(400, 350),(150, 100),(650, 100), (400, 350), (150, 600)]  
        self.left_diagonal = []
        self.right_diagonal = []

        self.init_piece_positions()

    def init_piece_positions(self):
        for i in range(6):
            self.piece_positions.append((650 - i * 100, 600))
  
    

        ## bottom left
        for i in range(4):
            self.piece_positions.append((150, 500 - i * 100))

        for i in range(6):
            self.piece_positions.append((150 + i * 100, 100))

        ##top-left
        

      
        for i in range(4):
            self.piece_positions.append((650, 200 + i * 100))
        self.piece_positions.append((650, 600))


        ## top right corner

        self.piece_positions.reverse()

        self.left_diagonal.append((650,600))
        for i in range(5):
            
            x = 550 - i * 75
            y = 500 - i * 75
            
            self.left_diagonal.append((x, y))
        self.left_diagonal.append((150, 100))
        # print(self.left_diagonal, 'left')
            
    
        self.right_diagonal.append((150, 600))
        for i in range(5):

            x = 250 + i * 75

            y = 500 - i * 75
            self.right_diagonal.append((x, y))
        self.right_diagonal.append((650, 100))
        # print(self.right_diagonal, 'right')
        # print(self.piece_positions)
        
 
      


  

    def draw(self):
        pass
    #for debugging
        #   for position in self.piece_positions:
        #     pygame.draw.circle(self.screen, (255, 255, 255), position, 10)
        #     font = pygame.font.Font(None, 20)
        #     text = font.render(f"{position}", True, (255, 0, 0))
        #     text_rect = text.get_rect(center=position)
        #     self.screen.blit(text, text_rect)
                
        #     for position in self.event_positions:
        #         pygame.draw.circle(self.screen, (255, 255, 255), position, 10)
        #         font = pygame.font.Font(None, 20)
        #         text = font.render(f"{position}", True, (255, 0, 0))
        #         text_rect = text.get_rect(center=position)
        #         self.screen.blit(text, text_rect)
                
        #     for position in self.left_diagonal:
        #         pygame.draw.circle(self.screen, 'pink', position, 10)
        #         font = pygame.font.Font(None, 20)
        #         text = font.render(f"{position}", True, (255, 0, 0))
        #         text_rect = text.get_rect(center=position)
        #         self.screen.blit(text, text_rect)
                
        #     for position in self.right_diagonal:
        #         pygame.draw.circle(self.screen, 'yellow', position, 10)
        #         font = pygame.font.Font(None, 20)
        #         text = font.render(f"{position}", True, (255, 0, 0))
        #         text_rect = text.get_rect(center=position)
        #         self.screen.blit(text, text_rect)
        
        #     for position in self.event_positions:
        #         if position == (150, 600):
        #             pygame.draw.circle(self.screen, 'red', position, 10)
        #         elif position == (150, 100):
        #             pygame.draw.circle(self.screen, 'blue', position, 10)
        #         elif position == (650, 100):
        #             pygame.draw.circle(self.screen, 'green', position, 10)
        #         else:
        #             pygame.draw.circle(self.screen, 'orange', position, 10)



            # draw diagonal shortcut path


# ##When a token arrives at the top left or top right corner of the board, the player can take a diagonal shortcut to the opposite corner.
# A shortcut path will be added to the board, and the token will follow this shortcut path when it arrives at the left, center, or right corner of the board.
# The player's aim is to circle back to the starting point in a counter-clockwise direction.