def db_crt():
    import mysql.connector as sq
    import time as t
    db=sq.connect(host='localhost',user='root',passwd='1234')
    cursor=db.cursor()
    print("Checking Database")
    check='show databases'
    cursor.execute(check)
    l=cursor.fetchall()
    l=[i[0] for i in l]
    if not 'farec' in l:
        qu='create database farec;'
        print("Database doesn't exist\nCreating database")
        cursor.execute(qu)
        print('Loading',end="")
        for i in range(0,20):
            print(".",end="")
            t.sleep(0.01)
        db.commit()
        db.close()
    else:
        print("\nDatabase found!")

def tb_crt():
    import mysql.connector as sq
    import time as t
    tb=sq.connect(host='localhost',user='root',passwd='1234',database='farec')
    crsr=tb.cursor()
    print("\nChecking Table")
    check2='show tables'
    crsr.execute(check2)
    m=crsr.fetchall()
    m=[i[0] for i in m]
    if not 'record' in m:
        qu2='create table record (roll int(11), name varchar(20), adm int(11), farec_id int(11) PRIMARY KEY);'
        print("Table doesn't exist\nCreating table")
        crsr.execute(qu2)
        print('Loading',end="")
        for i in range(0,20):
            print(".",end="")
            t.sleep(0.01)
        print("\n")
        tb.commit()
        tb.close()
    else:
        print("\nTable found!\n------------\n")
        
