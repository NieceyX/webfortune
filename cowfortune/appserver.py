# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os 
import subprocess

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'
fileName = "out.txt"

@app.before_first_request
def app_init():
    if not (os.path.exists(fileName)):
        f = open(fileName, "x")
        f.close()

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    command = "fortune > " + fileName
    subprocess.call(command, shell=True)
    with open(fileName) as f: 
        return "<pre>" + f.read() + "</pre>"

@app.route('/cowsay/<message>/')
def cowsay(message):
    command = "cowsay " + message + " > " + fileName
    subprocess.call(command, shell=True)
    with open(fileName) as f: 
        return "<pre>" + f.read() + "</pre>"

@app.route('/cowfortune/')
def cowfortune():
    command = "fortune | cowsay > " + fileName
    subprocess.call(command, shell=True)
    with open(fileName) as f: 
        return "<pre>" + f.read() + "</pre>"









