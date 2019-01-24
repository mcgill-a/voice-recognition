from flask import Flask, render_template, url_for, jsonify, request, redirect, session, flash
from flask_bootstrap import Bootstrap
import os, json, string, datetime, bcrypt, urllib, hashlib

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Load configuration file
app.config.from_pyfile("config/defaults.py")
app.secret_key = app.config['SECRET_KEY']


# Connect to the DB and load tables	
# DB CONNECTION HERE

from improvisor import routes