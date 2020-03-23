from tkinter import*

def afficheGrille(can):
    for j in range (1, 10):
        can.create_line(100*j,100,100*j,900)
        can.create_line(100,100*j,900,100*j)

def creertableau(tab):
    for j in range(0,9):
        ligne=[]
        for i in range(0,9):
            ligne.append(0)
        tab.append(ligne)
    #for j in range(0,9):
        #print(tableau[j])

def affichagepions():
    for j in range (0,9):
        for i in range (0,9):
            if tableau[j][i]>0:
                if tableau[j][i]==2:
                    cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='white')
                else:
                    cani.create_oval((j*100+50),(i*100+50),(j*100+150),(i*100+150),fill='black')

def callback(event):
    print("clicked at", event.x, event.y)
    remplirtableaudist2(tableaudist,event)
    zemin = min(list(map(min, tableaudist)))
    print(zemin)
    lignemin = list(map(min, tableaudist)).index(zemin)
    print(lignemin)
    colonnemin = tableaudist[lignemin].index(zemin)
    print(colonnemin)
    tableau[lignemin][colonnemin]=((tableau[lignemin][colonnemin])+1)
    affichagepions()
    
def remplirtableaudist2(tab,event):
    for j in range(0,9):
        for i in range(0,9):
            tab[j][i]=(((event.x-(100+(j*100)))*(event.x-(100+(j*100))))+((event.y-(100+(i*100)))*(event.y-(100+(i*100)))))
    for j in range(0,9):
        print(tab[j])
    
#def valmin ():
 #   for j in range(0,9):
  #      for i in range(0,9):
            

tableau=[]
tableaudist=[]
master = Tk()

cani = Canvas(master, width=1000, height=1000,bg='grey80')
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')

afficheGrille(cani)
creertableau(tableaudist)
creertableau(tableau)
tableau[1][2]=1
tableau[3][2]=2
tableau[3][8]=2
          
affichagepions()

cani.bind("<Button-1>", callback)



