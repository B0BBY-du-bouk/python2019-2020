from tkinter import*

master = Tk()

cani = Canvas(master, width=1000, height=1000,bg='grey80')
cani.pack()
cani.create_rectangle(100,100,900,900,fill='grey60')

for j in range (1, 10):
    cani.create_line(100*j,100,100*j,900)
    cani.create_line(100,100*j,900,100*j)

testta=[]

for j in range(0,9):
    tampon=[]
    for i in range(0,9):
        tampon.append(0)
    testta.append(tampon)
for j in range(0,9):
    print(testta[j])

testta[2][2]=1
testta[3][3]=2
testta[4][4]=2

for j in range(0,9):
    print(testta[j])

#cani.create_oval(250,250,350,350,fill='black')
#cani.create_oval(350,350,450,450,fill='white')

for j in range (0,9):
    for i in range (0,9):
        if testta[j][i]>0:
           cani.create_oval((j*100+50),(j*100+50),(j*100+150),(j*100+150),fill='black')
        if testta[j][i]>1:
            cani.create_oval((j*100+50),(j*100+50),(j*100+150),(j*100+150),fill='white')
