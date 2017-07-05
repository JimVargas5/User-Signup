from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return redirect("/signup")


@app.route("/signup")
def DisplaySignup():
    return render_template('MainForm.html')


@app.route("/signup", methods= ['POST'])
def ValidateSignup():
    username = cgi.escape(
        request.form['username'])
    password = cgi.escape(
        request.form['password'])
    Confirmpass = cgi.escape(
        request.form['verify'])
    email = cgi.escape(
        request.form['email'])

    usernameEr = ""
    passwordEr = ""
    ConfirmpassEr = ""
    emailEr = ""

    if  username == "":
        usernameEr = "That's not a valid username"
    elif len(username) > 20 or len(username) < 3:
        usernameEr = "That's not a valid username"

    if password == "":
        passwordEr = "That's not a valid password"
    elif len(password) > 20 or len(password) < 3:
        passwordEr = "That's not a valid password"
    
    if Confirmpass == "":
        ConfirmpassEr = "The passwords don't match"
    elif not password == Confirmpass:
        ConfirmpassEr = "The passwords don't match"

    if len(email) > 0:
        if email.count("@") < 1:
            emailEr = "That's not a valid email"
        elif email.count(".") < 1:
            emailEr = "That's not a valid email"
        elif email.count(" ") > 0:
            emailEr = "That's not a valid email"
        elif len(email) > 20 or len(email) < 3:
            emailEr = "That's not a valid email"
    
    if not usernameEr and not passwordEr and not ConfirmpassEr and not emailEr:
        return redirect('/welcome?username= {0}'.format(username))
        #return "<h1> Hello, "+ username +"! </h1>"
    else:
        return render_template('MainForm.html', 
            username= username, usernameEr= usernameEr, 
            passwordEr= passwordEr, ConfirmpassEr= ConfirmpassEr,
            email= email, emailEr= emailEr)


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username= username)



app.run()

