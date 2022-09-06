import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Tamanho da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#movimentação
x = 0
y = 0

relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Persongem
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 40))

    #Moeda
    pygame.draw.circle(tela, (0, 255, 255), (300, 200), 5)

    y = y + 1
    if y >= altura:
        y = 0

    pygame.display.update()
