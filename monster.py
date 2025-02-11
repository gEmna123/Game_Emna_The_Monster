import pygame
import random
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,340)
        self.rect.y = 540
        self.velocitty = random.randint(1,2)
    
    def damage(self,amount):
        self.health -= amount
        if self.health <= 0:
            #apparetre comme un nouveau
            self.rect.x = 1000
            self.health = self.max_health
            self.velocitty = random.randint(1,2)
            #gerer le score
            self.game.add_score()

    
    def update_health_bar(self,surface):
        #dessioner la bar
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 10 ,self.rect.y -20 ,self.max_health,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10 ,self.rect.y -20 ,self.health,5])
    
    
    def forward(self):
        #verification de collision de groupe de joueur avec le monster
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocitty
        
        #si le monster est en coliison anec le player
        else:
            #infliger les degats
            self.game.player.damage(self.attack)
