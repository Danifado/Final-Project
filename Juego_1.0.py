# -*- coding: utf-8 -*-

import pygame
import player

pygame.init()

"""Variables"""

width = 791 #Ancho de la ventana
height = 575 #Largo de la ventana

screen = pygame.display.set_mode((width, height))#Crea una ventana
pygame.display.set_caption("Glass")
clock = pygame.time.Clock() #Lo utilizaremos para dar la velocidad el personaje

player = player.Player((67,45),5,"Body_1.png")
"""La clase player, los
argumentos que recibe son: Coordenadas, velocidad e imagen para tomar los
 sprites respectivamente"""

background=pygame.image.load('background_1.png') #Carga la imagen de fondo

""" Quitar este comentario para ver el área de las colisiones
collision = pygame.sprite.Sprite()
collision = pygame.image.load("Collision_1.png")
"""

game_over = False

def load_music(song):
    """Carga una canción"""
    pygame.mixer.music.load(song)
def play_music():
    """Inicia la canción """
    pygame.mixer.music.play(1)

load_music("Spring-Village.mp3")
play_music()

while game_over == False:

    screen.blit(background,(0,0)) #Aquí se carga la imágen de fondo
    """ Quitar este comentario para ver el área de las colisiones
    screen.blit(collision,(0,0)) #Esta es la imagen que indica donde debería haber colisiones entre el mapa y el jugador """

#    if player.colliderect(collision): #Ignorar--------------------------------

    for event in pygame.event.get():
        """Evalua si se presionó el boton de cerrar el juego, de ser así, se
        terminará la ejecución del mismo"""
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    """clock.tick() determina la velocidad base del personaje, acualizando Clock
    en milisegudos """
    clock.tick(20)
    if event.type == pygame.KEYDOWN:
        """
        if event.key == pygame.K_p:
            clock.tick(0)
        if event.key == pygame.K_r:
            clock.tick(20)
            """
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_p:
            game_over = True

load_music("Spring-Village.mp3")
play_music()

pygame.quit ()
