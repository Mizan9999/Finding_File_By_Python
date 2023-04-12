from tkinter import *
import path
import disk

di = disk.disk_no()

master = Tk()
master.title("File Finder 1.0")
master.geometry("700x300")

variable = StringVar(master)
variable.set(di[0])

your_file = "------ Your file location will be here ------"


def okh():
    global your_file
    ter_1 = entry_1.get()
    ter_2 = variable.get()
    path_file = path.file_path(file_name=ter_1, path=ter_2)
    your_file = path_file
    print(your_file)
    label_4.config(text=your_file, font=("Segoe UI Bold", 8))


def button1():

    global your_file
    master.clipboard_clear()
    master.clipboard_append(your_file)


label = Label(text="File Finder", font=("Segoe UI Bold", 30))
label.grid(row=0, column=1)
label_1 = Label(text="File Name:", font=("Segoe UI Bold", 20))
label_1.grid(row=1, column=0, padx=10)
entry_1 = Entry(width=40)
entry_1.grid(row=1, column=1, padx=10)

label_2 = Label(text="Path:", font=("Segoe UI Bold", 20))
label_2.grid(row=2, column=0, sticky="e")

w = OptionMenu(master, variable, *di)
w.grid(row=2, column=1, sticky='WE', columnspan=1, padx=5)

button_1 = Button(text="Search", command=okh, height=1)
button_1.grid(row=3, column=1, sticky='NWSE', padx=10, columnspan=1)

label_3 = Label(text="Output:", font=("Segoe UI Bold", 20))
label_3.grid(row=4, column=0, sticky="e")

label_4 = Label(text=your_file, font=("Segoe UI Bold", 10))
label_4.grid(row=4, column=1, columnspan=2)

b = Button(master, text="copy", width=10, height=2, command=button1)
b.grid(row=5, column=1, sticky="w")

master.mainloop()
