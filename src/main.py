from flask import Flask
from controllers import users, books, index, todos

app = Flask(__name__)

# route
app.register_blueprint(users.app, url_prefix = "/api")
app.register_blueprint(books.app, url_prefix = "/api")
app.register_blueprint(index.app, url_prefix = "/api")
app.register_blueprint(todos.app, url_prefix = "/api")

if __name__ == '__main__':
  app.run()
