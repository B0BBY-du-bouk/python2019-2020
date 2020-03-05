from tkinter import*

def afficheGrille(can):
    for j in range (1, 10):
        can.create_line(100*j,100,100*j,900)
        can.create_line(100,100*j,900,100*j)

tableau=[]
master = Tk()

cani = Canvas(master, width=1000, height=1000,bg='grey80')
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')


afficheGrille(cani)

def creertableau():
    for j in range(0,9):
        ligne=[]
        for i in range(0,9):
            ligne.append(0)
        tableau.append(ligne)
    #for j in range(0,9):
        #print(tableau[j])
creertableau()
tableau[2][2]=1
tableau[3][3]=2
tableau[4][4]=2

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
          
affichagepions()
