import tkinter as tk
from tkinter import filedialog


class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Notepad")
        self.master.geometry("500x500")
        self.theme = "black"

        self.create_widgets()

    def create_widgets(self):
        self.create_textbox()
        self.create_menu()
        self.create_buttons()

    def create_textbox(self):
        self.textbox = tk.Text(self.master, wrap=tk.WORD)
        self.textbox.pack(fill=tk.BOTH, expand=True)

    def create_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)

    def create_buttons(self):
        self.create_button("Clear Text", self.clear_text, side=tk.LEFT)
        self.create_button("Toggle Theme", self.toggle_theme, side=tk.RIGHT)

    def create_button(self, text, command, side):
        button = tk.Button(self.master, text=text, command=command)
        button.pack(side=side, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                content = self.textbox.get(1.0, tk.END)
                file.write(content)

    def clear_text(self):
        self.textbox.delete(1.0, tk.END)

    def toggle_theme(self):
        new_theme = "#1e1e1f" if self.theme == "white" else "white"
        fg_color = "#d4d4d4" if new_theme == "black" else "black"

        self.textbox.config(bg=new_theme, fg=fg_color)
        self.theme = new_theme


def main():
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()


if __name__ == "__main__":
    main()
