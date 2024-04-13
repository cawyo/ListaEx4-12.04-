valor = int(input("Digite um número entre 1 e 10: "))

while valor<1 or valor>10:
    valor = int(input("Digite um número válido: "))

print("//////")

for a in range(1,11):
    print(f"{valor}x{a}={valor*a}")

print("//////")