from tkinter import *
import random
import tkinter.messagebox
import pickle

import Python_sendMail

#Create root window
root = Tk()

#Change the window size
root.geometry("350x300")

#change root window background color

root.configure(bg="white")

#Change the title

root.title("my super To Do List")

#create an emoty list

tasks = [] #only for fist use if pickle file does not exist
pickle_in = open("tasks.pickle", "rb")
tasks = pickle.load(pickle_in)


#create functions

def update_listbox():
    #clear the current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    #Get the task to add
    task = txt_input.get()
    #Make sure the task is not empty
    if task !="":
        #Append to the list
        tasks.append(task)
        #Update the listbox
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task."
    #Delete entry in Entry box
    txt_input.delete(0, "end")

def del_all():
    confirmed = tkinter.messagebox.askyesno("Please confirm", "do you really want to delete all?")
    if confirmed == True:
        # since we are changing the list, it needs to be global
        global tasks
        #clear the tasks list
        tasks = []
        #Update the listbox
        update_listbox()

def del_one():
    #Get the text of the currently selected item
    task = lb_tasks.get("active")
    #Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    #Update the listbox
        update_listbox()

def sort_asc():
    #sort the list
    tasks.sort()
    #Update the listbox
    update_listbox()

def sort_desc():
    #Sort the list
    tasks.sort()
    #Reverse the list
    tasks.reverse()
    #Update the listbox
    update_listbox()

def choose_random():
    #Chooe a random task
    task = random.choice(tasks)
    #Update the display label
    lbl_display["text"]=task

def show_number_of_tasks():
    #get the number of tasks
    number_of_tasks = len(tasks)
    #create and format the message
    msg = "Number of tasks: %s" % number_of_tasks
    #display the message
    lbl_display["text"] = msg

def exit_it():
    #Picke out tasks Array into bytes
    pickle_out = open("tasks.pickle", "wb")
    pickle.dump(tasks, pickle_out)
    pickle_out.close()
    exit()


#Create Widgets

lbl_title = Label(root,text="To-Do-List", bg="red")
lbl_title.grid(row=0,column=0)

lbl_display = Label(root,text="", bg="grey", width="15")
lbl_display.grid(row=0,column=1)

txt_input = Entry(root)
txt_input.grid(row=1,column=1)

btn_add_task = Button(root,text="Add Task", fg="green", bg="grey", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = Button(root,text="Delete all", fg="green", bg="grey", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = Button(root,text="Delete Selection", fg="green", bg="grey", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = Button(root,text="Sort (ASC)", fg="green", bg="grey", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = Button(root,text="Sort (DESC)", fg="green", bg="grey", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = Button(root,text="choose random", fg="green", bg="grey", command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_task = Button(root,text="total number of tasks", fg="green", bg="grey", command=show_number_of_tasks)
btn_number_of_task.grid(row=7,column=0)

btn_exit = Button(root,text="Exit", fg="green", bg="grey", command=exit_it)
btn_exit.grid(row=8,column=0)

btn_send_mail = Button(root,text="Mail", fg="green", bg="grey", command=Python_sendMail.send_it)
btn_send_mail.grid(row=9,column=0)

lb_tasks = Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)

update_listbox()

#Start the main events loop
root.mainloop()
