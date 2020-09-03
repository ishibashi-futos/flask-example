import pytest
from test_app import client

def test_health_check_ok(client):
  json = client.get("/api/health").get_json()
  assert 'OK' == json['status']

def test_index_ok(client):
  body = client.get("/api/").data
  assert b'Hello, World!' == body
