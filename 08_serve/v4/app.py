# DogDino: Anjini, Gabriel, Vivian
# SoftDev v4
# Oct 6 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__) # prints __main__ to the console if this is not an imported file
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# all starter kits have the same looking webpage surface level