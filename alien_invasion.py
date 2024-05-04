import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop of game
    while True:
        # listen keyboard and mouse event
        gf.check_events(ship)
        ship.update()
        # redraw screen every loop
        gf.update_screen(ai_settings, screen, ship)


run_game()
