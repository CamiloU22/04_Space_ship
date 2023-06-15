import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
# ENEMYS = {
#     0: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")),
#     1: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png")),
#     2: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png")),
#     3: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png")),
#     4: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png")),
#     5: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_6.png")),
#     6: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_7.png")),
#     7: pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_8.png")),
# }
ENEMY1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
                          

FONT_STYLE = 'freesansbold.ttf'
