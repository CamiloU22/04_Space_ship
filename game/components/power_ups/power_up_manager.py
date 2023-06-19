import pygame 
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.fire import Fire
from game.components.power_ups.speed import Speed 

from game.utils.constants import DEFAULT_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3, 5)
        self.shield= Shield()
        
    def generate_power_up(self):
        power_up_items = [Shield, Fire, Speed]
        power_up_type = random.choice(power_up_items)
        power_up = power_up_type()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

        
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
            
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                if power_up.__class__ is Shield:
                    power_up.play(game)
                elif power_up.__class__ is Fire:
                    power_up.play(game)
                elif power_up.__class__ is Speed:
                    power_up.play(game)
                self.power_ups.remove(power_up)
                break

            
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self,game):
        now = pygame.time.get_ticks()
        self.power_ups = []
        game.player.power_up_type = DEFAULT_TYPE
        self.when_appears = random.randint(5000, 10000)