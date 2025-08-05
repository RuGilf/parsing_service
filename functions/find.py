import csv 

def find(user_number):
    k = 0
    with open('data.csv', mode='r') as file:
        csv_reader = csv.reader(file)  
        for row in csv_reader:  
            if str(user_number) in row[0]:
                k += 1
                row_k = row 
        if k == 1:
            return row_k
        else:
            return 'Некоректный номер'

def before(user_number):
    k = 0
    with open('data.csv', mode='r') as file:
        csv_reader = csv.reader(file)  
        for row in csv_reader:
            if (str(user_number) not in row[0]) and ('+' in row[0]):
                k += 1
            elif str(user_number) in row[0]:
                return k

def all():
    k = 0
    with open('data.csv', mode='r') as file:
        csv_reader = csv.reader(file) 
        for row in csv_reader:
            if '+' in row[0]:
                k += 1
    return k 

def after(user_number):
    return all() - before(user_number)

def find_place(selected_spec):
    with open('places.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if selected_spec in row[0]:
                return row[0][len(selected_spec) + 1:]
