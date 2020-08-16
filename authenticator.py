def check():
    import os.path
    return os.path.isfile('./auth.dat')

def reg():
    auth=open("auth.dat","w")
    user=str(input("Enter your MySQL User-ID [press Enter to use default 'root']: "))
    passw=str(input("Enter you MySQL Password [press Enter to use default '1234']: "))
    if user=="":
       user="root"
    if passw=="":
        passw="1234"
    line=[user,"\n",passw]
    auth.writelines(line)
    auth.close()
    return "Login data saved"

def read():
    auth=open("auth.dat","r")
    dat=auth.readlines()
    auth.close()
    uid=dat[0].strip('\n')
    passw=dat[1]
    return uid,passw

    


