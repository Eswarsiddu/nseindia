# for testing
from  tkinter import *
root = Tk()
root.geometry("400x400+483+184")

l1 = Label(root,text="Label 1")
l2 = Label(root,text="Label 2")
l3 = Label(root,text="Label 3")
l4 = Label(root,text="Label 4")
l5 = Label(root,text="Label 5")
l6 = Label(root,text="Label 6")
l7 = Label(root,text="Label 7")
l8 = Label(root,text="Label 8")
l9 = Label(root,text="Label 9")

li = [[l1,l2,l3],[l4,l5,l6],[l7,l8,l9]]
for i in range(3):
    for j in range(3):
        li[i][j].grid(row=i,column=j)

def delpressed():
    # r = int(row.get())
    # c = int(column.get())
    for i in range(3):
        for j in range(3):
            li[i][j].grid(row=j, column=i)


row = Entry(root)
column = Entry(root)
delbut = Button(root,text="delete",command = delpressed)

row.grid(row=3,column=0)
column.grid(row=3,column=1)
delbut.grid(row=3,column=2)

root.mainloop()