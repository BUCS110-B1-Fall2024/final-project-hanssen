import pygame 
import time

def main():
    pygame.init()
    
    surface = pygame.display.set_mode((500, 500))
    surface.fill((0, 0, 255))
    pygame.display.flip()
    time.sleep(5)