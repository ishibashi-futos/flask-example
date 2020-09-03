from flask import Blueprint, request
from flask_restful import Resource, Api

app = Blueprint('index', __name__)

@app.route("/", methods = ["GET"])
def index():
  return "Hello, World!"

@app.route("/health", methods = ["GET"])
def health_check():
  return {
    "status": "OK"
  }
