import tkinter as tk

class TimbreApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Timbres")

        self.total_label = tk.Label(master, text="Cantidad Total:")
        self.total_label.grid(row=0, column=0)

        self.total_entry = tk.Entry(master)
        self.total_entry.grid(row=0, column=1)

        self.calc_button = tk.Button(master, text="Calcular", command=self.calcular_timbre)
        self.calc_button.grid(row=1, column=0)

        self.clear_button = tk.Button(master, text="Limpiar", command=self.limpiar_timbre)
        self.clear_button.grid(row=1, column=1)

        self.result_label = tk.Label(master, text="Resultados:")
        self.result_label.grid(row=2, column=0)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=3, column=0, columnspan=2)

    def calcular_timbre(self):
        total = self.total_entry.get()

        if total:
            if not total.isdigit():
                self.result_text.insert(tk.END, "Por favor ingrese solo números.\n")
                return

            total = int(total)

            if total < 200:
                total = 200
            else:
                total -= total % 200

            timbre_500 = total // 100000
            total -= timbre_500 * 100000
            timbre_100 = total // 20000
            total -= timbre_100 * 20000
            timbre_50 = total // 10000
            total -= timbre_50 * 10000
            timbre_20 = total // 4000
            total -= timbre_20 * 4000
            timbre_10 = total // 2000
            total -= timbre_10 * 2000
            timbre_5 = total // 1000
            total -= timbre_5 * 1000
            timbre_1 = total // 200
            total -= timbre_1 * 200

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Timbres de Q500: {timbre_500}\n")
            self.result_text.insert(tk.END, f"Timbres de Q100: {timbre_100}\n")
            self.result_text.insert(tk.END, f"Timbres de Q50: {timbre_50}\n")
            self.result_text.insert(tk.END, f"Timbres de Q20: {timbre_20}\n")
            self.result_text.insert(tk.END, f"Timbres de Q10: {timbre_10}\n")
            self.result_text.insert(tk.END, f"Timbres de Q5: {timbre_5}\n")
            self.result_text.insert(tk.END, f"Timbres de Q1: {timbre_1}\n")

        else:
            self.result_text.insert(tk.END, "Por favor ingrese una cantidad.\n")

    def limpiar_timbre(self):
        self.total_entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)
        
root = tk.Tk()
timbre_app = TimbreApp(root)
root.mainloop()
