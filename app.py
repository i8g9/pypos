from flask import Flask, render_template, request, redirect, url_for, jsonify

from db import db_connection

app = Flask(__name__)
