import os

def update():
    os.remove('data.csv')
    os.system('main.py')