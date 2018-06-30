#this is a python file
from flask import Flask
from flask import render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/blogs")
def blogs():
  return renter_template("blogs.html")

app.run(debug=true, port=5000)
