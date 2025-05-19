import ctypes
import tkinter as tk
from time import strftime
from tkinter import PhotoImage

ico='pngwing'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(ico)

wind=tk.Tk()
wind.title('Digital Clock')
wind.configure(bg='#121212')
wind.geometry('500x200')
wind.resizable(False,False)
img=PhotoImage(file=r'D:/pngwing.png')
wind.iconphoto(False,img)

def time():
    string=strftime('%H:%M:%S \n %D')
    Label1.config(text=string)
    Label1.after(1000,time)

Label1=tk.Label(wind,foreground='#2531ED',background='#121212',font=('calibri',50,'bold'))
Label1.pack(anchor='center')

time()
wind.mainloop()