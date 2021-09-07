# from flask import Flask, request
# app = Flask(__name__)


# @app.route("/concat/<string:name>", methods=["GET"])
# def tha(name):
#     global s
#     s = s + " " + name 
#     return s+ " " +name 


# if __name__ == '__main__':
#     app.run()
#     # app.run(debug = True) #to see the error during development

from re import A
from flask import Flask
app = Flask("__name__")

string = ""

@app.route("/")
def index():
    return """<h1>Welcome!!!</h1>
    <br>
    <h3>Go To : </h3>
    <br>
    <b>/StoreString/arg </b> : for storing arg as string
    <br>
    <b>/Concatenate </b> : to get concatenated strings (all passed till now)
    """

@app.route("/StoreString/<string:text>")
def store(text):
    global string
    string = string + " " + text
    return "<h3>" + text + "</h3>"

@app.route("/Concatenate/")
def concat():
    global string
    return string