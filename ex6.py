nums1 = []
nums2 = []

for a in range(1,11):
    novoNum=int(input(f"Digite o {a}º número: "))
    if novoNum>=10 and novoNum<=20:
        nums1.append(novoNum)
    else:
        nums2.append(novoNum)

print(f"//////////////\nExistem {len(nums1)} números dentre 10 e 20 e eles são:\n{nums1}")
print(f"Existem {len(nums2)} números fora de 10 e 20 e eles são:\n{nums2}")