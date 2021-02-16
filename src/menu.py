import pygame
import pygame_menu

baseTheme = pygame_menu.themes.Theme(background_color = (0,0,0, 100),
                                     title_font_color = (255,255,255),
                                     title_shadow = True,
                                     title_background_color = (0,0,0),
                                     title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
                                     widget_font = pygame_menu.font.FONT_NEVIS,
                                     widget_font_color = (255,255,255))
inGameTheme = pygame_menu.themes.Theme()


class Menu():

    def __init__(self, game, nb):

        self.game = game

        if nb == 1 : #Base Menu
            self.menu = pygame_menu.Menu(self.game.screen_size.height, self.game.screen_size.width, "The Blue Moon - Menu", theme=baseTheme)
            self.menu.add_button('Play', self.game.start)
            self.menu.add_button('Quitter', None)
        elif nb == 2 : #InGame Menu
            self.menu = pygame_menu.Menu(self.game.screen_size.height, self.game.screen_size.width, "The Blue Moon - Menu", theme=inGameTheme)

        self.showMenu()


    def showMenu(self):

        """
        Draw the current menu
        """

        self.menu.mainloop(self.game.WIN)

