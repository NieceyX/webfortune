# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os 
import subprocess

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    command = "fortune"
    p = subprocess.run(command, stdout=subprocess.PIPE)
    output = str(p.stdout).replace("\\n","<br />").replace("\\t","    ").replace("\\","")
    return "<pre>" + output[2:-1] + "</pre>"

@app.route('/cowsay/<message>/')
def cowsay(message):
    command = "cowsay " + message
    p = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = str(p.stdout).replace("\\n","<br />").replace("\\t","    ").replace("\\","")
    return "<pre>" + output[2:-1] + "</pre>"

@app.route('/cowfortune/')
def cowfortune():
    command = "fortune | cowsay"
    p = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = str(p.stdout).replace("\\n","<br />").replace("\\t","    ").replace("\\'","'").replace("\\","")
    return "<pre>" + output[2:-1] + "</pre>"









