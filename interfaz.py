import tkinter as tk
from tkinter import ttk, messagebox
from funciones import *

def calcular_volumen():
    try:
        elemento = combo.get()

        if elemento == "Losa":
            L = float(entry1.get()); A = float(entry2.get()); E = float(entry3.get())
            vol = volumen_losa(L, A, E)

        elif elemento == "Zapata":
            L = float(entry1.get()); A = float(entry2.get()); E = float(entry3.get())
            vol = volumen_zapata(L, A, E)

        elif elemento == "Columna rectangular":
            L1 = float(entry1.get()); L2 = float(entry2.get()); H = float(entry3.get())
            vol = volumen_columna_rect(L1, L2, H)

        elif elemento == "Columna circular":
            D = float(entry1.get()); H = float(entry2.get())
            vol = volumen_columna_circ(D, H)

        messagebox.showinfo("Resultado", f"Volumen requerido: {vol:.3f} m³")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def actualizar_campos(event=None):
    elemento = combo.get()

    for widget in frame_inputs.winfo_children():
        widget.destroy()

    global entry1, entry2, entry3

    if elemento in ["Losa", "Zapata"]:
        tk.Label(frame_inputs, text="Largo (m):").grid(row=0, column=0)
        entry1 = tk.Entry(frame_inputs); entry1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Ancho (m):").grid(row=1, column=0)
        entry2 = tk.Entry(frame_inputs); entry2.grid(row=1, column=1)

        tk.Label(frame_inputs, text="Espesor (m):").grid(row=2, column=0)
        entry3 = tk.Entry(frame_inputs); entry3.grid(row=2, column=1)

    elif elemento == "Columna rectangular":
        tk.Label(frame_inputs, text="Lado 1 (m):").grid(row=0, column=0)
        entry1 = tk.Entry(frame_inputs); entry1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Lado 2 (m):").grid(row=1, column=0)
        entry2 = tk.Entry(frame_inputs); entry2.grid(row=1, column=1)

        tk.Label(frame_inputs, text="Altura (m):").grid(row=2, column=0)
        entry3 = tk.Entry(frame_inputs); entry3.grid(row=2, column=1)

    elif elemento == "Columna circular":
        tk.Label(frame_inputs, text="Diámetro (m):").grid(row=0, column=0)
        entry1 = tk.Entry(frame_inputs); entry1.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Altura (m):").grid(row=1, column=0)
        entry2 = tk.Entry(frame_inputs); entry2.grid(row=1, column=1)


def iniciar_gui():
    global combo, frame_inputs

    ventana = tk.Tk()
    ventana.title("Cálculo de volumen de concreto")

    tk.Label(ventana, text="Selecciona el elemento:").pack()

    combo = ttk.Combobox(ventana, values=[
        "Losa",
        "Zapata",
        "Columna rectangular",
        "Columna circular"
    ])
    combo.pack()
    combo.bind("<<ComboboxSelected>>", actualizar_campos)

    frame_inputs = tk.Frame(ventana)
    frame_inputs.pack(pady=10)

    tk.Button(ventana, text="Calcular", command=calcular_volumen).pack(pady=10)

    ventana.mainloop()