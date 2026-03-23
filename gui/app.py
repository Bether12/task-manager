import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from datahandler import data

class TaskManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("800x400")
        self.root.resizable(False, False)

        self.tasks = data.Data()

        self.set_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def set_widgets(self):

        # Menu
        self.menubar = tk.Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.menu_file = tk.Menu(self.menubar, tearoff=0)
        self.menu_file.add_command(label="Import from CSV", command=self.import_csv)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Export to CSV", command=self.export_csv)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Exit", command=self.on_closing)

        self.menu_help = tk.Menu(self.menubar, tearoff=0)
        self.menu_help.add_command(label="Github page") #TODO

        self.menubar.add_cascade(label="File", menu=self.menu_file)
        self.menubar.add_cascade(label="Help", menu=self.menu_help)

        # Table view

        self.tree = ttk.Treeview(self.root, columns=("priority", "name", "status", "date_created", "date_updated"), show="headings")
        self.tree.heading("name", text="Task name")
        self.tree.heading("priority", text="Priority level")
        self.tree.heading("status", text="Status")
        self.tree.heading("date_created", text="Date created")
        self.tree.heading("date_updated", text="Date updated")
        self.tree.pack(pady=5)

        # Button frame

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=15)
        tk.Button(self.btn_frame, text="Add Task", command=self.open_dialog, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="Mark as done", command=self.mark_done, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
        tk.Button(self.btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=2, padx=10)

        self.refresh_tree()

    def open_dialog(self):
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("New Task")
        self.dialog.geometry("400x300")
        self.dialog.resizable(False, False)
        self.dialog.grab_set()

        tk.Label(self.dialog, text="New Task:", font=("Arial", 12)).pack(pady=8)
        
        self.entry = tk.Entry(self.dialog, width=55, font=("Arial", 11))
        self.entry.pack(pady=10)

        tk.Label(self.dialog, text="Priority:", font=("Arial", 12)).pack(pady=8)
        self.priority_val = tk.StringVar(value="1(High)")
        self.priority_combo = ttk.Combobox(self.dialog, textvariable=self.priority_val, values=["1(High)", "2(Medium)", "3(Low)"], state="readonly", width=15, font=("Arial", 11))
        self.priority_combo.pack(pady=5)

        self.frame = ttk.Frame(self.dialog)
        self.frame.pack(pady=15)
        ttk.Button(self.frame, text="Add", command=self.add_task).grid(row=0, column=0, padx=10)
        ttk.Button(self.frame, text="Cancel", command=self.dialog.destroy).grid(row=0, column=1, padx=10)


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
        self.dialog.destroy()

    def mark_done(self):
        try:
            #Selects the selected item id, splits it and access the relevant number part, then subtracts 1 to be compatible with zeroth indexes
            index = self.tree.index(self.tree.selection())
            self.tasks.mark_done(index)
            self.refresh_tree()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")

    def delete_task(self):
        try:
            #Selects the selected item id, splits it and access the relevant number part, then subtracts 1 to be compatible with zeroth indexes
            index = self.tree.index(self.tree.selection())
            self.tasks.delete_task(index)
            self.refresh_tree()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task")

    def import_csv(self):
        file = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Import tasks from CSV")
        result = self.tasks.import_csv(file)

        if result == 0:
            messagebox.showinfo("Success", "CSV information imported correctly")
            self.refresh_tree()
        else:
            messagebox.showerror("Error", f"File not imported:\n{str(result)}")
    
    def export_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Save tasks as CSV")
        result = self.tasks.export_csv(file)

        if result == 0:
            messagebox.showinfo("Success", "File saved correctly")
        else:
            messagebox.showerror("Error", f"File not saved:\n{str(result)}")

    def refresh_tree(self):
        for id in self.tree.get_children():
            self.tree.delete(id)
        for task in self.tasks.task_list:
            self.tree.insert("", "end", values=(task.priority, task.name, task.type, task.date_created, task.date_updated))

    def on_closing(self):
        self.tasks.save_data()
        self.root.destroy()