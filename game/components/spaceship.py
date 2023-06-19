import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, DEFAULT_TYPE, SHIELD_TYPE, FIRE_TYPE, SPEED_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    x_POS = (SCREEN_WIDTH // 2 ) - 40
    y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_POS
        self.rect.y = self.y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        self.speed = 10


    def move_left(self):
        if self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
        else :
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x =self.rect.x + self.speed
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - self.speed

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + self.speed
 
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):
        
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()     
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)     

        if self.power_up_type == SPEED_TYPE:
            self.speed = 20
        elif self.power_up_type == FIRE_TYPE:
            game.bullet_manager.activate_fire_powerup(20)

        if self.has_power_up and pygame.time.get_ticks() >= self.power_time_up:
            self.has_power_up = False
            self.power_time_up = 0
            self.set_image()  
            self.speed = 10
            game.bullet_manager.activate_fire_powerup(3)
            self.power_up_type = DEFAULT_TYPE
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def set_image(self, size = (40,60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.rect.x = self.x_POS
        self.rect.y = self.y_POS
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        self.speed = 10