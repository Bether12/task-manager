import tkinter as tk

class TaskManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("800x600")
        self.root.resizable(False, False)