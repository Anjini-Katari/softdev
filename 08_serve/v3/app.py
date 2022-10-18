# DogDino: Anjini, Gabriel, Vivian
# SoftDev v3
# Oct 6 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? to the console if we run hello_world()
    return "No hablo queso!"

app.debug = True # turns debug mode on, updates the site whenever you change the code without restarting the server
app.run()
