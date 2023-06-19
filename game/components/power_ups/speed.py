from game.components.power_ups.power_up import PowerUps
from game.utils.constants import SPEED, SPEED_TYPE, SPACESHIP_SPEED

class Speed(PowerUps):
    def __init__(self):
        super().__init__(SPEED,SPEED_TYPE)

    def play(self, game):
        game.player.power_up_type = SPEED_TYPE
        game.player.set_image((65,75), SPACESHIP_SPEED)