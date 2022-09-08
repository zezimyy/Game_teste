import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Tamanho da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#movimentação
x_player = largura / 2
y_player = altura / 2

#moedaX,y
x_coin = randint(40, 600)
y_coin = randint(40, 440)

relogio = pygame.time.Clock()

#Pontos
pontos = 0
#Fonte para pontos
fonte = pygame.font.SysFont("arial", 30, False, False)

while True:
    #fps
    relogio.tick(15)
    tela.fill((0, 0, 0))

    #Mensagem na tela
    mensagem = f"pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Persongem
    player = pygame.draw.rect(tela, (255, 0, 0), (x_player, y_player, 40, 40))

    #Moeda
    coin = pygame.draw.circle(tela, (0, 255, 255), (x_coin, y_coin), 5)

    #esquerda
    if pygame.key.get_pressed()[K_a]:
        x_player = x_player - 10
    #direita
    if pygame.key.get_pressed()[K_d]:
        x_player = x_player + 10
    #cima
    if pygame.key.get_pressed()[K_w]:
        y_player = y_player - 10
    #baixo
    if pygame.key.get_pressed()[K_s]:
        y_player = y_player + 10

    #pegar moeda
    if player.colliderect(coin):
        x_coin = randint(40, 600)
        y_coin = randint(40, 440)
        pontos = pontos + 1

    #Mostrar msg na tela
    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()
