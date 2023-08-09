from flask import Flask, render_template, request

app = Flask(__name__) # Turn this file into a Flask app

# Python Decorator assigns the below function to the assigned route.
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method=="GET":
		return render_template("index.html")
	elif request.method=="POST":
		# check for value or return default
		return render_template("greet.html", name=request.form.get("name", "World"))
