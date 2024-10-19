numeroSecreto = 5
tentativasMaximas = 3
cont = 0

while cont < tentativasMaximas:
    palpite = int(input("Adivinhe um número entre 1 e 10:"))
    cont += 1

    if palpite == numeroSecreto:
        print("Você acertou o sorteado!")
        break
else:
    print(f"Você esgotou as tentativas! O número era {numeroSecreto}")
