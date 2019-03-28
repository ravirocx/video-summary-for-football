import json
import re
import cv2
import time

from pprint import pprint

f = open("video.ini", "r")
content = f.read()

st1 = int((content.split(' = ')[1]).split('[')[0].strip())
st2 = int((content.split(' = ')[2]).strip())


listdata1 = list()
listdata2 = list()

d=1
with open('Labels.json') as f:
	data = json.load(f)

for row in data["annotations"]:
	temp = re.search("\s([0-9_:]+)$",row["gameTime"])
	t1 = temp.group(1).split(':')[0]
	t2 = temp.group(1).split(':')[1]
	time_mili1 = (int(t1)*60 + int(t2))* 1000 + st1*1000
	time_mili2 = (int(t1)*60 + int(t2))* 1000 + st2*1000

	
	if int(row["gameTime"].split(' ')[0]) ==1:
		listdata1.append([row["gameTime"].split(' ')[0],time_mili1-10000,time_mili1-9500,time_mili1-9000,time_mili1-8500,time_mili1-8000,time_mili1-7500,time_mili1-7000,time_mili1-6500,time_mili1-6000, time_mili1-5500, time_mili1-5000, time_mili1-4500, time_mili1-4000,time_mili1-3500,time_mili1-3000,time_mili1-2500,time_mili1-2000,time_mili1-1500, time_mili1-1000, time_mili1-500,time_mili1,row["label"]])

	if int(row["gameTime"].split(' ')[0]) ==2:
		listdata2.append([row["gameTime"].split(' ')[0],time_mili2-10000,time_mili2-9500,time_mili2-9000,time_mili2-8500,time_mili2-8000,time_mili2-7500,time_mili2-7000,time_mili2-6500,time_mili2-6000, time_mili2-5500, time_mili2-5000, time_mili2-4500, time_mili2-4000,time_mili2-3500,time_mili2-3000,time_mili2-2500,time_mili2-2000,time_mili2-1500, time_mili2-1000, time_mili2-500,time_mili2,row["label"]])
print(listdata1)
print(" ")
print(listdata2)
print(" ")
print(" ")

##

cap = cv2.VideoCapture('1_HQ.mkv')

count=0
for k in listdata1:
	for m in range(1,22):
		cap.set(cv2.CAP_PROP_POS_MSEC,k[m])     
		ret,frame = cap.read()   
		print (ret)
		cap.set
		count=count+1     
		if k[22]=="substitution-in":
			cv2.imwrite("subs/frame%d.jpg" % count , frame)


cap = cv2.VideoCapture('2_HQ.mkv')


for k in listdata2:
	for m in range(1,22):
		cap.set(cv2.CAP_PROP_POS_MSEC,k[m])      # Go to the 1 sec. position
		ret,frame = cap.read()   
		print (ret)
		cap.set
		count=count+1     
		if k[22]=="substitution-in":
			cv2.imwrite("subs/frame%d.jpg" % count , frame)
		
cv2.waitKey()

##