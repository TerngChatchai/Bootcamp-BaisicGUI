# Write CSV
import csv

def writecsv(data):
	# data = ['Time','10','1000']
	with open('data.csv', 'a', newline='', encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)


#d = ['2022-08-12 10:43:41', 9, 9000]
#writecsv(d)


def readcsv():
	with open('data.csv', newline='', encoding='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data

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

xx = sumdata()
print(xx)
