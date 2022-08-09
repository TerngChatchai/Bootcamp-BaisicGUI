# Read JSON.py

import json

def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		#print(type(data))
		#print(data[0])
		#print(data[0]['name'])
	return data
	
def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False, indent= 4)
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)

data = {'12345':['Banana',100,5],
		'12346':['Durian',150,99],
		'12347':['Apple',200,10],
		'12348':['แก้วมังกร',300,20]
		}

writejson(data)