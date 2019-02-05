import json
import re
import cv2

from pprint import pprint
listdata1 = list()
listdata2 = list()

for t in range(1,12):
	d=1
	with open('Labels%d.json' %t) as f:
		data = json.load(f)

	for row in data["annotations"]:
		temp = re.search("\s([0-9_:]+)$",row["gameTime"])
		t1 = temp.group(1).split(':')[0]
		t2 = temp.group(1).split(':')[1]
		time_mili = (int(t1)*60 + int(t2))* 1000

	
		if int(row["gameTime"].split(' ')[0]) ==1:
			listdata1.append([row["gameTime"].split(' ')[0],time_mili-2000, time_mili-1000, time_mili, time_mili+1000, time_mili + 2000,row["label"]])

		if int(row["gameTime"].split(' ')[0]) ==2:
			listdata2.append([row["gameTime"].split(' ')[0],time_mili-2000, time_mili-1000, time_mili, time_mili+1000, time_mili + 2000,row["label"]])



print(listdata1)
print(" ")
print(listdata2)
print(" ")
print(" ")

##

cap = cv2.VideoCapture('%d_1.mkv' % d)

count=0
for k in listdata1:
	for m in range(1,6):
		cap.set(cv2.CAP_PROP_POS_MSEC,k[m])      
		ret,frame = cap.read()   
		print (ret)
		cap.set
		count=count+1     
		if k[6]=="substitution-in":
			cv2.imwrite("subs/frame%d.jpg" % count , frame)
		if k[6]=="soccer-ball":
			cv2.imwrite("socb/frame%d.jpg" % count , frame)
		if k[6]=="y-card":
			cv2.imwrite("ycard/frame%d.jpg" % count , frame)
		if k[6]=="soccer-ball-own":
			cv2.imwrite("socbo/frame%d.jpg" % count , frame)
		if k[6]=="penalty-missed":
			cv2.imwrite("pm/frame%d.jpg" % count , frame)


cap = cv2.VideoCapture('%d_2.mkv' % d)


for k in listdata2:
	for m in range(1,6):
		cap.set(cv2.CAP_PROP_POS_MSEC,k[m])      # Go to the 1 sec. position
		ret,frame = cap.read()   
		print (ret)
		cap.set
		count=count+1     
		if k[6]=="substitution-in":
			cv2.imwrite("subs/frame%d.jpg" % count , frame)
		if k[6]=="soccer-ball":
			cv2.imwrite("socb/frame%d.jpg" % count , frame)
		if k[6]=="y-card":
			cv2.imwrite("ycard/frame%d.jpg" % count , frame)
		if k[6]=="soccer-ball-own":
			cv2.imwrite("socbo/frame%d.jpg" % count , frame)
		if k[6]=="penalty-missed":
			cv2.imwrite("pm/frame%d.jpg" % count , frame)
cv2.waitKey()

##