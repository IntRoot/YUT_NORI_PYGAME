import pygame
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class BaseScreen:
    """
    Base class for a screen. You should create your own classes that inherit from this class.
    """

    def __init__(self, window):
        """Default attributes"""
        self.window = window
        self.background = pygame.transform.scale(pygame.image.load(os.path.join(parent_dir, 'images', 'board.png')).convert(), (1000, 800))
        self.next_screen = False
        self.persistent = {}

    def run(self):
        """Runs the pygame event loop"""
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()

            for event in pygame.event.get():
                # Default event management
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                self.manage_event(event)

    @property
    def rect(self):
        return self.window.get_rect()

    def draw(self):
        """
        Override this method in your child classes to handle the draw operations for the screen.
        """
        pass

    def update(self):
        """
        Override this method in your child classes to handle the update operations for the screen.
        """
        pass

    def manage_event(self, event):
        """
        Override this method in your child classes to handle events for the screen.
        """
        pass
