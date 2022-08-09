# Basic GUI.py
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.geometry('500x400')
GUI.title('Program for Bow tiw calculate v.0.0.1')

file = PhotoImage(file='bow.png')
IMG = Label(GUI, image=file,text='')
IMG.pack()

L1 = Label(GUI, text='Program to calculate bow ties', font = ('angsana new',30,'bold'), fg = 'blue')
L1.pack() #place(x,y) , grid(row=0, column, =0)

L2 = Label(GUI, text = 'Enter amount of bow ties', font=('angsana new', 20),fg='green')
L2.pack()

quan = StringVar()
E1 = ttk.Entry(GUI, textvariable=quan, font=('impact',20))
E1.pack()

#####
def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year = stamp.year + 543) # บวกเป็น พศ
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return stamp

#######
def writetext(quantity,total):
	stamp = timestamp()
	#with open(filename, 'a',encoding='utf-8') as file: สำหรับใช้ภาษาไทย
	filename = 'data.txt'
	with open(filename, 'a') as file:
		file.write('\n' + 'Date-Time: {} Bowtie: {} ea Total {} Baht'.format(timestamp(thai=False),quantity,total))
#########

def writecsv(data):
	
	with open('data.csv', 'a', newline='', encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)

############

def readcsv():
	with open('data.csv', newline='', encoding='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data

############

def sumdata():
	# ฟังก์ชั่นสำหรับรวมค่าที่ได้จาก csv file สรุปออกมาเป็นสองอย่าง
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result: 
		#sumlist_quan = [ int(d[1])   for d in result]
		sumlist_quan.append(int(d[1]))
		sumlist_total.append(int(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)
	return (sumquan,sumtotal)

##################

def calculate(event=None): #เชคทั้งevent คือกดปุ่ม หรือไม่มี event คือคลิกปกติ
	quantity = quan.get()
	price = 1000
	pay = int(quantity)*price
	writetext(quantity,pay)

	data = [timestamp(thai=False),quantity,pay]
	writecsv(data)
	

	#pop up
	sm = []
	sm = sumdata()
	title = 'Total Pay'
	text = 'Bow tie: {} ea Pay: {} Baht'.format(quantity,pay)
	messagebox.showinfo(title,text)

	quan.set('') #clear data ในช่อง
	E1.focus() #ให้ cursor วิ่งไปที่E1 หลังจบฟังชั่น calculate
	


B1 =  ttk.Button(GUI, text ='calculate', command=calculate)
B1.pack(ipadx=30,ipady=20, pady=20)

E1.bind('<Return>',calculate) #เพิ่มฟังก์ชั่นปุ่ม Enter

#เพิ่มฟังก์ชั่นสำหรับการกดปุ่ม
def summaryData(event):
	sm = sumdata()
	title = 'Total Sell'
	text = 'Total sell: {} ea\nTotal Recieve: {} Baht'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',summaryData)
GUI.bind('<F2>',summaryData)

E1.focus() #ให้ cursor ไปที่ตำแหน่ง E1 ตอนstart
GUI.mainloop()