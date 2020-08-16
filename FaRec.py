import os
if os.name=='nt': #windows
    shell='cmd /c '
    clr='cls'
    pyt=''
elif os.name=='posix': #linux/mac
    shell=''
    clr='clear'
    pyt='python3 '
print("Checking required modules")
os.system(shell+'pip3 install pillow numpy opencv-python opencv-contrib-python tabulate mysql-connector-python mysql-connector pyfiglet')
os.system(shell+clr)

import mysql.connector as sq
from tabulate import tabulate
import table_creator as tbc
import pyfiglet as fg
import authenticator

if authenticator.check()==True:
    auth_data=authenticator.read()
    uid=auth_data[0]
    password=auth_data[1]
elif authenticator.check()==False:
    authenticator.reg()

tbc.db_crt()
tbc.tb_crt()

db=sq.connect(host='localhost',user=uid,passwd=password,database='farec')
cursor=db.cursor()
tabulate.PRESERVE_WHITESPACE = True
os.system(shell+clr)
banner = fg.figlet_format("FaRec")

while True:
    options="1. Add students in database\n2. Update table column\n3. Collect images for FaRec\n4. Start trainer\n5. Start FaRec recognizer\n6. Show attendance record\n7. Exit"
    print(banner)
    print('Choose the following to continue:\n------------')
    print(options)

    opt=int(input("Enter your choice: "))

    qu='desc record'
    cursor.execute(qu)
    a=cursor.fetchall()
    header=[]
    for i in a:
        header.append(i[0])
    if opt==1:
        os.system(shell+clr)
        print("Opening Record Updater")
        print("------------")
        os.system(pyt+'rec_upd.py')
        print("------------")
        os.system(shell+clr)
    elif opt==2:
        os.system(shell+clr)
        print("Opening Table Updater")
        print("------------")
        os.system(pyt+'tb_upd.py')
        print("------------")
        os.system(shell+clr)
    elif opt==3:
        os.system(shell+clr)
        print("Opening Dataset Collector")
        print("------------")
        os.system(pyt+'data_col.py')
        print("------------")
        os.system(shell+clr)
    elif opt==4:
        os.system(shell+clr)
        print("Training faces")
        print("------------")
        os.system(pyt+'trainer.py')
        print("------------")
        os.system(shell+clr)
    elif opt==5:
        os.system(shell+clr)
        print("Opening Recognizer")
        print("------------")
        os.system(pyt+'recognizer.py')
        print("------------")
        os.system(shell+clr)
    elif opt==6:
        os.system(shell+clr)
        cursor.execute("select * from record;")
        b=cursor.fetchall()
        for i in b:
            header.append(i[0])
        print(tabulate(b, header, tablefmt='fancy_grid'))
        print("------------")
        input("Press enter to continue")
        os.system(shell+clr)
    elif opt==7:
        os.system(shell+clr)
        print("------------")
        print("Thank you for using FaRec\nBase/Source code by: Jacob12138xieyuan\nGithub- https://github.com/Jacob12138xieyuan/easy-real-time-face-recognition-python")
        print("Edited and Developed by Abhinandan Mandal and Ayush Kumar")
        print("Version: Alpha 0.3")
        input("Press enter to exit")
        break
    else:
        print("Invalid choice")
        print("------------")
        os.system(shell+clr)
