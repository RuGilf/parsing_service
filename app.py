from functions.update import update
from functions.find import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def find_app():
    user_number = find_line.get()
    try:
        if not user_number.isdigit() or int(user_number) <= 0:
            output.configure(text='Некорректный номер', foreground='red')
        else:
            before_count = before(user_number)
            after_count = after(user_number)
            total_count = all()
            
            result_text = f"До вас: {before_count}\nПосле вас: {after_count}\nВсего абитуриентов: {total_count}"
            output.configure(text=result_text, foreground='black')
            
            if total_count > 0:
                position_percent = (before_count / total_count) * 100
                progress['value'] = 100 - position_percent
                progress_label.configure(text=f"Вы в топ {100 - position_percent:.1f}%")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        output.configure(text='Ошибка при обработке данных', foreground='red')

def on_update():
    try:
        update()
        messagebox.showinfo("Успех", "Данные успешно обновлены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось обновить данные: {str(e)}")

root = Tk()
root.title('Парсер конкурсных списков МИСиС')
root.configure(bg='#f0f0f0')

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('TLabel', font=('Arial', 12), background='#f0f0f0')
style.configure('TEntry', font=('Arial', 12), padding=5)

header = Label(root, text="Конкурсные списки МИСиС", font=('Arial', 16, 'bold'), bg='#f0f0f0')
header.pack(pady=20)

control_frame = Frame(root, bg='#f0f0f0')
control_frame.pack(pady=20)

find_label = Label(control_frame, text="Введите ваш номер:", bg='#f0f0f0')
find_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

find_line = Entry(control_frame, width=30, font=('Arial', 12))
find_line.grid(row=0, column=1, padx=5, pady=5)

find_button = Button(control_frame, text='Найти', command=find_app, bg='#4CAF50', fg='white')
find_button.grid(row=0, column=2, padx=5, pady=5)

update_button = Button(root, text='Обновить списки', command=on_update, bg='#2196F3', fg='white')
update_button.pack(pady=10)

progress_label = Label(root, text="Ваша позиция:", bg='#f0f0f0')
progress_label.pack(pady=10)

progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress.pack()

output_frame = Frame(root, bg='white', bd=2, relief=GROOVE)
output_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

output = Label(output_frame, text="Здесь будет отображена информация о вашей позиции", 
               font=('Arial', 12), bg='white', wraplength=600, justify=LEFT)
output.pack(pady=20, padx=20)

footer = Label(root, text="© Копирайт 😎", font=('Arial', 10), bg='#f0f0f0')
footer.pack(side=BOTTOM, pady=10)

root.mainloop()
