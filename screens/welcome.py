import pygame
import sys
import os

# add the parent directory of the current file to the system path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# rest of your code goes here

from components.button import Button

from screens.base_screen import BaseScreen

from screens.game import GameScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        """
        Creates two buttons on the screen.
        """
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        self.background = pygame.transform.scale(pygame.image.load(os.path.join(parent_dir, 'images', 'start_image.png')).convert(), (1000, 800))

        
        bg_size = self.background.get_size()
        button_size = (300, 100)

        # Calculate the x-position for the buttons for horizonal center of window
        x_pos = int(bg_size[0] / 2 - button_size[0] / 2)


        self.button1 = Button(300, 100, "Start Game")
        self.button1.rect.x = x_pos
        self.button1.rect.y = 525

        self.button2 = Button(300, 100, "Rules")
        self.button2.rect.x = x_pos
        self.button2.rect.y = 650

        self.sprites.add(self.button1)
        self.sprites.add(self.button2)
        self.running = True

    def draw(self):
        """Draws the screen"""
        self.window.blit(self.background, (0, 0))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Button 1 clicked
            if self.button1.rect.collidepoint(event.pos):
                self.next_screen = "game"
                self.running = False
                print('left click')
                self.persistent["welcome_button_clicked"] = 1
            # # Button 2 clicked
            if self.button2.rect.collidepoint(event.pos):
                self.persistent["welcome_button_clicked"] = 2
                import webbrowser
                rule_url = ''
                webbrowser.open(url, new=2)


def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("My Game")

    screen = WelcomeScreen(window)

    while screen.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.running = False
          
        screen.draw()
        pygame.display.flip()

        # redirect to base game page when game start button is clicked
        if screen.next_screen == "game":
            screen = GameScreen(window)
            

     
        
  

    

    


if __name__ == "__main__":
    main()