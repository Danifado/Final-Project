# -*- coding: utf-8 -*-

import pygame, player, enemy, enemy_1

from pygame.locals import *


pygame.init()

"""Variables"""

width = 790 #Ancho de la ventana
height = 350 #Largo de la ventana

screen = pygame.display.set_mode((width, height))#Crea una ventana
pygame.display.set_caption("Shattered Time")
clock = pygame.time.Clock() #Lo utilizaremos para dar la velocidad el personaje

player = player.Player((350,250),5,"Body_1.png")
player.fondo = 3
if player.fondo ==1:
    pygame.display.update()
    background = pygame.image.load("segundo_piso.png") #Carga la imagen de fondo
    rectangulo=pygame.draw.rect(background ,(50,210,0),(75,303,636,35),1)
    rectangulo_1=pygame.draw.rect(background ,(50,210,0),(60,62,40,235),1)
    rectangulo_2=pygame.draw.rect(background ,(50,210,0),(690,62,40,235),1)
    rectangulo_3=pygame.draw.rect(background ,(50,210,0),(75,25,636,35),1)
    salida =pygame.draw.rect(background,(50,210,0),(610,95,50,50),1)
    lado_1_1=pygame.draw.rect(background,(50,210,0),(625,110,40,0),1)
elif player.fondo == 2:
    background = pygame.image.load("fonfo_afuera.png")
    salida =pygame.draw.rect(background,(50,210,0),(90,55,20,30),1)
    lado_i = pygame.draw.rect(background,(0,0,0),(0,0,10,550),1)
    lado_a = pygame.draw.rect(background,(0,0,0),(0,0,791,5),1)
    lado_b =pygame.draw.rect(background,(0,0,0),(0,345,791,5),1)
    lado_d =pygame.draw.rect(background,(0,0,0),(780,0,10,550),1)
    muro_a =pygame.draw.rect(background,(0,0,0),(30,220,60,1),1)
    muro_b =pygame.draw.rect(background,(0,0,0),(30,200,60,1),1)
    muro_d =pygame.draw.rect(background,(0,0,0),(87,201,1,1),1)
    muro2_a =pygame.draw.rect(background,(0,10,0),(160,220,20,1),1)
    muro2_b =pygame.draw.rect(background,(0,0,0),(172,205,45,1),1)
    muro2_i =pygame.draw.rect(background,(0,0,0),(150,199,1,1),1)
    lado=pygame.draw.rect(background,(0,100,100),(215,145,1,60),1)
    lado_1_a=pygame.draw.rect(background,(0,100,100),(235,145,1,60),1)
    tronco_a=pygame.draw.rect(background,(0,0,0),(190,195,20,1),1)
    tronco_i=pygame.draw.rect(background,(0,0,0),(185,197,5,5),1)
    murito_a=pygame.draw.rect(background,(0,0,0),(10,290,55,1),1)
    murito_d=pygame.draw.rect(background,(0,0,0),(75,290,1,60),1)
    centro_i=pygame.draw.rect(background,(0,0,0),(196,310,1,40),1)
    centro_a=pygame.draw.rect(background,(0,0,0),(196,310,35,1),1)
    centro_d=pygame.draw.rect(background,(0,0,0),(230,310,1,40),1)
    lado_2=pygame.draw.rect(background,(0,0,0),(235,65,1,60),1)
    lado_2_a=pygame.draw.rect(background,(0,0,0),(255,65,1,60),1)
    lado_3=pygame.draw.rect(background,(0,0,0),(235,120,3,1),1)
    lado_4=pygame.draw.rect(background,(0,0,0),(255,45,15,1),1)
    lado_5=pygame.draw.rect(background,(0,0,0),(345,25,45,1),1)
    lado_6=pygame.draw.rect(background,(0,0,0),(405,35,50,1),1)
    lado_7=pygame.draw.rect(background,(0,0,0),(465,55,1,1),1)
    lado_8=pygame.draw.rect(background,(0,0,0),(485,85,1,1),1)
    lado_9=pygame.draw.rect(background,(0,0,0),(500,110,1,50),1)
    lado_9_a=pygame.draw.rect(background,(0,0,0),(480,110,1,50),1)
    lado_10=pygame.draw.rect(background,(0,0,0),(495,195,1,1),1)
    lado_11=pygame.draw.rect(background,(0,0,0),(460,210,1,1),1)
    lado_12=pygame.draw.rect(background,(0,0,0),(440,230,1,20),1)
    lado_12_a=pygame.draw.rect(background,(0,0,0),(410,230,1,20),1)
    lado_13=pygame.draw.rect(background,(0,0,0),(420,280,1,1),1)
    lado_14=pygame.draw.rect(background,(0,0,0),(357,290,1,1),1)
    lado_15=pygame.draw.rect(background,(100,100,0),(355,300,1,55),1)
    lado_15_a=pygame.draw.rect(background,(100,100,0),(335,300,1,55),1)
    lado_16=pygame.draw.rect(background,(0,0,0),(720,250,1,85),1)
    lado_17=pygame.draw.rect(background,(0,0,0),(720,280,25,1),1)
    lado_18=pygame.draw.rect(background,(0,0,0),(690,220,1,15),1)
    lado_19=pygame.draw.rect(background,(0,0,0),(670,235,55,1),1)
    lado_20=pygame.draw.rect(background,(0,0,0),(640,140,1,65),1)
    lado_21=pygame.draw.rect(background,(0,0,0),(650,140,12,1),1)
    lado_22=pygame.draw.rect(background,(0,0,0),(625,70,1,65),1)
    lado_23=pygame.draw.rect(background,(0,0,0),(585,80,50,1),1)
    lado_24=pygame.draw.rect(background,(0,0,0),(560,0,1,65),1)
    lado_25=pygame.draw.rect(background,(0,0,0),(410,30,5,5),1)
