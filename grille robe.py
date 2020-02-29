from tkinter import*

master = Tk()

cani = Canvas(master, width=900, height=900)
cani.pack()
#cani.create_line(100,0,100,900)

for j in range (0, 8):
    cani.create_line(100*j,50*j,100+(100*j),50+(50*j))
