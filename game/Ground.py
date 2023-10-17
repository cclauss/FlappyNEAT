import pygame

from game.globals import win_width

# Scroll
scroll_speed = 3

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_image):
        pygame.sprite.Sprite.__init__(self) #initialising the base class
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
