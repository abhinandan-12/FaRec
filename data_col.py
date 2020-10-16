import cv2
import os
import mysql.connector as sq
import authenticator

auth_data = authenticator.read()
uid = auth_data[0]
password = auth_data[1]

db=sq.connect(host='localhost',user=uid,passwd=password',database='farec')
cursor=db.cursor()
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n Enter your FaRec ID: ')

que='select name from record where farec_id ={};'.format(face_id)
exe1=cursor.execute(que)
name_list=cursor.fetchone()
for i in name_list:
    name=i
print(name)

print("\nInitializing face capture. Look the camera and wait ...")
count = 0

# Start detect your face and take 30 pictures
while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        cv2.imwrite("dataset/User." + str(face_id)  + '.' + str(name) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:
         break

print("\nExiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


