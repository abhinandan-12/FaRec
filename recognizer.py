############################################
## Modified By Ayush And Abhinandan       ##
##                                        ##
############################################


import cv2
import numpy as np
import os
from PIL import Image
import time
import mysql.connector as sq
count=0

db=sq.connect(host='localhost',user='root',passwd='1234',database='farec')
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
#print(name_list)
        
#for imagePath in imagePaths:
#    PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
#    img_numpy = np.array(PIL_img,'uint8')

#    name = str(os.path.split(imagePath)[-1].split(".")[2])
#    print(name)
#    if name in names:                                   #checking the names if it exist or not !!!
#      continue
    
#    else:
#        names.append(name)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

print(names)#################
font = cv2.FONT_HERSHEY_SIMPLEX
att=[]
com=0

#iniciate id counter, the number of persons you want to include
id = len(names)

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
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
        

        # Check if confidence is less them 100 ==> "0" is perfect match 
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
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
#cv2.destroyAllWindows()
