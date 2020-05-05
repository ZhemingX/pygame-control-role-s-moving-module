import pygame

class Agent():
    def __init__(self, screen):
        # initialize agent and its location
        self.screen = screen
        # images for load
        self.stand_image = 'images/luna_role.bmp'
        self.left_image = 'images/luna_left.bmp'
        self.right_image = 'images/luna_right.bmp'
        self.up_image = 'images/luna_up.bmp'
        self.down_image = 'images/luna_down.bmp'
        # load bmp and get rectangle
        self.image = pygame.image.load(self.stand_image)
        # adjust the size of pics
        self.image = pygame.transform.scale(self.image, (130,130))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # put agent on the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # control its moving
        self.move_x = 0
        self.move_y = 0
        # tag for reloading image
        # 0 for stand, 1 for left, 2 for right, 3 for up, 4 for down
        self.tag = 0
            
    def reload_image(self):
        oldpos = (self.rect.centerx, self.rect.centery)
        if self.tag == 0:
            self.image = pygame.image.load(self.stand_image)
            self.image = pygame.transform.scale(self.image, (130,130))
        elif self.tag == 1:
            self.image = pygame.image.load(self.left_image)
            self.image = pygame.transform.scale(self.image, (120,120))
        elif self.tag == 2:
            self.image = pygame.image.load(self.right_image)
            self.image = pygame.transform.scale(self.image, (120,120))
        elif self.tag == 3:
            self.image = pygame.image.load(self.up_image)
            self.image = pygame.transform.scale(self.image, (120,120))
        elif self.tag == 4:
            self.image = pygame.image.load(self.down_image)
            self.image = pygame.transform.scale(self.image, (120,120))
        
        
        self.rect = self.image.get_rect()
        self.rect.centerx = oldpos[0]
        self.rect.centery = oldpos[1]
        
    def update_position(self):
        
        self.reload_image()

        self.rect.centerx += self.move_x
        self.rect.centery += self.move_y

        if self.rect.bottom > self.screen_rect.bottom or self.rect.top < self.screen_rect.top:
            self.rect.centery -= self.move_y
       
        if self.rect.left < self.screen_rect.left or self.rect.right > self.screen_rect.right:
            self.rect.centerx -= self.move_x
           
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)