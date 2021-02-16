from pygame import Surface
import pygame

class View():

    """
    Classe abstraite pour chacune des vues
    """

    BLACK = (0,0,0)

    def __init__(self, name, game):

        """
        Initialisation des vues
        """

        self.game = game
        self.bg = pygame.image.load("res/" + name + ".jpg")
        self.bg = pygame.transform.smoothscale(self.bg, self.game.screen_size)

    def draw(self):

        self.game.WIN.blit(self.bg, (0,0))
