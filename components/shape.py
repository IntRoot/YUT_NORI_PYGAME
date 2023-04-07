import pygame


class Shape(pygame.sprite.Sprite):
    def __init__(self, width, height, bgcolor=(0, 0, 0), fgcolor=(255, 255, 255), limits=None):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(bgcolor)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.limits = limits

    def move(self, direction):
        if direction == "right":
            self.rect.x += self.speed
        if direction == "left":
            self.rect.x -= self.speed

        self.check_limits()

    def check_limits(self):
        if not self.limits:
            return

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.limits[0]:
            self.rect.right = self.limits[0]
