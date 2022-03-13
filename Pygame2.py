# Computação e Matemática
# Santiago

# Pygame: biblioteca de jogos multiplataforma (independente de sistema 
# operacional) feita para ser utilizada em conjunto com a linguagem de
# programação python. 

import pygame
pygame.init()

# Desenha uma casa
def desenharCasa(x, y, comp, alt, t, cor):
    pontos = [(x,y- ((2/3.0) * alt)), (x,y), (x+comp,y), (x+comp,y-(2/3.0) * alt), 
        (x,y- ((2/3.0) * alt)), (x + comp/2.0,y-alt), (x+comp,y-(2/3.0)*alt)]
    pygame.draw.lines(t, cor, False, pontos, 4)


# Definindo variáveis de acordo com as cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
amarelo = (225, 255, 00)

# Configurando a janela e preenchendo-a com preto
tela = pygame.display.set_mode([650, 650])
tela.fill(preto)

rodar = True
while rodar:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False

    # Quadrado
    pygame.draw.rect(tela, vermelho, pygame.Rect(50, 30, 70, 70))

    # Retângulo
    pygame.draw.rect(tela, verde, pygame.Rect(50, 170, 70, 35))
    
    # Trapézio
    pygame.draw.lines(tela, azul, True, [(50,400), (170,400), (120,300), (70, 300)], 5)
    
    # Desenhar casa
    desenharCasa(50, 600, 150, 100, tela, amarelo)
    
    pygame.display.flip()

pygame.quit()