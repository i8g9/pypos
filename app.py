from flask import Flask, render_template, request, redirect, url_for, jsonify

# from db import db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('createproduct.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')


