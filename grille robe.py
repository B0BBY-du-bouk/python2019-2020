from tkinter import*

master = Tk()

cani = Canvas(master, width=1000, height=1000)
cani.pack()

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

for j in range(0,9):
    print(testta[j])
