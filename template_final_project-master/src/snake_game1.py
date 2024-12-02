import pygame 
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1000, 500))
    surface.fill((0, 128, 255))
    pygame.display.flip()
    
    block = pygame.image.load("assets/spixil-frame-0.png").convert()
    block_x = 1000
    block_y = 500
    surface.blit(block, (block_x, block_y))
    
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            elif event.type == QUIT:
                run = False
    