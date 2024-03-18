import tkinter
import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="grey99")

root = tk.Tk()
root.title("Task list")
root.configure(background="dark orange")

text1 = tk.Label(root, text="Введите вашу задачу: ", bg="dark orange")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=40, bg="OrangeRed")
task_entry.pack(pady=15)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=10)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=10)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=10)

text2 = tk.Label(root, text="Список задач: ", bg="dark orange")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=45, bg="orange4")
task_listBox.pack(pady=10)

root.mainloop()
