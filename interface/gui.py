import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("Access Control System")

        self.label = tk.Label(master, text="Welcome to the Access Control System")
        self.label.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def login(self):
        messagebox.showinfo("Login", "Login functionality to be implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()