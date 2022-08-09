from datetime import datetime

quantity = 10
cal = quantity * 100



def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year = stamp.year + 543)
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	#with open(filename, 'a',encoding='utf-8') as file: สำหรับใช้ภาษาไทย
	filename = 'data.txt'
	with open(filename, 'a') as file:
		file.write('\n' + 'Date-Time: {} Bowtie: {} ea Total {} Baht'.format(stamp,quantity,total))


writetext(90,9000)
writetext(91,9100)
writetext(92,9300)