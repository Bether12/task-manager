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
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def set_widgets(self):
        tk.Label(self.root, text="New Task:", font=("Arial", 12)).pack(pady=8)
        
        self.entry = tk.Entry(self.root, width=55, font=("Arial", 11))
        self.entry.pack(pady=10)

        tk.Label(self.root, text="Priority:", font=("Arial", 12)).pack(pady=8)
        self.priority_val = tk.StringVar(value="1(High)")
        self.priority_combo = ttk.Combobox(self.root, textvariable=self.priority_val, values=["1(High)", "2(Medium)", "3(Low)"], state="readonly", width=15, font=("Arial", 11))
        self.priority_combo.pack(pady=5)

        tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("name", "status", "priority", "date"), show="headings")
        self.tree.heading("name", text="Task name")
        self.tree.heading("priority", text="Priority level")
        self.tree.heading("status", text="Status")
        self.tree.heading("date", text="Date created")
        self.tree.pack(pady=5)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack()
        tk.Button(self.btn_frame, text="Mark as done", command=self.mark_done, bg="#2196F3", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=1, padx=10)

        self.refresh_tree()

    def add_task(self):
        name = self.entry.get()
        if not name:
            messagebox.showwarning("Warning", "Write task name")
            return

        priority = int(self.priority_val.get()[0])

        self.tasks.add_task(name, priority)
        self.refresh_tree()
        self.entry.delete(0, tk.END)
        self.priority_val.set("1(High)")

    def mark_done(self):
        try:
            #Selects the selected item id, splits it and access the relevant number part, then subtracts 1 to be compatible with zeroth indexes
            index = int(self.tree.selection()[0].split('I')[1]) - 1
            self.tasks.mark_done(index)
            self.refresh_tree()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")

    def delete_task(self):
        try:
            #Selects the selected item id, splits it and access the relevant number part, then subtracts 1 to be compatible with zeroth indexes
            index = int(self.tree.selection()[0].split('I')[1]) - 1 
            self.tasks.delete_task(index)
            self.refresh_tree()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")
    
    def refresh_tree(self):
        for id in self.tree.get_children():
            self.tree.delete(id)
        for task in self.tasks.task_list:
            self.tree.insert("", "end", values=(task.name, task.priority, task.type, task.date_created))

    def on_closing(self):
        self.tasks.save_data()
        self.root.destroy()