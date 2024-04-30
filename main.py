import tkinter as tk
from task import *
from tkinter import PhotoImage

tasks = []

def add_buttom():
    global tasks
    def save_task():
        tasks = entry.get()
        list_tasks.config(text=tasks)
        entry.delete(0,tk.END)
        window.destroy()


    window = tk.Toplevel(root)
    window.title("Add Task")
    window.resizable(False, False)
    
    #window options
    label = tk.Label(window, text="Qué tarea deseas agregar?")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    save_buttom = tk.Button(window, text="guardar", command=save_task)
    save_buttom.pack()


root = tk.Tk()
root.geometry('400x600')

root.resizable(False, False)

title = tk.Label(root, text='Tareas', justify='left', pady=20, font=('Arial', 20))
title.pack()

list_tasks = tk.Label(root)
list_tasks.pack()



buttom_image = PhotoImage(file="add.png")

add_task_buttom = tk.Button(root, image=buttom_image, borderwidth=0, command=add_buttom)
add_task_buttom.pack(side="bottom", anchor='se')


root.mainloop()