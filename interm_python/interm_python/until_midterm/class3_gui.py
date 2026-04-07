import tkinter as tk

root = tk.Tk()

root.title("Tk example")
root.configure(background="yellow")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

tk.Label(root, text="Rules are made to be broken").pack()
tk.Label(root, text="-TB").pack()

image = tk.PhotoImage(file="TB.png", height=300)
tk.Label(root, image=image).pack()

root.mainloop()