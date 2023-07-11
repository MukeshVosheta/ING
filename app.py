from flask import Flask,render_template,request,redirect,url_for
from db import user_login,user_register
from mailvari import otp_varify
import os


app=Flask(__name__)
app.secret_key=os.urandom(24)



#______________________Main Html Pages______________________

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/t&c")
def tc():
    return render_template('t&c.html')


@app.route("/VarifyEmail/<int:email>")
def email_varify(email):
    return render_template('email_varify.html',email)




#                       Action functions

#________________________login_function______________________

@app.route("/login_validation",methods=["POST"])

def login_validation():
    email=request.form.get("email")
    password=request.form.get("password")
    data=user_login(email,password)
    try:
        if data[0] == 'logged-in':
            return redirect('/')
        else:
            return redirect('/login')
    except:
        return redirect('/login')




#______________________register_function__________________________

@app.route("/register_user",methods=["post"])
def register_user():
    fname=request.form.get("f_name")
    lname=request.form.get("l_name")
    contact=request.form.get("u_contact")
    u_email=request.form.get("u_email")
    u_password=request.form.get("u_password")
    password_2=request.form.get("password_2")
    a=[fname,lname,contact,u_email,u_password] 
    if u_password == password_2:
        #user_register(fname,lname,contact,u_email,u_password)
        #otp_varify(u_email)
        return render_template('email_varify.html',u_email=u_email)
    else:
        return "confirm password"
    

 









if __name__ == "__main__":
    app.run(debug=True)