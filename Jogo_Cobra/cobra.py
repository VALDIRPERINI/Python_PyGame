import pygame as pg 
from pygame.locals import *
from sys import exit
from random import randint

pg.init()

# Variáveis
largura = 800
altura = 640
x = largura/2
y = altura/2
x_azul = randint(40, 760)
y_azul = randint(40, 600)

# Pontuação
fonte = pg.font.SysFont('arial', 40, True, True)
pontos = 0

# Canvas
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('JOGO DO VALDIR PERINI')
relogio = pg.time.Clock()

while True:
    # CONTROLA A VELOCIDADE DE FRAME
    relogio.tick(20)
    # PINTA A TELA DE PRETO A CADA FRAME
    tela.fill((0, 0, 0))
    mensagem = f'Points: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            exit()

    if pg.key.get_pressed()[K_a]:
        x = x - 20
    if pg.key.get_pressed()[K_d]:
        x = x + 20
    if pg.key.get_pressed()[K_w]:
        y = y - 20
    if pg.key.get_pressed()[K_s]:
        y = y + 20

# DESENHA UM RETANGULO
    quad_vermelho = pg.draw.rect(tela, (255, 0, 0), (x, y, 40, 40))
    quad_azul = pg.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 40))

    if quad_vermelho.colliderect(quad_azul):
        x_azul = randint(40, 760)
        y_azul = randint(40, 600)
        pontos = pontos + 1

    tela.blit(texto_formatado, (450, 40))

    pg.display.update()
