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
                    cani.create_oval((j*100+50),(j*100+50),(j*100+150),(j*100+150),fill='white')
                else:
                    cani.create_oval((j*100+50),(j*100+50),(j*100+150),(j*100+150),fill='black')

def callback(event):
    print("clicked at", event.x, event.y)
    remplirtableaudist2(tableaudist,event)
    
def remplirtableaudist2(tab,event):
    for j in range(0,9):
        for i in range(0,9):
            tab[j][i]=((event.x-(j*100)*event.x-(j*100))+(event.y-(i*100)*event.y-(i*100)))
    for j in range(0,9):
        print(tab[j])
    


tableau=[]
tableaudist=[]
master = Tk()

cani = Canvas(master, width=1000, height=1000,bg='grey80')
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')

afficheGrille(cani)
creertableau(tableaudist)
creertableau(tableau)
tableau[2][2]=1
tableau[3][3]=2
tableau[4][4]=2
          
affichagepions()

cani.bind("<Button-1>", callback)



