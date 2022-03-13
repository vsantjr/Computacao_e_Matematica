# Computação e Matemática
# Santiago

# Pygame: biblioteca de jogos multiplataforma (independente de sistema 
# operacional) feita para ser utilizada em conjunto com a linguagem de
# programação python. 

import pygame
pygame.init()

dis = pygame.display.set_mode((500, 500))
x = 50
y = 50
altura = 40
comprimento = 100
rodar= True
clock = pygame.time.Clock()
direcao = 'Direita'
color = (0, 127, 255)

def animar(x, y, altura, comprimento, direcao, vel):
    if x < 0:
        direcao = 'Direita'

    elif x > 500:
        direcao = 'Esquerda'

    if direcao == 'Direita':
        x += vel
        if (y > 0) and (y < 500):
           y += 10
        else:
          y = 50   
    elif direcao == 'Esquerda':
        x -= vel
        if (y > 0) and (y < 500):
           y += 10
        else:
           y = 50 

    
    pygame.draw.rect(dis, color, pygame.Rect(x, y, comprimento, altura))

    return x, y, direcao

vel = float(input('Digite a velocidade: '))
cnt = 0
while rodar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False
    keys = pygame.key.get_pressed()

    dis.fill((0, 0, 0))


    x, y, direcao = animar(x, y, altura, comprimento, direcao, vel)
    pygame.display.flip()
    clock.tick(60)

    cnt+=1
    if (cnt > 300):
       vel = float(input('Digite a velocidade: '))
       cnt = 0
pygame.quit()