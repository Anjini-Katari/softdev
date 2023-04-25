#Adorable Didactic Elephants: Anjini Katari, Kevin Li
#SoftDev
#K20 -- API keys
#2022-11-21
#time spent: <elapsed time in hours, rounded to nearest tenth>


from flask import Flask
from flask import request
from flask import render_template
import requests
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    
    return render_template("news-magazine.html")

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
