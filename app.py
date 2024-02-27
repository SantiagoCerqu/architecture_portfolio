from flask import Flask, render_template, Request
from information import df
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/biografia")
def biografia():
    return render_template("biografia.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/proyectos")
def proyectos():
    return render_template("proyectos.html", df=df)

@app.route("/proyecto/<code>")
def proyecto(code):
    # Get the names of all the images of the project
    # Get the images folder path and change os path
    
    path = os.getcwd()
    img_path = f"{path}/static/images/{code}"

    images = [f"images/{code}/{image}" for image in os.listdir(img_path) if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg")]

    return render_template("proyecto.html", df =df, pr_code=code, images=images)