import pygame 
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("template_final_project-master/assets/pixil-frame-0.png").convert()
        self.x = 100
        self.y = 100
        self.direction = 'up'
        
    def draw(self):
        self.parent_screen.fill((0, 128, 255))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    def walk(self):
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10
            
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
        self.snake = Snake(self.surface)
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
    
    