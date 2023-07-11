import mysql.connector
from mysql.connector import Error

try:
    con=mysql.connector.connect(host="localhost",db="mukudb",user="muku",password="25456")
    cursor=con.cursor()

    s="create table if not exists users (uid int auto_increment not null primary key,u_first_name varchar(30) not null,u_last_name varchar(30) not null,u_contact bigint(10) not null,u_email varchar(30),u_pass varchar(20) not null);;"
    cursor.execute(s)

except Error as e:
    e


def user_login(email,pw):
    s=f"select u_email from users where u_email='{email}'"
    cursor.execute(s)
    dt=cursor.fetchone()
    try:
        dt=dt[0]
        s=f"select u_pass,u_first_name,u_last_name from users where u_email='{email}'"
        cursor.execute(s)
        ps=cursor.fetchone()
        passw=ps[0]
        fname=ps[1]
        lname=ps[2]
        if passw==pw:
            return ["logged-in",fname,lname,]
        else:
            return ["wrong password"]
    
    except:
        return  ["Email not registered"]
    

#______________________register_user_function__________________

def user_register(fname,lname,u_contact,u_email,u_password):
    s=f"select u_email from users where u_email='{u_email}'"
    cursor.execute(s)
    dt=cursor.fetchone()
    if dt:
        return "email already exists"
    else:
        s=f"insert into users (u_first_name,u_last_name,u_contact,u_email,u_pass) values('{fname}','{lname}','{u_contact}','{u_email}','{u_password}')"
        cursor.execute(s)
        con.commit()
        return "registered"

            
        













