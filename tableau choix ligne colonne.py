testta=[]
nombredeligne=input("entre nb ligne")
print(nombredeligne)
nombredecolonne=input("entre nb colonne")
print(nombredecolonne)
for j in range(0, int(nombredeligne)):
    tampon=[]
    for i in range(int(nombredecolonne)):
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)):
    print(testta[j])
nombredeligne=input("changer le nombre de ligne c'est un ordre")
print(nombredeligne)
for j in range(0, int(nombredeligne)):
    tampon=[]
    for i in range(int(nombredecolonne)):
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)):
    print(testta[j])
testta=[]
nombredecolonne=input("et maintenant les colonnes")
print(nombredecolonne)
for j in range(0, int(nombredeligne)):
    tampon=[]
    for i in range(int(nombredecolonne)):
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)):
    print(testta[j])

