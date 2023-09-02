#Exemplo 2 - Algoritmo para solicitação de emprestimo

print("Programa de empréstimos ## Responda: (0 - Não e 1 - Sim)")
nomeNegativado = int(input("Possui nome negativado? "))
if nomeNegativado == 1 :
    print("Não pode realizar emprestimo")
else :
    carteiraAssinada = int(input("Possui carteira assinada? "))
    if carteiraAssinada == 0 :
        print("Não pode realizar emprestimo")
    else :
        CasaPropria = int(input("Possui casa própria? "))
        if CasaPropria == 0 :
            print("Não pode realizar empréstimo")
        else :
            print("Conceder empréstimo")
        