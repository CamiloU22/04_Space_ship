import pygame
from pygame.sprite import Sprite

class BulletManager:

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []


    def update(self,game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect)and bullet.owner != 'enemy':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.update_score()       


    def draw (self,screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)

    