else:
    background = pygame.image.load("primer_piso.png")
    rectangulo=pygame.draw.rect(background ,(50,210,0),(75,303,260,35),1)
    rectangulo_1=pygame.draw.rect(background ,(50,210,0),(60,62,40,235),1)
    rectangulo_2=pygame.draw.rect(background ,(50,210,0),(690,62,40,235),1)
    rectangulo_3=pygame.draw.rect(background ,(50,210,0),(75,25,636,35),1)
    rectangulo_4=pygame.draw.rect(background ,(50,210,0),(450,303,260,35),1)
    salida_p=pygame.draw.rect(background ,(50,210,0),(355,320,75,15),1)
    subida =pygame.draw.rect(background,(50,210,0),(620,95,60,50),1)
    lado_1_1=pygame.draw.rect(background,(50,210,0),(635,110,40,0),1)


"""La clase player, los
argumentos que recibe son: Coordenadas, velocidad e imagen para tomar los
sprites respectivamente"""
#enemy = enemy.Enemy((105,60),5,"Skeleton_1.png")
#boss = boss.Boss((370,60),0,"Boss_1.png")

"""Pause: """

pause_menu = pygame.image.load("Pause_1.png")

def Button(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords[0]+190,coords[1]
    #surface.blit(image,coords)
    return (image,imagerect)



start = False

game_over = False

pause = True

white = (255,255,255)

main_f = False

skeleton = enemy_1.Enemy(300, 200, 64, 64, 370)
skeleton_2 = enemy_1.Enemy(200, 200, 64, 64, 270)

skeleton_c=skeleton.hitbox
player_c=player.rect
def load_music(song):
    """Carga una cancion"""
    pygame.mixer.music.load(song)
def play_music():
    """Inicia la cancion """
    pygame.mixer.music.play(-1) #El -1 reproduce la canci�n en bucle
def pause_music():
    pygame.mixer.music.pause()
def unpause_music():
    pygame.mixer.music.unpause()

load_music("Spring-Village.mp3")
#play_music()

def exit():
    pygame.quit()
    quit()

def not_pause():
    """Establece pause como False """
    global pause
    pause = False
def b_main_f():
    if main_f == True:
        screen.blit(b_main[0],b_main[1])
def paused():

    out = False

    """// Suspende el juego y abre el menu de pausa con las opciones "Main Menu",
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
                main_f = False
            else:
                main_f = False
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
                        not_pause()
                        unpause_music()

                    if b_end[1].collidepoint(mouse):
                        exit()

        pygame.display.update()
        clock.tick(20)


while start:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



while game_over == False:
    #print(enemy.rect.x)
    screen.blit(background,(0,0)) #Aqu� se carga la im�gen de fondo
    #print(skeleton.x)
    for event in pygame.event.get():
        """Evalua si se presion� el boton de cerrar el juego, de ser as�, se
        terminar� la ejecuci�n del mismo"""
        if event.type == pygame.QUIT:
            game_over = True

    #enemy.handle_event(event)
    #screen.blit(enemy.image, enemy.rect)
    #skeleton_3.draw(screen)
    skeleton.draw(screen)
    skeleton_2.draw(screen)

    player.handle_event(event)
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    """clock.tick() determina la velocidad base del personaje, acualizando Clock
    en milisegudos """

    clock.tick(20)
    if player.rect.colliderect(skeleton.hitbox)==True: #detectamos si el enemigo y el jugador estan en contacto
            if (skeleton.life>0):
                if (player.direction==1 and player.attack==2):#si el jugador esta atacando le resta vida al esqueleto
                    skeleton.life -= 1
                elif(player.direction == 3 and player.attack==4):
                    skeleton.life -= 1
                elif(player.direction == 3 and player.attack==0 ):#si el jugador no esta atacando, le resta vida al jugador
                    player.life -= 1
                elif(player.direction == 1 and player.attack == 0):
                    player.life -= 1
                print("the skeleton life is: ",skeleton.life)#imprimimos ambas vidas
                print("your life is: ",player.life)


    if player.fondo ==1:
        if (rectangulo.colliderect(player.rect) and player.direction ==2)  or (rectangulo_1.colliderect(player.rect) and player.direction == 3 )or (rectangulo_2.colliderect(player.rect) and player.direction == 1 ) or (rectangulo_3.colliderect(player.rect) and player.direction ==0):
            player.speed=0

        elif (salida.colliderect(player.rect) and player.direction ==1 and player.rect[1] <= (salida.y +10)) :
            print("saliste")
        elif(lado_1_1.colliderect(player.rect) and player.direction ==0 ):
            player.speed=0


        else:
            player.speed=5


    elif player.fondo ==2 :
        #if (salida.colliderect(player.rect) and player.direction==0):
            #player.fondo=1
        if (lado_i.colliderect(player.rect) and player.direction==3 ):
            player.speed = 0
        #elif (muro.colliderect(player.rect) and (player.direction == 2)):
        #    player.rect[0] -10
        elif(lado_a.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_b.colliderect(player.rect) and (player.direction ==2)):
            player.speed=0
        elif(lado_d.colliderect(player.rect) and (player.direction == 1)):
            player.speed=0
        elif(muro_a.colliderect(player.rect) and (player.direction ==2) and player.rect[1] < (muro_a.y-20)):
            player.speed=0
        elif(muro_b.colliderect(player.rect ) and (player.direction==0) and player.rect[1] > (muro_b.y - 20)):
            player.speed=0
        elif(muro_d.colliderect(player.rect) and (player.direction ==3)):
            player.speed=0
        elif(tronco_a.colliderect(player.rect) and (player.direction ==2)):
            player.speed=0
        elif(muro2_b.colliderect(player.rect ) and (player.direction==0) and player.rect[1] > (muro2_b.y - 20)):
            player.speed=0
        elif(muro2_i.colliderect(player.rect) and (player.direction ==1) and player.rect[0] > (muro2_i.x +20)):
            player.speed=0
        elif(muro2_a.colliderect(player.rect) and (player.direction ==2)and player.rect[0] < (muro2_a.x - 10) ):
            player.speed=0
        elif(tronco_i.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(murito_a.colliderect(player.rect) and (player.direction ==2)):
            player.speed=0
        elif(murito_d.colliderect(player.rect) and (player.direction == 3)):
            player.speed=0
        elif(centro_i.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(centro_a.colliderect(player.rect) and (player.direction ==2)):
            player.speed=0
        elif(centro_d.colliderect(player.rect) and (player.direction ==3)):
            player.speed=0
        elif(lado.colliderect(player.rect) and (player.direction == 3)and player.rect[0] > (lado.x -20)):
            player.speed=0
        elif(lado_1_a.colliderect(player.rect) and (player.direction == 1)and player.rect[0] < (lado_1_a.x -20)):
            player.speed=0
        elif(lado_2.colliderect(player.rect) and (player.direction == 3) and player.rect[0] > (lado_2.x - 25)):
            player.speed=0
        elif(lado_2_a.colliderect(player.rect) and (player.direction == 1) and player.rect[0] < (lado_2_a.x -20) ):
            player.speed=0
        elif(lado_3.colliderect(player.rect) and (player.direction == 0) and player.rect[0] > (lado.x -5)):
            player.speed=0
        elif(lado_4.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_5.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_6.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_7.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_8.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_9.colliderect(player.rect) and (player.direction ==1 and (player.rect[0] < (lado_9.x - 25)))):
            player.speed=0
        elif(lado_9_a.colliderect(player.rect) and (player.direction ==3 and (player.rect[0] > (lado_9_a.x - 25)))):
            player.speed=0
        elif(lado_10.colliderect(player.rect) and (player.direction ==2) and (player.rect[1] < (lado_10.y - 20))):
            player.speed=0
        elif(lado_11.colliderect(player.rect) and (player.direction ==2) and player.rect[1] < (lado_11.y - 40)):
            player.speed=0
        elif(lado_12.colliderect(player.rect) and (player.direction ==1) and player.rect[0] < (lado_12.x -25) ):
            player.speed=0
        elif(lado_12_a.colliderect(player.rect) and (player.direction ==3) and player.rect[0] > (lado_12_a.x -25) ):
            player.speed=0
        elif(lado_13.colliderect(player.rect) and (player.direction ==2) and (player.rect[1] < (lado_13.y - 28))):
            player.speed=0
        #elif(lado_14.colliderect(player.rect) and (player.direction ==2)):
        #    player.speed=0
        elif(lado_15.colliderect(player.rect) and (player.direction ==1) and (player.rect[0] < (lado_15.x - 20))):
            player.speed=0
        elif(lado_15_a.colliderect(player.rect) and (player.direction ==3) and (player.rect[0] > (lado_15_a.x -20))):
            player.speed=0
        elif(lado_16.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(lado_17.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0

        elif(lado_18.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(lado_19.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_20.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(lado_21.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_22.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(lado_23.colliderect(player.rect) and (player.direction ==0)):
            player.speed=0
        elif(lado_24.colliderect(player.rect) and (player.direction ==1)):
            player.speed=0
        elif(lado_25.colliderect(player.rect) and (player.direction ==3)):
            player.speed=0


        else:
            player.speed=5

    else:
        if (rectangulo.colliderect(player.rect) and player.direction ==2)  or (rectangulo_1.colliderect(player.rect) and player.direction == 3 )or (rectangulo_2.colliderect(player.rect) and player.direction == 1 ) or (rectangulo_3.colliderect(player.rect) and player.direction ==0):
            player.speed=0
        elif (rectangulo_4.colliderect(player.rect) and player.direction ==2):
            player.speed=0
        elif (salida_p.colliderect(player.rect) and player.direction ==2):
            print("saliste al patio")
        elif (subida.colliderect(player.rect) and player.direction ==1 and player.rect[1] <= (subida.y +10)) :
            print("subiste")
        elif(lado_1_1.colliderect(player.rect) and player.direction ==0 ):
            player.speed=0
        else:
            player.speed=5



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
            pause_music()
            pause = not pause
            paused()



load_music("Spring-Village.mp3")
#play_music()

pygame.quit ()
