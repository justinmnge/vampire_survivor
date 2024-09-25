import pygame
from os.path import join
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.load(join('images', 'player', 'o.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()

# pygame setup
pygame.init()
display = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    display.fill("black")
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()