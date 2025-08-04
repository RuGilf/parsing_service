from functions.update import update
from functions.find import *
from tkinter import *
from tkinter import ttk
import csv

def find_app():
    user_number = find_line.get()
    try:
        if int(user_number) <= 0:
            output.configure(text = 'Псих')
        else:
            output.configure(text = 'До тебя: ' + str(before(user_number)) + 'после тебя: ' + str(after(user_number)) + 'Всего' + str(all()))
    except:
        output.configure(text='Неверный ввод')       

root = Tk()
root.title('Парсер конкурсных списков МИСиС')

w = root.winfo_screenwidth() // 2 - 500
h = root.winfo_screenheight() // 2 - 500
root.geometry(f'1000x1000+{w}+{h}')

update_button = Button(root, text='Обновить списки', command=update)
update_button.grid(column=0, row=0)

output = Label(root, text='')
output.grid(column=1, row=0)

find_button = Button(root, text='Найти себя', command=find_app)
find_button.grid(column=0, row=1)

find_line = Entry(root, width=50)
find_line.grid(column=1, row=1)

root.mainloop()