from tkinter import *
from tkinter import ttk, messagebox

friend = {'somchai':'สมชาย ดีมาก', 
		  'somsak':'สมศักดิ์ เก่งมาก',
		  'somsri':'สมศรี เยี่ยมมาก'}

GUI = Tk()
GUI.title('My first Programe')
GUI.geometry('500x300')



v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text,font=('angsana new', 20))
E1.pack()

def click():
	text = v_text.get()
	print('Text: ', text)
	if text in friend:
		result = friend[text]
		messagebox.showinfo('Result','รหัส: {} คือชื่อ: {}'.format(text,result))
	else:
		print('No data')
		messagebox.showwarning('Result: Error','ไมมีมีข้อมูล')

B1 = ttk.Button(GUI, text= 'Click!!', command=click)
B1.pack(ipadx=50,ipady=30,pady=50)

GUI.mainloop()