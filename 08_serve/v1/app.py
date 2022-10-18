# DogDino: Anjini, Gabriel, Vivian
# SoftDev v1
# Oct 6 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask
                      #__name__ = __main__

@app.route("/")       #assign fxn to route
def hello_world():
    # why no print statement? same thing happens on the surface though
    # answer: print(__name__) does nothing here since it's not being returned, so it won't be displayed on the webpage
    return "No hablo queso!"

app.run()

