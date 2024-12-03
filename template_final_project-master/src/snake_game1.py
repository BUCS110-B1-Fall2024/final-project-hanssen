import pygame 
from pygame.locals import *
import time

size = 40

class Snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("template_final_project-master/assets/pixil-frame-0.png").convert()
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'up'
        
    def draw(self):
        self.parent_screen.fill((0, 128, 255))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i] ))
        pygame.display.flip()
        
    def walk(self):
        
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
            
        self.draw()
        
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'
        
    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction = 'right'

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((0, 128, 255))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
    
    def run(self):
        run = True
    
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                    
                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_s:
                        self.snake.move_down()
                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_d:
                        self.snake.move_right()
                
                elif event.type == QUIT:
                    run = False
                    
            self.snake.walk() 
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()    
    
    