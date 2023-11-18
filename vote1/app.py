import os
import requests
from flask import Flask, jsonify, render_template,request
from flask_socketio import SocketIO , emit
app = Flask(__name__) # creating the app
app.config["SECRECT_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/") 
def index(): 
    return render_template("index.html")


@socketio.on("submit vote") 
def vote(data):
    selection = data["selection"]
    emit("annouce vote" , {"selection" : selection} , broadcast=True) # sending data to client , broadcast every one else = true
