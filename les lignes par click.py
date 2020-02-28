from tkinter import*

def changement(event):
    #print(event.x)
    #print(event.y)
    a,b=event.x,event.y
    tpl=(a,b)
    #cani.configure(bg = "blue")
    print("tuple ab =",tpl)
    print (tpl[0])
    listtpl.append(tpl)
    print (listtpl)
    #cani.create_line(x0=tpl[0],y0=tpl[1])

feni=Tk()
cani=Canvas(feni,height=700,width=1000,bg="green")
cani.grid()
listtpl=[]
cani.bind("<Button-1>",changement)
