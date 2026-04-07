import tkinter as tk

#counting seconds
# counter = 0
# def counter_label(label):
#     def count():
#         global counter
#         counter += 1
#         label.config(text = str(counter))
#         label.after(1000, count)
#     count()

# root = tk.Tk()
# root.title("Counting seconds")
# label = tk.Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text="Stop", width = 25, command=root.destroy)
# button.pack()
# root.mainloop()


#justifying text
# root = tk.Tk()
# logo = tk.PhotoImage(file="cat.gif")

# explanation = '''Right now only GIF and PPM/PGM are supported,
# but we can allow additional formats by using a special interface
# '''

# w1 = tk.Label(root, image=logo).pack(side="right")
# w2 = tk.Label(root, justify=tk.CENTER, padx=10, text=explanation).pack(side="left")

# root.mainloop()


# 
root = tk.Tk()
tk.Label(root, text = "Red Text in Times Font",
         fg = "red",
         font = "Times").pack()
tk.Label(root, text = "Green Text in Helvetica Font",
         fg = "light green",
         bg = "dark green",
         font = "Helvetica 16 bold italic").pack()
tk.Label(root, text = "Blue Text in Verdana Font",
         fg = "blue",
         bg = "yellow",
         font = "Verdana 10 bold").pack()

root.mainloop()