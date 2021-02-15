import pygame
from pygame.time import Clock

import pyautogui

class Game:
    def __init__(self):

        self._screensize = pyautogui.size()
        self._running = False


    def start(self):

        """
        Point d'entrée du jeu.
        """

        print()
        print("[GAME] Starting PyGame...")

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("The Blue Moon")
        #pygame.display.set_icon(pygame.image.load(res.get_res("")))

        self.__init__()
        self._running = True

        print("[GAME] Starting loop...")

        clock = Clock()

        while self._running :

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.ESCAPE):
                    self._running = False
                else :
                    pygame.display.set_mode(self._screensize)

            pygame.display.flip()
            clock.tick(60)

        print("[GAME] Cleanup...")

        pygame.quit()

        print("[GAME] Stopped.")