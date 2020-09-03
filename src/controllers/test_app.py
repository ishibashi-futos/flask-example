import pytest
from flask import Flask
import users, books, index

def create_app(test_config = None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    EXECUTOR_TYPE="process",
    EXECUTOR_MAX_WORKERS="1",
  )
  app.register_blueprint(users.app, url_prefix = "/api")
  app.register_blueprint(books.app, url_prefix = "/api")
  app.register_blueprint(index.app, url_prefix = "/api")
  return app

@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True
  with app.test_client() as client:
    yield client
