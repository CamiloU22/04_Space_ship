import pygame 

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu


class Game:
    def __init__(self):
        LEVEL = 8
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = False
        self.game_speed = 10

        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.menu = Menu("Press any key to start...", self.screen)
        self.hight_score = 0
        self.dead = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        self.enemy_manager.resset()
        self.score = 0

        self.playing = True
        while self.playing:
            self.events()
            if self.playing:
                self.update()
                self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self,)
        if user_input[pygame.K_SPACE]:
            self.player.shoot(self.bullet_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill( (255,255,255)) #color blanco
        
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen) 
        self.bullet_manager.draw(self.screen) 
        self.draw_score()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg = self.y_pos_bg + self.game_speed 


    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_hight = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('Game Over Press any Key To restart')
            self.draw_scores("HIGHT SCORE",self.hight_score,550,350)
            self.draw_scores("YOUR SCORE",self.score,550,400)
            # self.draw_scores("TOTAL DEATHS",self.dead,550,450)
            self.menu.draw(self.screen)
        
        icon =pygame.transform.scale(ICON, (80,120))
        self.screen.blit(icon, (half_screen_width -50, half_screen_hight - 150 ))
        self.menu.update(self)

    def update_score(self):
        self.score +=1
        if self.score > self.hight_score:
            self.hight_score = self.score

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE,30)
        text =font.render(f'Score: {self.score}',True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100,50)
        self.screen.blit(text,text_rect)

    def draw_scores(self,message,score,x,y):
        font = pygame.font.Font(FONT_STYLE,30)
        text =font.render(f'{message} :{score}',True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text,text_rect)

        


