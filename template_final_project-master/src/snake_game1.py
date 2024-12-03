import pygame 
from pygame.locals import *
import time
import random

size = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("template_final_project-master/assets/apple.png").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120
        
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(0, 24) * size
        self.y = random.randint(0, 19) * size

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("template_final_project-master/assets/pixil-frame-0.png").convert()
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'down'
        
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
        
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
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((0, 128, 255))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
            
        return False
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
    
    def display_score(self):
        font = pygame.font.SysFont('roboto', 30, bold = True)
        score = font.render(f"Score: {self.snake.length - 1}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))
    
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
                    
            self.play()
            
            time.sleep(0.3)

if __name__ == "__main__":
    game = Game()
    game.run()    
    
    