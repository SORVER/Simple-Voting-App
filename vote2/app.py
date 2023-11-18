import os
import requests
from flask import Flask, jsonify, render_template,request
from flask_socketio import SocketIO , emit
app = Flask(__name__) # creating the app
app.config["SECRECT_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votes = {"yes":0 , "no":0 , "maybe": 0 }
@app.route("/") 
def index(): 
    return render_template("index.html", votes = votes)

@socketio.on("submit vote") 
def vote(data):
    selection = data["selection"]
    votes[selection]+=1
    emit("annouce vote" , {"selection" : selection} , broadcast=True) # sending data to client , broadcast every one else = true
