def table_crt():
    import mysql.connector as sq
    import time as t
    db=sq.connect(host='localhost',user='root',passwd='1234')
    print("Checking Database")
    print('Loading',end="")
    for i in range(0,20):
        print(".",end="")
        t.sleep(0.01)
    qu='create database farec;'
    try:
        cursor.execute(qu)
    except:
        t.sleep(0.5)
        print("\nDatabase  found!\nChecking Table")
        print('Loading',end="")
        for i in range(0,20):
            print(".",end="")
            t.sleep(0.01)
        qu1='create table record (roll int(11), name varchar(20), adm int(11), farec_id int(11) PRIMARY KEY);'
        try:
            cursor.execute(qu1)
        except:
            t.sleep(0.01)
            print("\nTable found!\n------------")
