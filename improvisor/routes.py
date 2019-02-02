from flask import Flask, render_template, url_for, jsonify, request, redirect, session, flash
from flask_bootstrap import Bootstrap
import os, json, string, datetime, urllib, hashlib
from improvisor import app

@app.route('/', methods=['GET'])
def index():
	tags = ['database', 'server', 'improvise', 'group project', 'image', 'youtube video']
	return render_template('index.html', tags=tags)

@app.route('/presenter', methods=['GET'])
def presenter():
	return render_template('presenter.html')

@app.route('/controller', methods=['GET'])
def controller():
	tags = ['database', 'server', 'improvise', 'group project', 'image', 'youtube video']
	return render_template('controller.html', tags=tags)