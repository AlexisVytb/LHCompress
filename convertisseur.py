import os
import struct
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def convert_file(input_file):
    try:
        # Créer le fichier de sortie
        output_file = f"{input_file}.LZ"

        # Lire et écrire les données
        with open(input_file, 'rb') as infile:
            data = infile.read()

        with open(output_file, 'wb') as outfile:
            outfile.write(data)

        print(f"Conversion réussie : {output_file}")
        return output_file

    except Exception as e:
        print(f"Erreur lors de la conversion de {input_file} : {e}")
        return None

def select_file():
    file_path = filedialog.askopenfilename(title="Sélectionner un fichier", 
                                           filetypes=[("Fichiers supportés", "*.kpbin *.arc *.bin")])
    if file_path:
        result = convert_file(file_path)
        if result:
            messagebox.showinfo("Succès", f"Fichier converti avec succès :\n{result}")
        else:
            messagebox.showerror("Erreur", f"Échec de la conversion pour :\n{file_path}")

# Créer l'interface utilisateur
root = tk.Tk()
root.title("Convertisseur vers LZ")
root.geometry("600x400")
root.resizable(False, False)

# Style de l'interface
style = ttk.Style(root)
style.configure('TLabel', font=("Arial", 12))
style.configure('TButton', font=("Arial", 12))

# Cadre principal
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Titre
title_label = ttk.Label(main_frame, text="Convertisseur de fichiers vers LZ", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Cadre droit pour les actions
action_frame = ttk.LabelFrame(main_frame, text="Actions", padding="10")
action_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=20, pady=10)

# Boutons d'actions
select_button = ttk.Button(action_frame, text="Choisir un fichier", command=select_file)
select_button.pack(pady=10)

quit_button = ttk.Button(action_frame, text="Quitter", command=root.quit)
quit_button.pack(pady=10)

# Texte d'information
info_label = ttk.Label(main_frame, text="Instructions :\n1. Cliquez sur 'Choisir un fichier'.\n2. Le fichier sera automatiquement converti dans le même dossier avec l'extension .LZ.", 
                       justify=tk.LEFT, font=("Arial", 10))
info_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)

root.mainloop()
