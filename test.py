import tkinter as tk

print("imported tkinter")
HEIGHT = 500
WIDTH = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root,bg = 'blue')
frame.place(relx = 0.1, rely = 0.1,relwidth=0.8,relheight=0.8)

def bntpressed():
    exit(0)


bnt = tk.Button(frame, text="test bnt",
                bg='gray',
                fg='red',
                command=bntpressed)
bnt.place(x=150, y=200)

root.mainloop()
 