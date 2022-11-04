# TBD's Adventures: Samantha Hua, Anjini Katari, and Emerson Gelobter
# SoftDev
# K12 -- Take and Give
# 2022-10-17
# time spent: 1hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST']) #, 'POST'
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.form ***")
    print(request.form)

    if 'username' in request.args: # error otherwise because request.args (MultiDict) could be empty
        print("***DIAG: request.args['username']  ***") # username is like a key
        print(request.args['username'])

    print("***DIAG: request.headers ***")
    print(request.headers)

    # username: hello
    # password: goodbye
    

    return render_template( 'login.html' ) #


@app.route("/auth", methods =['GET', 'POST']) #we need a 'GET' here, otherwise we get a method not allowed error
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    if 'username' in request.args: # error otherwise because request.args could be empty
        print("***DIAG: request.args['username']  ***")
        print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    print("***DIAG: request.form ***")
    print(request.form)

    if request.method == "POST":
        print("wheee")
        # session['username'] = request.form['username']
        # return redirect(url_for('index'))
    # session['hello'] = "goodbye" #error
    print(session)

    x = ""
    if 'username' in session:
        username = session['username']
        x = "you're logged in"
    else:
        x = "you're not logged in"



    return render_template( 'response.html', user=request.form['username'], x = x, type=request)  # response to a form submission

@app.route('/logout')
def logout():
    session.pop('username')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()