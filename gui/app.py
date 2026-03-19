import tkinter as tk
from tkinter import ttk, messagebox
from datahandler import data

class TaskManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.tasks = data.Data()

        self.set_widgets()

    def set_widgets(self):
        tk.Label(self.root, text="New Task:", font=("Arial", 12)).pack(pady=8)
        
        self.entry = tk.Entry(self.root, width=55, font=("Arial", 11))
        self.entry.pack(pady=10)

        tk.Label(self.root, text="Priority:", font=("Arial", 12)).pack(pady=8)
        self.priority_val = tk.StringVar(value="1(High)")
        self.priority_combo = ttk.Combobox(self.root, textvariable=self.priority_val, values=["1(High)", "2(Medium)", "3(Low)"], state="readonly", width=15, font=("Arial", 11))
        self.priority_combo.pack(pady=5)

        tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=70, height=14, font=("Arial", 11))
        self.listbox.pack(pady=10)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack()
        tk.Button(self.btn_frame, text="Mark as done", command=self.mark_done, bg="#2196F3", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=1, padx=10)

        self.refresh_list()

    def add_task(self):
        name = self.entry.get()
        if not name:
            messagebox.showwarning("Warning", "Write task name")
            return

        priority = int(self.priority_val.get()[0])

        self.tasks.add_task(name, priority)
        self.refresh_list()
        self.entry.delete(0, tk.END)
        self.priority_val.set("1(High)")

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks.mark_done(index)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks.delete_task(index)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")
    
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks.task_list:
            self.listbox.insert(tk.END, f"{task.name}   {task.type}   {str(task.priority)}   {task.date_created}")
