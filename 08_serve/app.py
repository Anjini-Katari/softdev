# DogDino: Anjini, Gabriel, Vivian
# SoftDev v0
# K08 - Create a webpage with random occupation
# Oct 6-7 2022

import random

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    job_dict = create_dict("occupations.csv")
    return weighted_random(job_dict)

# if __name__ == "__main__":  # true if this file NOT imported
#     app.debug = True        # enable auto-reload upon code change
#     app.run()

def create_dict(file_name):
    file = open(filename, 'r')
    content = file.read()
    #splitting the file's info by line and making it a list
    total_list = content.split('\n')
    # getting rid of first and last line
    total_list = total_list[1:-2]
    job_dict = {}

    for job in total_list:
        # for each job in the list, split it by the last comma once
        job_list = job.rsplit(',',1)
        # read the occupation title into dict as key, read the percentage into dict as value
        job_dict[job_list[0]] = float(job_list[1]) # typecast percentage from string to float
    return job_dict

def weighted_random(job_dict):
    #use python's built-in weighted random choice function to get a job title
    random_job = random.choices(list(dict.keys(job_dict)), weights=list(dict.values(job_dict)))
    # since random_job is a list consisting of one element, we can print the first element
    return random_job[0]
