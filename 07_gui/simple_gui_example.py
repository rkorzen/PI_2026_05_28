import tkinter as tk

def oblicz():
    a = entry_a.get()
    b = entry_b.get()
    result = int(a) + int(b)
    wynik.configure(text=result)


root = tk.Tk()
label_a = tk.Label(root, text="Arg a: ")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Arg b: ")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

submit = tk.Button(root, command=oblicz, text="Oblicz")
submit.pack()

wynik = tk.Label(root, text="")
wynik.pack()

root.mainloop()

print("Koniec")