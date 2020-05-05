import sys
import pygame

def check_keydown_events(event, agent, ai_settings):
    # respond to keydown event
    if event.key == pygame.K_a:
        agent.move_x = -ai_settings.role_speed_factor
        agent.move_y = 0
        agent.tag = 1
    elif event.key == pygame.K_d:
        agent.move_x = ai_settings.role_speed_factor
        agent.move_y = 0
        agent.tag = 2
    elif event.key == pygame.K_w:
        agent.move_y = -ai_settings.role_speed_factor
        agent.move_x = 0
        agent.tag = 3
    elif event.key == pygame.K_s:
        agent.move_y = ai_settings.role_speed_factor
        agent.move_x = 0
        agent.tag = 4
    elif event.key == pygame.K_x:
        agent.move_x = 0
        agent.move_y = 0
        agent.tag = 0

def check_keyup_events(agent):
    # respond to keyup event
    agent.move_x = 0
    agent.move_y = 0
    agent.tag = 0

def check_events(agent, ai_settings):
    # respond to keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, agent, ai_settings)
        #elif event.type == pygame.KEYUP:
        #    check_keyup_events(agent)
        

def update_screen(ai_settings,screen,agent):
    # fill color
    screen.fill(ai_settings.bg_color)
    # display agent
    agent.blitme()
    # visualize the window
    pygame.display.flip()
    
    
