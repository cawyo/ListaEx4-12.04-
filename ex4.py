idades=[]
novaIdade=1
while True:
    novaIdade = int(input("Digite uma idade (em anos) ou 0 para a média: "))
    if novaIdade == 0:
        break
    if novaIdade<0:
        print("Número negativo convertido em 1")
        novaIdade=1
    idades.append(novaIdade)
    print(idades)

media= sum(idades)/len(idades)

print(f"/////////\n{idades}\nA média é: {media}")