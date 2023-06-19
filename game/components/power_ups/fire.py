from game.components.power_ups.power_up import PowerUps
from game.utils.constants import FIRE, FIRE_TYPE, SPACESHIP_FIRE

class Fire(PowerUps):
    def __init__(self):
        super().__init__(FIRE,FIRE_TYPE)

    def play(self, game):
        game.player.power_up_type = FIRE_TYPE
        game.player.set_image((65,75), SPACESHIP_FIRE)