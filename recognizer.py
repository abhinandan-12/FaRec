import cv2
import numpy as np
import os
from PIL import Image
import time
import mysql.connector as sq
import authenticator

auth_data = authenticator.read()
uid = auth_data[0]
password = auth_data[1]

count=0
db=sq.connect(host='localhost',user=uid,passwd=password,database='farec')
cursor=db.cursor()
cursor.execute("show columns from record;")
a=0
for i in cursor.fetchall():
    a=i

dt=a[0]


_att=[]
path='dataset'
# taking names from pictures
# variables
lister=[]

imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
names=[""]

que='select name from record;'
exe1=cursor.execute(que)
name_list=cursor.fetchall()
for i1 in name_list:
    for j1 in i1:
        names.append(j1)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

print(names)#################
font = cv2.FONT_HERSHEY_SIMPLEX
att=[]
com=0

id = len(names)

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

xaxis=[]
yaxis=[]
maxc=0
minc=100
while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if confidence >= maxc:
            maxc=confidence
        elif confidence <= minc:
            minc=confidence
        
        if ((100-confidence) < 50) and ((100-confidence) > 35) :
           # print(id)
        #if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(confidence))
            count=count+1
            if count==100:
                count=0
                if id in _att:
                    break
                
                elif id not in att:
                    att.append(id)
                    for i in att:
                        qu2="update record set "+dt+" = 'yes' where name = ('"+ str(i) +"');"
                        print(str(i),", attendance recorded.")
                        cursor.execute(qu2)
                        db.commit()
                        com=1
                        _att.extend(att)
                        att=[]
                        print("done")

        else:
            id = "unknown person"
            confidence = "  {0}%".format(round(confidence))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
print(maxc,"is the maximum confidence detected")
print(minc,"is the minimum confidence detected")

cursor.close()
db.close()
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
#cv2.destroyAllWindows()
