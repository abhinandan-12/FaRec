def tb_upd():
    import mysql.connector as sq
    from datetime import datetime
    import authenticator
    auth_data = authenticator.read()
    uid = auth_data[0]
    password = auth_data[1]
    db=sq.connect(host='localhost',user=uid,passwd=password,database='farec')
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
