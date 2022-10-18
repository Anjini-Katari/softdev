# DogDino: Anjini, Gabriel, Vivian
# SoftDev v0
# Oct 6 2022

from flask import Flask
app = Flask(__name__) # app is an object that stores the Flask app/website

@app.route("/") # sets the route/path of the website (links a route to a function defined below)
def hello_world():
    print(__name__) # prints __name__(predefined variable) to the console
    return "No hablo queso!"  # whatever the function returns gets printed on the webpage

app.run()  # starts a webserver with the routes defined in this file; you can now see the webpage stuff
                
