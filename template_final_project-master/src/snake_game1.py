import pygame 
from pygame.locals import *

def draw_block():
    surface.fill((0, 128, 255))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1000, 500))
    surface.fill((0, 128, 255))
    
    block = pygame.image.load("template_final_project-master/assets/pixil-frame-0.png").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))
    
    pygame.display.flip()
    
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    
                if event.key == K_w:
                    block_y -= 10
                    draw_block()
                if event.key == K_s:
                    block_y += 10
                    draw_block()
                if event.key == K_a:
                    block_x -= 10
                    draw_block()
                if event.key == K_d:
                    block_x += 10
                    draw_block()
                
            elif event.type == QUIT:
                run = False
    