import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

task_list = []


# ------------------- ADD BUTTON ------------------------- #

def addTask():
    task = search_entry.get()
    search_entry.delete(0, END)
    if task:
        with open("tasks.txt", "a") as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def addTask2(event):
    task = search_entry.get()
    search_entry.delete(0, END)
    if task:
        with open("tasks.txt", "a") as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)


def openTaskFile():
    try:
        global task_list
        with open("tasks.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("tasks.txt", "w")
        file.close()


# ------------------- DELETE BUTTON ------------------------- #
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasks.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task)
        listbox.delete(ANCHOR)


# ------------------- EDIT BUTTON ------------------------- #

def editTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    search_entry.insert(0, task)
    deleteTask()


# ------------------- CHECK BUTTON ------------------------- #
def checkTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    task_num = listbox.curselection()
    listbox.itemconfig(task_num, {'fg': DARK})


# ------------------- UI ------------------------- #
# top bar color #9078E8
# backgroud color #241246, #381F68, #241246
LIGHT_DARK = '#131313'
DARK = '#241246'
DARK_BLUE = '#9078e8'

win = ctk.CTk()
win.title("To Do List")
win.config(width=460, height=700)
win.resizable(False, False)

file_path = os.path.dirname(os.path.realpath(__file__))

canvas = Canvas(width=450, height=600)
background_img = PhotoImage(file='img/background.png')
background = canvas.create_image(230, 350, image=background_img)
canvas.grid(row=0, column=0, columnspan=4, rowspan=6)

topImage = ctk.CTkImage(Image.open(file_path + "/img/topbar.png"), size=(460, 60))
top_image = ctk.CTkLabel(win, image=topImage, text="", bg_color=DARK)
top_image.grid(row=0, column=0, columnspan=4, pady=0)

task_image = ctk.CTkLabel(win, bg_color=DARK_BLUE, text='MAKE YOUR DAY MATTER \n ALL TASKS',
                          font=('Century Gothic', 20))
task_image.grid(row=0, column=0, columnspan=4)

noteImage = ctk.CTkImage(Image.open(file_path + "/img/task.png"), size=(40, 40))
task_image = ctk.CTkLabel(win, text='', image=noteImage, bg_color=DARK_BLUE)
task_image.place(x=360, y=15)

search_entry = ctk.CTkEntry(win, width=315, fg_color="#ddd3ef", justify='right', text_color='#393939',
                            font=('ariel', 20), placeholder_text='Enter Tasks')
win.bind('<Return>', addTask2)
search_entry.grid(row=3, column=0, columnspan=3, pady=10, ipady=10, padx=10)

add_icon = ctk.CTkImage(Image.open(file_path + "/img/add.png"), size=(40, 40))
add_button = ctk.CTkButton(win, image=add_icon, text='', width=115, bg_color=DARK, fg_color=DARK, hover_color=DARK_BLUE,
                           command=addTask)
add_button.grid(row=3, column=3)

listbox = Listbox(win, font=('ariel', 20), width=30, height=12, bg=DARK_BLUE, fg='#ddd3ef', cursor='hand2',
                  justify='right')
listbox.grid(row=4, column=0, columnspan=4, padx=5)

Delete_icon = ctk.CTkImage(Image.open(file_path + "/img/delete.png"), size=(40, 40))
delete_button = ctk.CTkButton(win, image=Delete_icon, text='', width=80, bg_color=DARK, fg_color=DARK,
                              command=deleteTask)
delete_button.grid(row=5, column=3, pady=10)

check_icon = ctk.CTkImage(Image.open(file_path + "/img/check.png"), size=(40, 40))
check_button = ctk.CTkButton(win, image=check_icon, text='', width=80, bg_color=DARK, fg_color=DARK, command=checkTask)
check_button.grid(row=5, column=0, pady=10)

edit_icon = ctk.CTkImage(Image.open(file_path + "/img/edit.png"), size=(40, 40))
edit_button = ctk.CTkButton(win, image=edit_icon, text='', width=80, bg_color=DARK, fg_color=DARK, command=editTask)
edit_button.place(x=200, y=545)

openTaskFile()
win.mainloop()
