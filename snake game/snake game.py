import pygame
from pygame.locals import *
import time
import random

size = 40



class watermelon:
    def __init__(self,main_screen):
        self.image = pygame.image.load("resources/watermelon.png").convert()
        self.main_screen =main_screen
        self.x = size * 2
        self.y = size * 2

    def move(self):
        self.x = random.randint(0,15) * size
        self.y = random.randint(0,10) * size
    def draw(self):
        self.main_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self,main_screen,length):
        self.length = length
        self.main_screen = main_screen
        self.block = pygame.image.load("resources/trollface.png").convert()
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'down'

    def increaselength(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.main_screen.fill((0,0,0))
        for w in range(self.length):
             self.main_screen.blit(self.block, (self.x[w], self.y[w]))


    def walk(self):

        for w in range(self.length-1,0,-1):
            self.x[w] = self.x[w-1]
            self.y[w] = self.y[w - 1]

        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size

        self.draw()



    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 600))
        self.surface.fill((0, 0, 0))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.watermelon = watermelon(self.surface)
        self.watermelon.draw()


    def eatwatermelon(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                    return True
            return False

    def play(self):
        self.snake.walk()
        self.watermelon.draw()
        self.score()
        pygame.display.flip()

        # Troll eating apple
        if self.eatwatermelon(self.snake.x[0], self.snake.y[0], self.watermelon.x, self.watermelon.y):
            self.snake.increaselength()
            self.watermelon.move()

    def score(self):
            font = pygame.font.SysFont('arial', 20)
            score1 = font.render(f"Trolls: {self.snake.length}", True, (255, 255, 255))
            self.surface.blit(score1, (600, 10))

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(.2)

if __name__ == "__main__":
    game = Game()
    game.run()

