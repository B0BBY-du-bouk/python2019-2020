
from tkinter import*

def creertableau(tab): #pour créer un tableau de valeur 
    for j in range(0,9):
        ligne=[]
        for i in range(0,9):
            ligne.append(0)
        tab.append(ligne)
     #pour afficher le tableau
        #print()

def affichagepions(): #la fonction qui place les points sur la grille, ce sont des canevas qu'il faut remplacer par des widgets
    for j in range (0,9):
        for i in range (0,9):
            if tableau[j][i]>0:
                if tableau[j][i]==2:
                    tableaugraphique[j][i]=cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='white')
                else:
                    tableaugraphique[j][i]=cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='black')
                    print  (tableaugraphique[j][i])

    
def afficheGrille(can): #la fonction qui créer la grille de jeu
    for j in range (1, 10):
        can.create_line(100*j,100,100*j,900)
        can.create_line(100,100*j,900,100*j)
        
master = Tk()
tableaugraphique = []
tableau = []
cani = Canvas(master, width=1000, height=1000,bg='grey80') #on créer le "plateau de jeu"
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')
creertableau(tableaugraphique)
creertableau(tableau)
afficheGrille(cani) #on affiche la grille

tableau[8][8]=1
tableau[0][0]=2
tableau[1][1]=1
tableau[3][2]=2
tableau[3][1]=1
affichagepions()
#tableaugraphique[1][1].destroy()
#affichagepions()

cani.delete(tableaugraphique[1][1])
