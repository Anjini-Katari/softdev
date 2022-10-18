# DogDino: Anjini, Gabriel, Vivian
# SoftDev
# K11 - Forms
# 2022-10-14
# time spent: 0.5 hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)

    if 'username' in request.args: # error otherwise because request.args (MultiDict) could be empty
        print("***DIAG: request.args['username']  ***") # username is like a key
        print(request.args['username'])

    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' ) #


@app.route("/auth", methods =['POST']) #we need a 'GET' here, otherwise we get a methood not allowed error
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
    return "Waaaa hooo HAAAH"  # response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
