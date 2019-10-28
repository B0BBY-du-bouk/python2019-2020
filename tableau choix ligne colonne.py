testta=[]
nombredeligne=input("entre nb ligne")

nombredecolonne=input("entre nb colonne")
print(nombredecolonne)
for j in range(1, int(nombredeligne)):
    tampon=[]
    for i in range(int(nombredecolonne)):
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)-1):
    print(testta[j])
