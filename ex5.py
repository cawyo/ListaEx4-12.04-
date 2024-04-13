numsP = []
numsI = []

for a in range(1,11):
    novoNum=int(input(f"Digite o {a}º número: "))
    if novoNum%2==0:
        numsP.append(novoNum)
    else:
        numsI.append(novoNum)

print(f"//////////////\nExistem {len(numsP)} números pares e eles são:\n{numsP}")
print(f"Existem {len(numsI)} números impares e eles são:\n{numsI}")