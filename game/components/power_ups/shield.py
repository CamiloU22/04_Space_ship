from game.components.power_ups.power_up import PowerUps
from game.utils.constants import SHIELD, SHIELD_TYPE , SPACESHIP_SHIELD

class Shield(PowerUps):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE)

    def play(self, game):
        game.player.power_up_type = SHIELD_TYPE
        game.player.set_image((65,75), SPACESHIP_SHIELD)
        
