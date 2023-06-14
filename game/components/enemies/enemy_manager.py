from game.components.enemies.enemy import Enemy

class EnemyManager:

    def __init__(self,level):
        self.enemies = []
        for i in range(level):
            enemy = Enemy(i)
            self.enemies.append(enemy)

    def update (self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def add_enemy(self):
        if len(self.enemies) <1 :
            enemy = Enemy()
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in  self.enemies:
            enemy.draw(screen)
