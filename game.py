from player import Player
from monster import Monster
import pygame
class Game:
    def __init__(self):
        #definir le deburt du jeu
        self.is_playing = False
        #generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        #groupe de monster
        self.all_monsters = pygame.sprite.Group()
        self.font = pygame.font.Font("assets/my_font.ttf",25)
        self.score = 0
        
    def start(self):
        self.is_playing = True
        
        #appeller un monster
        self.spawn_monster()
        self.spawn_monster()

    def add_score(self,points=10):
        self.score += points
    def game_over(self):
        # restart le jeu
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self,screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score: {self.score}", 1, (0,0,0))
        screen.blit(score_text,(20,20))

        #application de l'image du joueur
        screen.blit(self.player.image,self.player.rect)

        # actualiser la barre de vie du player
        self.player.update_health_bar(screen)
        #recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #recuperer les monsters
        for monnster in self.all_monsters:
            monnster.forward()
            monnster.update_health_bar(screen)


        #application des images de groupe de projectile 
        self.player.all_projectiles.draw(screen)

        #afficher l'ensemble des monsters 
        self.all_monsters.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
