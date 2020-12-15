import pygame

X_MAX = 600
Y_MAX = 700

class Game:
    def __init__(self):
        self._thing = Something()

    def play(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing == False
                    pygame.display.quit()
                    pygame.quit()
            screen.blit(self._thing.get_image(), self._thing.get_location())
            pygame.display.update()

class Entity:
    def __init__(self):
        self._location = (0, 0)
        self._image = pygame.image.load('nothing.png')

    def update_location(self, location):
        self._location = location

    def update_image(self, image):
        self._image = pygame.image.load(image)

    def get_image(self):
        return self._image

    def get_location(self):
        return self._location

class Something(Entity):
    def __init__(self):
        super().__init__()
        self.update_image('red_dot.png')


class Input:
    pass

class Output:
    pass





if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    game = Game()
    game.play()