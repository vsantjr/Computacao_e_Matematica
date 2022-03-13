# Computação e Matemática
# Santiago

# Esse é um arquivo com as minhas funções
import math

def identificar_triangulo_lado(a, b, c):
  # \ => para colocar em múltiplas linhas
  tipo = ''
  if not ( (abs(b-c) < a) and (a < (b+c)) ) or \
     not ( (abs(a-c) < b) and (b < (a+c)) ) or \
     not ( (abs(a-b) < c) and (c < (a+b)) ):
       print("Triângulo não existe!")
       tipo = 'nao'
  else:
    if (a==b) and (b==c):
      print("Triângulo Equilátero!")
      tipo = 'equ'
    elif (a==b) or (b==c) or (c==a):
      print("Triângulo Isósceles!")
      tipo = 'iso'
    else:
      print("Triângulo Escaleno!") 
      tipo = 'esc'

  return tipo





def calcular_area_triangulo(a, b, c, t):
  area = -1
  if (t == 'equ'): # Equilátero
    # Base pode ser qualquer lado. Nesse caso, b.
    h = (b*math.sqrt(3))/2
    area = (b*h)/2
  else: # Fórmula de Heron: serve para qualquer área de qualquer triângulo, inclusive Equilátero.
    sp = (a + b + c)/2 # sp = semiperímetro
    area = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
  return area   