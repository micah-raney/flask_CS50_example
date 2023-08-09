from flask import Flask, render_template, request

app = Flask(__name__) # Turn this file into a Flask app

registrants = {}

# Python Decorator assigns the below function to the assigned route.
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	sport = request.form.get("sport")
	registrants[name] = sport
	return render_template("success.html")


@app.route("/registrants")
def registrant_page():
	return render_template("registrants.html", registrants=registrants)