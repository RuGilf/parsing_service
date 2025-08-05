from functions.update import update
from functions.find import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *

SPECIALTIES = {
    "Лингвистика": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-450302-NITU_MISIS-OKM-000005584",
    "Физика": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-030302-NITU_MISIS-OKM-000005370",
    "Эдектроника и наноэлектроника": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-110304-NITU_MISIS-OKM-000005408",
    "Материаловедение и технологии материалов": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-220301-NITU_MISIS-OKM-000005497",
    "Нанотехнологии и наноматериалы": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-280000-NITU_MISIS-OKM-000005544",
    "Биотехнология": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-190301-NITU_MISIS-OKM-000005600",
    "Прикладная математика": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-010304-NITU_MISIS-OKM-000005364",
    "Информатика и вычислительная техника": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-090000-NITU_MISIS-OKM-000005382",
    "Бизнес-информатика": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-380305-NITU_MISIS-OKM-000005577",
    "Технологические машины и оборудование": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-150302-NITU_MISIS-OKM-000005436",
    "Металлургия": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-220302-NITU_MISIS-OKM-000005510",
    "Электроэнергетика и электротехника": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-130302-NITU_MISIS-OKM-000005419",
    "Геотехнологии": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=SPEC-COMM-O-210000-NITU_MISIS-OKM-000005481",
    "Инноватика": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-270305-NITU_MISIS-OKM-000005594",
    "Экономика и управление": "https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BAC-COMM-O-380000-NITU_MISIS-OKM-000005551",
}

current_url = None 

def find_app():
    user_number = find_line.get()
    selected_spec = specialty_var.get()
    try:
        if not user_number.isdigit() or int(user_number) <= 0:
            output.configure(text='Некорректный номер', foreground='red')
        else:
            before_count = before(user_number)
            after_count = after(user_number)
            total_count = all()
            current_places = int(find_place(selected_spec))
            
            result_text = f"До вас: {before_count}\nПосле вас: {after_count}\nВсего абитуриентов: {total_count}\nВсего мест: {current_places}"
            output.configure(text=result_text, foreground='black')
            
            if before_count > current_places:
                progress['value'] = 0
                progress_label.configure(text='Без шансов, братик')
            elif total_count > current_places:
                position_percent = (before_count / current_places) * 100 
                progress['value'] = 100 - position_percent
                progress_label.configure(text=f'Вы в топ {100 - position_percent:.1f}%')
            else:
                position_percent = (before_count / total_count) * 100
                progress['value'] = 100 - position_percent
                progress_label.configure(text=f"Вы в топ {100 - position_percent:.1f}%")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        output.configure(text='Ошибка при обработке данных', foreground='red')

def on_update():
    global current_url
    if not current_url:
        messagebox.showwarning("Предупреждение", "Сначала выберите специальность!")
        return
        
    try:
        update()
        update_script(current_url)
        places_function(SPECIALTIES)

        messagebox.showinfo("Успех", "Данные успешно обновлены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось обновить данные: {str(e)}")

def on_specialty_select(event):
    global current_url
    selected_spec = specialty_var.get()
    current_url = SPECIALTIES.get(selected_spec)
    status_label.config(text=f"Выбрано: {selected_spec}", fg="green")

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

spec_frame = Frame(root, bg='#f0f0f0')
spec_frame.pack(pady=10)

spec_label = Label(spec_frame, text="Выберите специальность:", bg='#f0f0f0')
spec_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

specialty_var = StringVar(root)
specialty_var.set(list(SPECIALTIES.keys())[0])
current_url = SPECIALTIES[list(SPECIALTIES.keys())[0]]

spec_menu = OptionMenu(spec_frame, specialty_var, *SPECIALTIES.keys(), command=on_specialty_select)
spec_menu.config(width=30, font=('Arial', 11))
spec_menu.grid(row=0, column=1, padx=5, pady=5)

status_label = Label(spec_frame, text="", bg='#f0f0f0')
status_label.grid(row=1, column=0, columnspan=2, pady=5)

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
