#18-5-2020

#VENTANA DE JUEGO
import pygame
import math
import random
from pygame import mixer #para meter musiquita




#Inicia pygame
pygame.init() #obligatoria

#Creación de la pantalla (tamaño)
screen = pygame.display.set_mode((800,600)) #ancho (x) por alto (y). El origen está en la esquina superior izquierda.
                                            #El eje X es positivo hacia la derecha y el eje Y es positivo hacia abajo.

#TÍTULO E ICONO DE LA VENTANA DE JUEGO

pygame.display.set_caption("Space Invaders")
    #Ve a flaticon.com, busca el icono que quieras, dale a descargar en formato PNG y tamaño 32. En la web pone que
    #tengo que dar créditos al autor, así que aquí van:
        #Icons made by <a href="https://www.flaticon.com/authors/icongeek26" title="Icongeek26">Icongeek26</a>
        #from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon = pygame.image.load('nature.png')
pygame.display.set_icon(icon)

#MÚSICA DE FONDO
mixer.music.load('background.wav')
mixer.music.play(-1) #en bucle
#El sonido de las balas está en el código de las teclas.

#AÑADIR IMÁGENES
    #Puedes coger fotos en flaticon.com o en freepik.com. Me he hecho cuenta en ambas con el correo basurillas.

        #<a href="https://www.freepik.es/fotos-vectores-gratis/fondo">Vector de Fondo creado por pikisuperstar
        # - www.freepik.es</a>

#Fondo
fondo = pygame.image.load('fondo.png')



        #Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a>
        #from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#Jugador
playerImg = pygame.image.load('game.png')
playerX = 370 #posición de la imagen en eje X
playerY = 480 #posición de la imagen en eje Y

playerX_change = 0

#def player():
    #screen.blit(playerImg,(playerX,playerY)) #blit es dibujar. Después de cargar la imagen, tienes que dibujarla en la pantalla,
                                            #dándole las coordenadas
def player(x,y):
    screen.blit(playerImg,(x,y))


            #Icons made by <a href="https://www.flaticon.com/authors/phatplus" title="phatplus">phatplus</a>
            #from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#Enemy
#Como quiero varios enemigos, hago una lista vacía.
enemyImg= []
enemyX= []
enemyY= []
enemyX_change= []
enemyY_change= []
num_enemigos= 4
for i in range(num_enemigos):

    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735)) #posición de la imagen en eje X. Queremos un valor de inicio (primera coordenada) y un
                                    #valor de final (segunda coordenada). Sería 736 porque 800-64 (píxeles) es 736, pero
                                    #para asegurarnos ponemos 735.
    enemyY.append(random.randint(50,150)) #posición de la imagen en eje Y

    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


            #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from
            #<a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#Bala

    #Ready-no puedes ver la bala en la pantalla
    #Fuego-la bala se está moviendo

balaImg = pygame.image.load('carrot.png')
balaX = 0 #posición de la imagen en eje X. Queremos un valor de inicio (primera coordenada) y un
                                #valor de final (segunda coordenada).
balaY = 480 #la bala sale de mi nave, tiene que estar a su altura

balaX_change = 0
balaY_change = 10
bala_state = "ready"

def lanza_bala(x,y):
    global bala_state
    bala_state= "fuego"
    screen.blit( balaImg, (x+16 , y+10) ) #para que esté un poco separada del icono de la nave y en el medio de la nave

#MOVIMIENTO DEL JUEGO

    #Mi icono de jugador está en x=370. Si, por ejmplo, quiero que se mueva 5 píxeles a la derecha, su nueva posición será
    #375. Es trivial, pero bueno. Esto se aplica a arriba, abajo, derecha e izquierda, en X o Y, según corresponda.
    #Ojo, tiene que verse movimiento, no teletransportación, o sea que tiene que haber un aumento o disminución de
    #coordenadas "incremental" O "progresivo", no instantáneo.

    #Quiero que el enemigo se mueva aleatoriamente en x y en y.

#COLISIÓN
    #Calculo la distancia entre la bala y el enemigo con la ecuación d=sqrt( (x2-x1)^2 + (y2-y1)^2 ).
    #Para meter ecuaciones, tenemos que importar el pip math.

