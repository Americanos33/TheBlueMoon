import pygame
from pygame.time import Clock

import view
from view import View

import pyautogui

from menu import Menu


print()
print("[GAME] Starting PyGame...")
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("The Blue Moon")
#pygame.display.set_icon(pygame.image.load(res.get_res("")))    

class Game:
    def __init__(self):

        self.screen_size = pyautogui.size()
        self.WIN = pygame.display.set_mode(self.screen_size)

        print(self.screen_size.width, self.screen_size.height)

        self._running = False
        self.inMenu = False

        self._viewList = []
        self.initViews()

    def initViews(self):

        Acceuil = View("Acceuil", self)
        self._viewList.append((Acceuil, "Acceuil"))

    def start(self):

        """
        Point d'entrée du jeu.
        """

        self._running = True

        print("[GAME] Initializing Views...")

        self._viewList[0][0].draw()

        print("[GAME] Starting loop...")

        clock = Clock()

        while self._running :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                #else : # boucle de jeu
                    
            pygame.display.flip()

            clock.tick(60)

        print("[GAME] Cleanup...")

        pygame.quit()

        print("[GAME] Stopped.")


    def launchBaseMenu(self):
        
        menu = Menu(self, 1)


    def loadLevel(self, nblvl):

        