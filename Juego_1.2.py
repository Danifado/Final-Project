# -*- coding: utf-8 -*-

import pygame
import player
from pygame.locals import *


pygame.init()

"""Variables"""

width = 790 #Ancho de la ventana
height = 350 #Largo de la ventana

screen = pygame.display.set_mode((width, height))#Crea una ventana
pygame.display.set_caption("Shattered Time")
clock = pygame.time.Clock() #Lo utilizaremos para dar la velocidad el personaje

player = player.Player((105,60),5,"Body_1.png")
"""La clase player, los
argumentos que recibe son: Coordenadas, velocidad e imagen para tomar los
sprites respectivamente"""

background = pygame.image.load('mapa_1.png') #Carga la imagen de fondo

"""Pause: """

pause_menu = pygame.image.load("Pause_1.png")

def Button(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords[0]+190,coords[1]
    #surface.blit(image,coords)
    return (image,imagerect)

game_over = False

pause = True

white = (255,255,255)


def load_music(song):
    """Carga una canción"""
    pygame.mixer.music.load(song)
def play_music():
    """Inicia la canción """
    pygame.mixer.music.play(-1) #El -1 reproduce la canción en bucle
def pause_music():
    pygame.mixer.music.pause()
def unpause_music():
    pygame.mixer.music.unpause()

load_music("Spring-Village.mp3")
play_music()

def exit():
    pygame.quit()
    quit()

def not_pause():
    """Establece pause como False """
    global pause
    pause = False

def paused():

    out = False

    """// Suspende el juego y abre el menú de pausa con las opciones "Main Menu",
    "Resume Game" & "End Game". // """

    while pause:

        if out == True:
            break
        screen.blit(background,(0,0))
        screen.blit(player.image,player.rect)

        screen.blit(pause_menu,(0,0))
        mouse = pygame.mouse.get_pos()

        print(mouse)

        b_main = Button("b_main_down.png",(288,143),screen)
        b_resume = Button("b_resume_down.png",(286,190),screen)
        b_end = Button("b_end_down.png",(297,235),screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    unpause_music()
                    not_pause()

            if b_main[1].collidepoint(mouse):
                screen.blit(b_main[0],b_main[1])
            if b_resume[1].collidepoint(mouse):
                screen.blit(b_resume[0],b_resume[1])
            if b_end[1].collidepoint(mouse):
                screen.blit(b_end[0],b_end[1])

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if b_main[1].collidepoint(mouse):
                        screen.blit(b_main[0],b_main[1])
                        continue
                    if b_resume[1].collidepoint(mouse):
                        unpause_music()
                        not_pause()
                    if b_end[1].collidepoint(mouse):
                        exit()

        pygame.display.update()
        clock.tick(20)


while game_over == False:
    print(player.rect.topleft)
    screen.blit(background,(0,0)) #Aquí se carga la imágen de fondo

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
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
            pause_music()
            pause = not pause
            paused()


load_music("Spring-Village.mp3")
play_music()

pygame.quit ()
