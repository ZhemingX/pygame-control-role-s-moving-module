import sys
import pygame
from settings import Settings
from luna_role import Agent
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # set agent
    agent0 = Agent(screen) 
    # set caption
    pygame.display.set_caption("luna mode")
    # set background color
    bg_color = ai_settings.bg_color
    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events(agent0, ai_settings)
        # agent position update
        agent0.update_position()
        # update and display screen
        gf.update_screen(ai_settings, screen, agent0)
        
run_game()

