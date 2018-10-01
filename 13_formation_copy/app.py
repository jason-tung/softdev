# azrael - Jason Tung
# SoftDev1 pd8
# K13 -- Echo Echo Echo
# 2018-09-28

# username entered
# request method used
# your greeting to this person

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(app)
    return (render_template("doggy.html"))

@app.route('/auth', methods = ["POST"])
def hello_world1():
    print("app: ", app)
    print("request: ", request)
    return (render_template("kitty.html", usrname=request.form['usrname'], method=request.method))

if __name__ == "__main__":
    app.debug = True
    app.run()
