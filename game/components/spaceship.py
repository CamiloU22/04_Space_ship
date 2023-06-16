import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH
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

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x = self.rect.x - 10
        else :
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x =self.rect.x + 10
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y = self.rect.y - 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y = self.rect.y + 10

    def move_up_left(self):
        if self.rect.left > 0 and self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.x -= 10
            self.rect.y -= 10

    def move_up_right(self):
        if self.rect.right < SCREEN_WIDTH and self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.x += 10
            self.rect.y -= 10

    def move_down_left(self):
        if self.rect.left > 0 and self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.x -= 10
            self.rect.y += 10

    def move_down_right(self):
        if self.rect.right < SCREEN_WIDTH and self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.x += 10
            self.rect.y += 10
    
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):
        
        if user_input[pygame.K_LEFT]:
            if user_input[pygame.K_UP]:
                self.move_up_left()
            elif user_input[pygame.K_DOWN]:
                self.move_down_left()
            else:
                self.move_left()
        elif user_input[pygame.K_RIGHT]:
            if user_input[pygame.K_UP]:
                self.move_up_right()
            elif user_input[pygame.K_DOWN]:
                self.move_down_right()
            else:
                self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()     
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)            

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


