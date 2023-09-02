#ESTRUTURA DE DECISÃO

#Exemplo de calculo de média (2 notas)
nota1 = int(input("Informe a nota do bimestre 1 (0-10): "))
nota2 = int(input("Informe a nota do bimestre 2 (0-10): "))
media = (nota1 + nota2)/2

#Estrutura de decisão IF
if media >= 6 :
    print("Aprovado")
else :
    print("Reprovado")