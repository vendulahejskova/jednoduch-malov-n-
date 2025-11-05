import tkinter as tk
from tkinter import colorchooser

# Funkce pro kreslení
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

# Funkce pro změnu barvy
def change_color():
    global color
    new_color = colorchooser.askcolor(color)[1]
    if new_color:
        color = new_color

# Funkce pro změnu velikosti štětce
def change_brush_size(value):
    global brush_size
    brush_size = int(value)

# Vyčištění plátna
def clear_canvas():
    canvas.delete("all")

# Hlavní okno
root = tk.Tk()
root.title("Jednoduché malování")
root.geometry("800x600")

# Výchozí barva a velikost
color = "black"
brush_size = 5

# Plátno
canvas = tk.Canvas(root, bg="white", width=800, height=500)
canvas.pack(pady=10)
canvas.bind("<B1-Motion>", paint)  # kreslení při držení levého tlačítka myši

# Ovládací panel
controls = tk.Frame(root)
controls.pack()

color_button = tk.Button(controls, text="Změnit barvu", command=change_color)
color_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(controls, text="Vyčistit plátno", command=clear_canvas)
clear_button.grid(row=0, column=1, padx=10)

brush_label = tk.Label(controls, text="Velikost štětce:")
brush_label.grid(row=0, column=2, padx=10)

brush_slider = tk.Scale(controls, from_=1, to=50, orient=tk.HORIZONTAL, command=change_brush_size)
brush_slider.set(brush_size)
brush_slider.grid(row=0, column=3)

# Spuštění aplikace
root.mainloop()
