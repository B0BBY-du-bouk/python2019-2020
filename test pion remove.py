
from tkinter import* #on appel TKinter

def afficheGrille(can): #la fonction qui créer la grille de jeu
    for j in range (1, 10):
        can.create_line(100*j,100,100*j,900)
        can.create_line(100,100*j,900,100*j)

def creertableau(tab): #pour créer un tableau de valeur 
    for j in range(0,9):
        ligne=[]
        for i in range(0,9):
            ligne.append(0)
        tab.append(ligne)
    #for j in range(0,9): #pour afficher le tableau
        #print(tableau[j])

def affichagepions(): #la fonction qui place les points sur la grille, ce sont des canevas qu'il faut remplacer par des widgets
    for j in range (0,9):
        for i in range (0,9):
            if tableau[j][i]>0:
                if tableau[j][i]==2:
                    tableaugraphique[j][i]=cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='white')
                else:
                    tableaugraphique[j][i]=cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='black')
            
        
def remplirtableaudist2(tab,event): #fonction pour remplir le tableau des distances par rapport aux clics
    for j in range(0,9):
        for i in range(0,9):
            tab[j][i]=(((event.x-(100+(j*100)))*(event.x-(100+(j*100))))+((event.y-(100+(i*100)))*(event.y-(100+(i*100)))))
    #for j in range(0,9):
        #print(tab[j])
    
def trouvervaleurmin ():#trouve la valeur min du tableau des distances puis l'associe au tableau des pionts pour ajouter une valeur au pions
    zemin = min(list(map(min, tableaudist)))#map cherche le minimum de chaque ligne de tableaudist, ensuite les minimums sont mis dans une liste, puis le minimum total est le minimum de cette dernière list
    #print(zemin)
    lignemin = list(map(min, tableaudist)).index(zemin) #je cherche les coordonées du minimum en commencen par la ligne
    #print(lignemin)
    colonnemin = tableaudist[lignemin].index(zemin) #puis la colonne
    #print(colonnemin)
    tableau[lignemin][colonnemin]=((tableau[lignemin][colonnemin])+1) #j'ajoute 1 à la valeur de la case pour changer la valeur du pion
    cani.delete(tableaugraphique[lignemin][colonnemin])
    if tableau[lignemin][colonnemin]>2: #je remet le conteur de la case à 0 (vide) au cas ou elle est supèrieur à 2 (blanc)
        tableau[lignemin][colonnemin]=0
        tableaugraphique[lignemin][colonnemin]=0
        cani.delete(tableaugraphique[lignemin][colonnemin])
        
def callback(event): #je programme l'action qui doit être prise à chaque clic
    #print("clicked at", event.x, event.y)
    remplirtableaudist2(tableaudist,event)
    trouvervaleurmin()
    affichagepions()

tableau=[] #le tableau des valeurs des pions
tableaudist=[] #le tableau qui va accueillir les distances des cases par rapport au clic
master = Tk() #on créé la fenetre de jeu
tableaugraphique = []

cani = Canvas(master, width=1000, height=1000,bg='grey80') #on créer le "plateau de jeu"
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')

afficheGrille(cani) #on affiche la grille
creertableau(tableaudist) #on transforme les tableaux en tableaux
creertableau(tableau)
creertableau(tableaugraphique)

affichagepions()#on affiche les pions



cani.bind("<Button-1>", callback) #on clic comme on veut


