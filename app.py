from flask import Flask, render_template, request, flash

app = Flask(__name__) # Create a class for the app
app.secret_key = "pega123"

@app.route("/hello")
def index():
    flash("What is your name?")
    return render_template("index.html")

#Different route for when the button is pushed
@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")
