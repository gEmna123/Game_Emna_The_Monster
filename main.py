import pygame 
import math
import pygame.display
import pygame.event
import pygame.image
import pygame.sprite
from game import Game

pygame.init()
 


#generation de lla fenetre du jeu
pygame.display.set_caption("Emna The monster")
screen = pygame.display.set_mode((1080,670))

#importation d'arriere plan 
background = pygame.image.load('assets/bg1.jpg')

#chargement de la banniere
banner = pygame.image.load('assets/banner2.png')
banner = pygame.transform.scale(banner,(300,300))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /3)
banner_rect.y = math.ceil(screen.get_height() /8)



#importer le bouton
play_button = pygame.image.load('assets/button1.png')
play_button = pygame.transform.scale(play_button,(300,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() /1.90)
#chargement du jeu 
game = Game()
is_running = True
while is_running:
    #application d'arriere plan
    screen.blit(background,(0,0))

    #verifier le debut du jeu
    if game.is_playing:
        game.update(screen)
    #verifier si le jeu n'a pas commance
    else:
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)


     #mettre a jour la fenetre du jeu
    pygame.display.flip()

    #boucle de la jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si le souris est sur le boutton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu start
                game.start()
        
