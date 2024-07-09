import tkinter as tk
from tkinter import Tk
import main as m

class Interface:

    def __init__(self, root):
        self.root = root
        self.root.title("Terminal")
        self.principalFrame = tk.Frame(root)

        self.clavesText = tk.Text(self.root, autoseparators=True, border=0.5, width=40, height=10)
        self.clavesText.grid(row=0, padx=10, pady=10, columnspan=3)
        self.clavesText.bind("<<Modified>>", self.toggle_button)

        self.claveEntry = tk.Entry(self.root)
        self.claveEntry.grid(row=1, column=0, padx=2, pady=2)
        self.similitudEntry = tk.Entry(self.root)
        self.similitudEntry.grid(row=1, column=2, padx=2, pady=2)
        
        self.iniciarButton = tk.Button(self.root, text="Iniciar", state=tk.DISABLED, command=self.extraerBoton)
        self.iniciarButton.grid(row=2, column=1, padx=2, pady=2)


    def toggle_button(self, event):
        # Obtener el contenido del Text widget
        content = self.clavesText.get("1.0", tk.END).strip()
        # Habilitar o deshabilitar el botón basado en el contenido del Text widget
        if content:
            self.iniciarButton.config(state=tk.NORMAL)
        else:
            self.iniciarButton.config(state=tk.DISABLED)

    def extraerBoton(self):
        content = self.clavesText.get("1.0", tk.END).rstrip()
        lista = content.split("\n")
        print(lista)
        palabras = m.insert(lista)
        palabras = m.seleccion(self.claveEntry.get(), int(self.similitudEntry.get()), palabras)

        texto = "\n".join([word.palabra for word in palabras])
        self.clavesText.delete("1.0", tk.END)
        self.clavesText.insert(tk.END, texto)


if __name__ == "__main__":
    root = Tk()
    root.wm_attributes("-topmost", True)
    app = Interface(root)
    root.mainloop()