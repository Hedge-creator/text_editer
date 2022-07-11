import tkinter #графическая библиотека
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile #библиотека для работы с файлами
from tkinter.messagebox import showerror #библиотека для сообщений (всплывающих окон)
from tkinter import messagebox

FILE_NAME = tkinter.NONE

def new_file(): #новый файл
	global FILE_NAME
	FILE_NAME = "Без названия"
	text.delete('1.0', tkinter.END)

def save_file(): #сохранить файл
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as(): #сохранить как
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:                               #если
		out.write(data.rstrip())
	except Exception:                  #иначе - ошибка
		showerror(title="Проблема", message="Ошибка сохранения файла")

def open_file(): #открыть файл
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def info(): #информация о программе
	messagebox.showinfo("Сведение", "Код написан Орловым Артёмом в 2022 году")

def root_quit(): #закрытие программы (завершение работы)
    root.destroy()


root = tkinter.Tk() #окно приложения
root.title("Текстовый редактор") #имя программы

root.minsize(width=350, height=250) #минимальные размеры окна
root.maxsize(width=700, height=500) #максимальные размеры окна

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview) #полоса прокрутки
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
#различные виджеты
text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Новый", command=new_file)
fileMenu.add_command(label="Открыть", command=open_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)

menuBar.add_cascade(label="Файл", menu=fileMenu)
menuBar.add_cascade(label="Инфо", command=info)
menuBar.add_cascade(label="Выход", command=root_quit)
root.config(menu=menuBar)
root.mainloop()
