#base tutorial https://www.youtube.com/watch?v=A_Sfru99QNA
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files","*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File{filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files","*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def use_theme(window, text_edit, current_theme):
    themes = ["dark", "red", "blue", "green", "light"]
    current_index = themes.index(current_theme)  # Get the index of the current theme
    next_theme = themes[(current_index + 1) % len(themes)]  # Get the next theme (cycle back to 0 if it reaches the end)

    if next_theme == "dark":
        window.configure(bg="black")
        text_edit.configure(bg="black", fg="white")
    elif next_theme == "red":
        window.configure(bg="darkred")
        text_edit.configure(bg="darkred", fg="white")
    elif next_theme == "blue":
        window.configure(bg="darkblue")
        text_edit.configure(bg="darkblue", fg="white")
    elif next_theme == "green":
        window.configure(bg="darkgreen")
        text_edit.configure(bg="darkgreen", fg="white")
    elif next_theme == "light":
        window.configure(bg="white")
        text_edit.configure(bg="white", fg="black")

    return next_theme  # Return the new theme to update the current theme

def main():
    window = tk.Tk()
    window.title("VaporNote")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    

    #save and open buttons
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    #initalize theme
    current_theme="dark"

    #cycle theme button
    theme_button = tk.Button(frame, text="Change Theme", command=lambda: set_theme())
    # Create the label for displaying the current theme
    theme_label = tk.Label(frame, text="Current Theme: Dark", font=("Helvetica", 12), width=20)
    

    #call buttons
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    theme_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    theme_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    def set_theme():
        nonlocal current_theme 
        current_theme = use_theme(window, text_edit, current_theme)
        theme_label.config(text=f"Current Theme: {current_theme.capitalize()}")


    #shortcuts
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()