import os
print("Checking required modules")
os.system('cmd /c pip install pillow numpy opencv-python opencv-contrib-python tabulate mysql-connector-python mysql-connector')
os.system('cmd /c cls')

import mysql.connector as sq
from tabulate import tabulate
import table_creator as tbc
tbc.db_crt()
tbc.tb_crt()
db=sq.connect(host='localhost',user='root',passwd='1234',database='farec')
cursor=db.cursor()
tabulate.PRESERVE_WHITESPACE = True
os.system('cmd /c cls')
print('Welcome to FaRec!\nChoose the following to continue:\n------------')

while True:
    os.system('color 3')
    options="1. Add students in database\n2. Update table column\n3. Collect images for FaRec\n4. Start trainer\n5. Start FaRec recognizer\n6. Show attendance record\n7. Exit"
    print(options)

    opt=int(input("Enter your choice: "))

    qu='desc record'
    cursor.execute(qu)
    a=cursor.fetchall()
    header=[]
    for i in a:
        header.append(i[0])
    if opt==1:
        os.system('cmd /c cls')
        print("Opening Record Updater")
        print("------------")
        os.system('rec_upd.py')
        print("------------")
    elif opt==2:
        os.system('cmd /c cls')
        print("Opening Table Updater")
        print("------------")
        os.system('tb_upd.py')
        print("------------")
    elif opt==3:
        os.system('cmd /c cls')
        print("Opening Dataset Collector")
        print("------------")
        os.system('data_col.py')
        print("------------")
    elif opt==4:
        os.system('cmd /c cls')
        print("Training faces")
        print("------------")
        os.system('trainer.py')
        print("------------")
    elif opt==5:
        os.system('cmd /c cls')
        print("Opening Recognizer")
        print("------------")
        os.system('recognizer.py')
        print("------------")
    elif opt==6:
        os.system('cmd /c cls')
        cursor.execute("select * from record;")
        b=cursor.fetchall()
        for i in b:
            header.append(i[0])
        print(tabulate(b, header, tablefmt='fancy_grid'))
        print("------------")
        input("Press enter to continue")
        os.system('cmd /c cls')
    elif opt==7:
        os.system('cmd /c cls')
        print("------------")
        print("Thank you for using FaRec\nBase/Source code by: Jacob12138xieyuan\nGithub- https://github.com/Jacob12138xieyuan/easy-real-time-face-recognition-python")
        print("Edited and Developed by Abhinandan Mandal and Ayush Kumar")
        print("Version: Alpha 0.2")
        input("Press enter to exit")
        break
    else:
        print("Invalid choice")
        print("------------")
        os.system('cmd /c cls')
