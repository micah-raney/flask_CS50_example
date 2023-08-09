from flask import Flask, render_template, request

app = Flask(__name__) # Turn this file into a Flask app

# Python Decorator assigns the below function to the assigned route.
@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/register")
def register():
	return render_template("success.html")