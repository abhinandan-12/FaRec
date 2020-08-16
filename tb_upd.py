def tb_upd():
    import mysql.connector as sq
    from datetime import datetime

    db=sq.connect(host='localhost',user='root',passwd='1234',database='farec')
    cursor=db.cursor()

    now=datetime.now()
    dt=now.strftime("%d_%m_%Y")
    qu="alter table record add "+dt+" varchar(3) default 'no';"
    cursor.execute(qu)
    cursor.close()
    db.close()
    print(dt)
    print("Done!")
tb_upd()
