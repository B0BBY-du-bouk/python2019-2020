nbco = []
print(len(nbco))
print("===================")
nbli0 = []
nbli1 = []
nbli2 = []
nbli3 = []
nbco = [nbli0,nbli1,nbli2,nbli3]
print(nbco)
print("===================")
nbli0 = ["A","B","C","D"]
nbli1 = ["E","F","G","H"]
nbli2 = ["I","K","L","M"]
nbli3 = ["N","O","P","Q"]
print(nbco)
nbco = [nbli0,nbli1,nbli2,nbli3]
print(nbco)
print("===================")
# programme de creation de tableau V2 (liste de liste)
colonnes=["z","u","d","t","q","c","s"] #création de la liste des intitulés de colonnes
lignes= ["A","B","C","D"] # création de la liste des intitulés de lignes
tableau = [] #création de la liste finale car python ne peut pas travailler avec des noms (de variables) calculés
for j in lignes :
    tampon = [] #liste stockant provisoirement les lignes pour permettre la concaténation
    for i in colonnes :
        tampon.append(j+i)#concatenation de colonnes avec l'intitulé de ligne pour faire beau
    tableau.append(tampon )#reconstitue le tableau en tant que liste de liste

# pour vérifier le travail      
for j in range (len(lignes)):
    print (tableau[j]) 
print()# pour sauter une ligne   
print ("la case tableau[3][1] est :",tableau[3][1])# montre comment extraire le contenu d'une "case"
print("===================")
listcolo=["1","2","3","4"]
listlign=["A","B","C","D"]
tableau=[]
print(listcolo)
print(listlign)
print(tableau)
print("===================")
for j in listlign:
    tampon=[]
    for i in listcolo:
        tampon .append(j+i)
    tableau.append(tampon)
for j in range (len(listlign)):
    print (tableau[j])
print("===================")
tableau=[]
print(listcolo)
print(listlign)
print(tableau)
print("===================")
for j in listlign:
    tampon=[]
    for i in listcolo:
        tampon .append("_")
    tableau.append(tampon)
for j in range (len(listlign)):
    print (tableau[j])
print("===================")
testta=[]
testco=["2","a"]
nombredeligne=input("entre lenombre de lignes")
print (nombredeligne)
for j in range(1, int(nombredeligne)):
    tampon=[]
    for i in testco:
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)-1):
    print(testta[j])
print("===================")
for j in range(1, int(nombredeligne)):
    tampon=[]
    for i in testco:
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)):
    print(testta[j])
print("===================")
testta=[]
nombredecolonne=input("entre nb colo")
print(nombredecolonne)
for j in range(1, int(nombredeligne)):
    tampon=[]
    for i in range(int(nombredecolonne)):
        tampon.append("_")
    testta.append(tampon)
for j in range(0, int(nombredeligne)-1):
    print(testta[j])
