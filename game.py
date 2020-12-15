import pygame
import random

X_MAX = 600
Y_MAX = 700
#ZOM_TYPES = [{}, {'speed':.5}, {'speed':1}, [{'speed':.3}, {'speed':2}]
# Zombie types: type 1 : crawler, type 2 : regular, type 3 : behemoth, type 4 : sprinter

class Game:
    def __init__(self):
        self._inputs = Input()
        self._outputs = Output()
        self._zombies = Zombies()
        self._crosshair = Crosshair()
        self._score = Score()
        self._heat = Heat()

    def play(self):
        while True:
            self.get_inputs()
            self.do_outputs()

    def get_entities(self):
        entities = [self._crosshair, self._score, self._heat]
        for zombie in self._zombies.get_all():
            entities.append(zombie)
        return entities

    def do_outputs(self):
        self._outputs.place_entities(self.get_entities())

    def get_inputs(self):
        pos = self._inputs.get_mouse_pos()
        clicked = self._inputs.get_mouse_press()
        self._crosshair.update_location((pos[0] - 25, pos[1] -25))

class Entity:
    def __init__(self):
        self._location = (0, 0)
        self.image = pygame.image.load('nothing.png')

    def update_location(self, location):
        self._location = location

    def update_image(self, image):
        self._image = pygame.image.load(image)

    def get_image(self):
        return self._image

    def get_location(self):
        return self._location

class Zombie(Entity):
    def __init_(self, zom_type):
        super().__init__()
        self._type = zom_type
        self._velocity = ZOM_TYPES[self._type]['speed']
        self.update_image = f'zombie{self._type}.png'
        self.update_location((random.randint(5, 545), -50))

    def move(self):
        self.update_location((self._location[0], self._location[1] + self._velocity))

class Zombies:
    def __init__(self):
        self._zombies = []

    def add_zombie(score):
        perc = random.randint(1, 100)
        perc_spread = [0]
        for i in range(4):
            if score <= 400:
                if i == 0:
                    perc_spread.append(-.1 * score + 40)
                elif i == 1:
                    perc_spread.append((-.15 * score + 60) + perc_spread[1])
                elif i == 2:
                    perc_spread.append((.1 * score) + perc_spread[2])
                elif i == 3:
                    perc_spread.append((.15 * score) + perc_spread[3])
        print(perc_spread)
        for i in range(1, 5):
            if perc_spread[i] >= perc and perc_spread[i - 1] < perc:
                zombie = Zombie(i)
                self._zombies.append(zombie)
                break

    def get_all(self):
        return self._zombies

    def kill(self, index):
        self._zombies.pop(index)


class Crosshair(Entity):
    def __init__(self):
        super().__init__()
        self.update_image('nothing.png')

class Text(Entity):
    def __init__(self):
        self._font = pygame.font.SysFont(None, 48)
        self._image = self._font.render('', True, (255, 255, 255))

    def set_text(self, text, rgb=(255, 255, 255)):
        self._image = self._font.render(text, True, rgb)

class Score(Text):
    def __init__(self):
        super().__init__()
        self._score = 0
        self.update_location((5, 5))
        self.update_score(0)

    def update_score(self, val):
        self._score += val
        self.set_text(f'Score: {self._score}')

class Heat(Text):
    def __init__(self):
        super().__init__()
        self._heat = 0
        self.update_location((300, 5))
        self.update_heat(0)

    def update_heat(self, val):
        self._heat += val
        gb = 255 - self._heat
        self.set_text(f'Heat Level: {(self._heat + 180)/2}°F', (255, gb, gb))

class Input:
    def __init__(self):
        self._mouse_pos = (0, 0)
        self._is_pressed = False
    def get_mouse_press(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._is_pressed = True
                return self._is_pressed
            elif event.type == pygame.MOUSEBUTTONUP:
                self._is_pressed = False
                return self._is_pressed
    def get_mouse_pos(self):
        self._mouse_pos = pygame.mouse.get_pos()
        return self._mouse_pos

        

class Output:
    def place_entities(self, entities):
        screen.fill((0, 0, 0))
        for entity in entities:
            screen.blit(entity.get_image(), entity.get_location())
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((X_MAX, Y_MAX))
    pygame.mouse.set_visible(False)
    game = Game()
    game.play()