def isColision(enemyX, enemyY, balaX, balaY):
    distancia= math.sqrt( math.pow(enemyX-balaX,2) + math.pow(enemyY-balaY,2) )
    if distancia< 27:
        return True
    else:
        return False
#Esto significa que, si la distancia es menor de 27, ha ocurrido colisión.


#PUNTUACIÓN
puntuacion_valor=0
font= pygame.font.Font('pixel.ttf', 32) #fuente y tamaño. freesansbold.ttf es la fuente por defecto en pygame, si quieres más,
                                                #te las tienes que descargar en dafont.com
textX= 10 #posición de la puntuación
textY= 10

def muestra_puntuacion(x,y):
    puntuacion = font.render("Puntuación: " + str(puntuacion_valor), True, (255,255,255))
        #qué texto sale en pantalla, true, de qué color (rgb)
    screen.blit(puntuacion, (x,y))

#GAME OVER
game_over_font= pygame.font.Font('pixel.ttf',64)
textoX=200
textoY=250
def game_over_text():
    the_end = game_over_font.render("HAS PERDIDO", True, (255,255,255))
    screen.blit(the_end, (textoX,textoY))

#BUCLE DEL JUEGO
running = True
while running:

    #Lo que quiero que persista en la pantalla, lo tengo que meter en este bucle.

    screen.fill((0, 0, 0))  # das valores del color en RGB (red, green, blue)
    screen.blit(fondo,(0,0)) #para cambiar la imagen de fondo. Ojo, es muy pesada y hace que to-do vaya muy despacio.
    #playerX -= 0.1 #si metes el cambio de coordenada en el bucle, va "despacito"

    #Los eventos que van a ocurrir en la ventana de juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #TECLAS

        # Si se pulsa una tecla (keystroke), comprueba si es derecha o izquierda.
        if event.type == pygame.KEYDOWN: #tecla abajo (pulsada)
            #print ("Se está pulsando alguna tecla")
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                #print("La flecha izquierda está siendo pulsada")
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
                #print("La flecha derecha está siendo pulsada")
            if event.key == pygame.K_SPACE:
                if bala_state is "ready": #para no poder disparar una bala nueva hasta que la primera cruce la pantalla
                    bala_sonido= mixer.Sound('laser.wav')
                    bala_sonido.play()
                    balaX= playerX #queremos que la bala salga de la nave, pero que no la siga
                    lanza_bala(balaX,balaY)

        if event.type == pygame.KEYUP:  # tecla arriba (no pulsada)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 #se para
                #playerX_change = 0.1 #esto sigue avanzando a la derecha aunque tú no pulses nada. So annoying.
                #print("Se ha dejado de pulsar alguna tecla")


    #FRONTERAS
    #para que no se me salga de la pantalla

    #Jugador
    playerX += playerX_change  # poisición en x = posición inicial en x + incremento/decremento en x.
    if playerX <=0:
        playerX = 0
    elif playerX >=736: #hay que tener en cuenta el tamaño de la imagen (64 píxeles), 800-64= 736.
        playerX = 736

    #Movimiento del enemigo
    for i in range(num_enemigos):

        #GAME OVER
        if enemyY[i] > 440:
            for j in range(num_enemigos):
                enemyY[j]= 2000 #para que se baje a la mierda
            game_over_text()
            break

         #________________________

        enemyX[i] += enemyX_change[i] #como mis matrices de matlab
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i] #cuando toca el borde, se mueve hacia abajo
        elif enemyX[i] >= 735:  # hay que tener en cuenta el tamaño de la imagen (64 píxeles), 800-64= 736.
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        #Colisión
        colision = isColision(enemyX[i], enemyY[i], balaX, balaY)
        if colision:
            explosion_sonido = mixer.Sound('explosion.wav')
            explosion_sonido.play()
            balaY = 480  # devuelve la bala a su sitio inicial
            bala_state = "ready"
            puntuacion_valor += 1
            enemyX[i] = random.randint(0, 735)  # cuando das al enemigo, se vuelve hacia atrás
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Movimiento de la bala
    if balaY<=0:
        balaY= 480 #para resetear la bala
        bala_state = "ready"

    if bala_state is "fuego":
        lanza_bala(balaX,balaY)
        balaY -= balaY_change


    player(playerX,playerY) #después del llenado de pantalla.
    muestra_puntuacion(textX,textY)
    pygame.display.update() #obligatoria




