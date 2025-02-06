import tkinter as tk
from tkinter import messagebox

def show_message():
    if check_state.get() == 0:
        print(textbox.get("1.0", tk.END))
    else:
        messagebox.showinfo("Message", textbox.get("1.0", tk.END))

def shortcut(event):
    if event.state == 12 and event.keysym == "Return":
        show_message()

def on_closing():
    user_response = messagebox.askyesno("Quit?", "Do you really want to quit?")
    if user_response:
        root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)

# Étiquette pour indiquer l'objectif de la zone de texte
label = tk.Label(root, text="Enter your message", font=("Arial", 18))
label.pack(padx=10, pady=10)

# Zone de texte pour saisir le message
textbox = tk.Text(root, font=("Arial", 16), height=5)
textbox.pack(padx=10, pady=10)

# Case à cocher pour décider d'afficher une boîte de message
check_state = tk.IntVar()
check = tk.Checkbutton(root, text="Show a message box", font=("Arial", 16), variable=check_state)
check.pack(padx=10, pady=10)

# Bouton pour afficher le message (ou imprimer à la console)
button = tk.Button(root, text="Show message", font=("Arial", 18), command=show_message)
button.pack()

# Raccourci clavier pour afficher le message
root.bind("<KeyPress>", shortcut)

# Barre de menu avec des options de fichier
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Close", command=on_closing)
file_menu.add_command(label="Close with error", command=exit)
file_menu.add_separator()
file_menu.add_command(label="Show message", command=show_message)

# Ajout du menu Fichier à la barre de menu
menu_bar.add_cascade(label="File", menu=file_menu)

# Configuration de la barre de menu pour la fenêtre principale
root.config(menu=menu_bar)

# Démarrage de la boucle principale
root.mainloop()
