import mysql.connector as sq
import authenticator

auth_data = authenticator.read()
uid = auth_data[0]
password = auth_data[1]

db=sq.connect(host='localhost',user=uid,passwd=password,database='farec')
cursor=db.cursor()

choice=int(input("1. Add data individually\n2. Import from spreadsheet\nEnter your choice: "))

while True:
      if choice==2:
###################
            path=input("Enter spreadsheet filename/directory or Drag it here: ")
            path=path.replace("\\","/")
            q1="load data local infile '{}' into table record fields terminated by ',' ignore 1 lines;".format(path)
            print("------------")
            print(q1)
            cursor.execute(q1)

            db.commit()
            print("Spreadsheet Imported")
            print("------------")

            cursor.close()
            db.close()
            break

      elif choice==1:
###################
            select='yes'

            while select=='yes':
                  roll=input("Enter your roll number: ")
                  name=input("Enter your name: ")
                  adm=input("Enter your admission number: ")
                  farec_id=input("Enter your FaRec ID: ")

                  qu="insert into record (roll,name,adm,farec_id) values ("+roll+",'"+name+"',"+adm+","+farec_id+");"
                  print(qu)

                  cursor.execute(qu)
                  db.commit()
                  print("Updated")

                  select=str(input("Enter more student details?(yes/no): "))
            else:
               print('Done!')


            cursor.close()
            db.close()
            break
