import pygame
from pygame.locals import *
import time
import random

size = 40
menu_background_image = "template_final_project-master/assets/menu_screen.png"
game_background_color = (0, 128, 255)

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
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill(game_background_color)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
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
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

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

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def show_game_over(self):
        self.surface.fill(game_background_color)
        font = pygame.font.SysFont('roboto', 30, bold=True)
        line1 = font.render(f"Game is over: Your score is {self.snake.length}", True, (255, 255, 255))
        line2 = font.render("Press Enter to Restart or Escape to Quit", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def display_score(self):
        font = pygame.font.SysFont('roboto', 30, bold=True)
        score = font.render(f"Score: {self.snake.length - 1}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def show_main_menu(self):
        background_image = pygame.image.load(menu_background_image).convert()
        background_image = pygame.transform.scale(background_image, (1000, 800))
        self.surface.blit(background_image, (0, 0))

        play_button = pygame.Rect(400, 300, 200, 50)
        quit_button = pygame.Rect(400, 400, 200, 50)

        pygame.draw.rect(self.surface, (255, 255, 255), play_button)
        pygame.draw.rect(self.surface, (255, 255, 255), quit_button)

        font = pygame.font.SysFont('roboto', 30, bold=True)
        play_text = font.render("Play", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))

        self.surface.blit(play_text, (play_button.x + 65, play_button.y + 10))
        self.surface.blit(quit_text, (quit_button.x + 65, quit_button.y + 10))

        pygame.display.flip()
        return play_button, quit_button

    def run(self):
        run = True
        pause = False
        main_menu = True

        while run:
            if main_menu:
                play_button, quit_button = self.show_main_menu()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False

                    if pause and event.key == K_RETURN:
                        self.reset()
                        pause = False
                        main_menu = True

                    if not pause and not main_menu:
                        if event.key == K_w:
                            self.snake.move_up()
                        if event.key == K_s:
                            self.snake.move_down()
                        if event.key == K_a:
                            self.snake.move_left()
                        if event.key == K_d:
                            self.snake.move_right()

                elif event.type == MOUSEBUTTONDOWN and main_menu:
                    if play_button.collidepoint(event.pos):
                        main_menu = False
                        pause = False
                    elif quit_button.collidepoint(event.pos):
                        run = False

                elif event.type == QUIT:
                    run = False

            if not main_menu and not pause:
                try:
                    self.play()
                except Exception as e:
                    self.show_game_over()
                    pause = True

            time.sleep(0.15)

if __name__ == "__main__":
    game = Game()
    game.run()
