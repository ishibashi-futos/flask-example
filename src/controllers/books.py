from flask import Blueprint, request
from flask_restful import Resource, Api

books = [
  {"id": 1, "title": "Hello, World"}
]

app = Blueprint('books', __name__)

@app.route("/books", methods = ["GET"])
def get():
  return {"books": books}

@app.route('/books/<int:id>', methods = ["GET"])
def byId(id):
  items = list(filter(lambda book: book["id"] == id, books))
  return {"books": items}

@app.route('/books', methods = ['POST'])
def create():
  title = request.json['title']
  books.append({"id": len(books) + 1, "title": title})
  return {"books": list(filter(lambda book: book["title"] == title, books))}
