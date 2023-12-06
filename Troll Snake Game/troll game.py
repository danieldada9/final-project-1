import pygame
from pygame.locals import *
import time
import random

size = 40
class MainMenu:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("TIME TO TROLL - Main Menu")
        self.clock = pygame.time.Clock()
        self.is_closed = False

        self.troll_image = pygame.image.load("pictures and music/trollmenu.png").convert()

    def display_menu(self):
        font = pygame.font.SysFont('Comic Sans', 36)
        title_text = font.render("To start TROLLING", True, (0, 0, 0))
        start_text = font.render("Press Enter to Start", True, (0, 0, 0))

        self.surface.fill((0, 0, 0))

        self.surface.blit(self.troll_image,(0,0))
        self.surface.blit(title_text, (250, 110))
        self.surface.blit(start_text, (250, 330))
        pygame.display.flip()

    def run(self):
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:
                    menu_running = False
                elif event.type == QUIT:
                    pygame.quit()
                    quit()

            self.display_menu()
            self.clock.tick(10)

        pygame.quit()
        self.is_closed = True


class watermelon:
    def __init__(self,main_screen):
        self.image = pygame.image.load("pictures and music/watermelon.png").convert()
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
        self.block = pygame.image.load("pictures and music/trollface.png").convert()
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'down'

    def increaselength(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
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
        pygame.display.set_caption("TROLL SNAKE GAME")

        pygame.mixer.init()
        self.backgroundmusic()
        self.surface = pygame.display.set_mode((800, 500))
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

    def backgroundmusic(self):
        pygame.mixer.music.load("pictures and music/Troll Face Song.mp3")
        pygame.mixer.music.play()
    def score(self):
            font = pygame.font.SysFont('Comic Sans', 20)
            score1 = font.render(f"Trolls: {self.snake.length}", True, (255, 255, 255))
            self.surface.blit(score1, (720, 10))

    def background(self):
        bg= pygame.image.load("pictures and music/background.png")
        self.surface.blit(bg,(0,0))

    def play(self):
        self.background()
        self.snake.walk()
        self.watermelon.draw()
        self.score()
        pygame.display.flip()

        # Troll eating apple
        if self.eatwatermelon(self.snake.x[0], self.snake.y[0], self.watermelon.x, self.watermelon.y):
            sound = pygame.mixer.Sound("pictures and music/Troll face laugh.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increaselength()
            self.watermelon.move()


        for i in range(3,self.snake.length):
            if self.eatwatermelon(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                sound = pygame.mixer.music.load("pictures and music/troll.mp3")
                pygame.mixer.music.play(sound)
                raise 'Game Over'

        if (
                self.snake.x[0] < 0
                or self.snake.x[0] >= self.surface.get_width()
                or self.snake.y[0] < 0
                or self.snake.y[0] >= self.surface.get_height()
        ):
            raise Exception('Game Over')
    def show_game_over(self):
        self.background()
        font = pygame.font.SysFont('arial', 20)
        line1= font.render(f"You've Been TROLLED! Your trolls are  {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (50,100))
        line2 = font.render("to TROLL again press Enter. To stop TROLLING press Escape!",True, (255,255,255))
        self.surface.blit(line2,(50,150))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface,1)
        self.watermelon = watermelon(self.surface)


    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == "__main__":
    mainmenu = MainMenu()
    mainmenu.run()


if __name__ == "__main__":
    game = Game()
    game.run()

    if not mainmenu.is_closed:
        game = Game()
        game.run()