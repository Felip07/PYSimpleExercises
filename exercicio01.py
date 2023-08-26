#Resposta 01

altura = float (input("Digite a sua altura (em metros):"))
altura = altura * 100
print(f"Sua altura é de {altura}cm")

#Resposta 02

delta_s = float (input("Digite o deslocamento (em metros):"))
delta_t = float (input("Digite o tempo (em segundos):"))
velocidade = delta_s / delta_t
print(f"Vm = {velocidade:.2f} m/s")

#Resposta 03

from math import pi
#utilização da bibliotecas math e pi
raio = float(input("Digite o raio da área: "))
#area = pi * raio ** 2
area = pi * pow(raio,2)
print(f"Area = {area:.2f}")