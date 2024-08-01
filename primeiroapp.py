import tkinter as tk
from tkinter import messagebox

class primeiroapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.frame, text="Adicionar", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remover Selecionado", command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

if __name__ == "__main__":
    root = tk.Tk()
    app = primeiroapp(root)
    root.mainloop()
